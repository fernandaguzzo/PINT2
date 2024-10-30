from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from tinydb import TinyDB, Query
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Chave secreta para gerenciamento de sessão

# Inicializa o TinyDB para pousadas, clientes e funcionários
db = TinyDB('db.json')
db_funcionarios = TinyDB('funcionarios.json')  # Banco de dados para login de funcionários
Funcionario = Query()

# Rota inicial para tela de login
@app.route('/')
def login():
    if 'user' in session:  # Verifica se o usuário já está logado
        return redirect(url_for('index'))
    return render_template('login.html')

# Rota para processar o login
@app.route('/login', methods=['POST'])
def login_post():
    cpf_cnpj = request.form.get('cpf_cnpj')
    senha = request.form.get('senha')
    
    funcionario = db_funcionarios.search(Funcionario.cpf_cnpj == cpf_cnpj)
    
    if funcionario and check_password_hash(funcionario[0]['senha'], senha):
        session['user'] = funcionario[0]['cpf_cnpj']  # Armazena o login na sessão
        return redirect(url_for('index'))  # Redireciona para o index.html
    else:
        return jsonify({'message': 'Falha no login! Verifique suas credenciais.'})

# Rota para o dashboard (redirecionado para o index.html)
@app.route('/index')
def index():
    if 'user' in session:
        return render_template('index.html', user=session['user'])
    else:
        return redirect(url_for('login'))

# Rota para cadastrar novos funcionários
@app.route('/cadastrar_funcionario', methods=['POST'])
def cadastrar_funcionario():
    nome = request.form.get('nome')
    cpf_cnpj = request.form.get('cpf_cnpj')
    senha = request.form.get('senha')
    
    # Hash da senha para segurança
    senha_hash = generate_password_hash(senha)

    if db_funcionarios.search(Funcionario.cpf_cnpj == cpf_cnpj):
        return jsonify({'message': 'Funcionário já cadastrado!'})

    db_funcionarios.insert({
        'nome': nome,
        'cpf_cnpj': cpf_cnpj,
        'senha': senha_hash
    })
    return jsonify({'message': 'Funcionário cadastrado com sucesso!'})

# Rota para cadastrar clientes
@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form.get('nome')
    cpf_cnpj = request.form.get('cpf_cnpj')
    telefone = request.form.get('telefone')
    email = request.form.get('email')

    if nome and cpf_cnpj and telefone and email:
        db.insert({
            'tipo': 'cliente',
            'nome': nome,
            'cpf_cnpj': cpf_cnpj,
            'telefone': telefone,
            'email': email
        })
        return jsonify({'message': 'Cliente cadastrado com sucesso!'}), 200
    return jsonify({'message': 'Falha ao cadastrar cliente! Campos vazios.'}), 400

# Rota para listar clientes
@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    Cliente = Query()
    clientes = db.search(Cliente.tipo == 'cliente')
    return jsonify(clientes), 200

# Rota para cadastrar pousadas
@app.route('/cadastrar_pousada', methods=['POST'])
def cadastrar_pousada():
    nome = request.form.get('nome')
    pousada_id = request.form.get('id_pousada')  # Atualizado para 'id_pousada'

    if nome and pousada_id:
        try:
            db.insert({'tipo': 'pousada', 'nome': nome, 'id': pousada_id})  # Inserindo no banco de dados
            return jsonify({'message': 'Pousada cadastrada com sucesso!'}), 200
        except Exception as e:
            return jsonify({'message': 'Falha ao cadastrar pousada!', 'error': str(e)}), 500
    return jsonify({'message': 'Falha ao cadastrar pousada! Campos vazios.'}), 400

# Rota para listar pousadas
@app.route('/listar_pousadas', methods=['GET'])
def listar_pousadas():
    Pousada = Query()
    pousadas = db.search(Pousada.tipo == 'pousada')
    return jsonify(pousadas), 200

# Rota para reservar pousada
@app.route('/reservar_pousada', methods=['POST'])
def reservar_pousada():
    cpf_cnpj = request.form.get('cpf_cnpj')
    pousada_id = request.form.get('pousada_id')

    if cpf_cnpj and pousada_id:
        # Verificar se a pousada já possui uma reserva
        reservas = db.search((Query().tipo == 'reserva') & (Query().pousada_id == pousada_id))
        if reservas:
            return jsonify({'message': 'Pousada já reservada!'}), 400
        
        # Adicionar reserva
        db.insert({'tipo': 'reserva', 'cpf_cnpj': cpf_cnpj, 'pousada_id': pousada_id})
        return jsonify({'message': 'Reserva feita com sucesso!'}), 200
    return jsonify({'message': 'Falha ao reservar pousada! Campos vazios.'}), 400

# Rota para listar pousadas reservadas
@app.route('/listar_pousadas_reservadas', methods=['GET'])
def listar_pousadas_reservadas():
    reservas = db.search(Query().tipo == 'reserva')
    pousadas_reservadas_info = []

    for reserva in reservas:
        pousada_info = db.search((Query().tipo == 'pousada') & (Query().id == reserva['pousada_id']))
        cliente_info = db.search((Query().tipo == 'cliente') & (Query().cpf_cnpj == reserva['cpf_cnpj']))
        
        if pousada_info and cliente_info:
            pousada_detalhes = pousada_info[0]
            cliente_detalhes = cliente_info[0]
            pousadas_reservadas_info.append({
                'pousada_nome': pousada_detalhes['nome'],
                'pousada_id': pousada_detalhes['id'],
                'cliente_nome': cliente_detalhes['nome'],
                'cliente_cpf_cnpj': cliente_detalhes['cpf_cnpj']
            })
    
    return jsonify(pousadas_reservadas_info), 200

@app.route('/listar_pousadas_livres', methods=['GET'])
def listar_pousadas_livres():
    reservas = db.all()
    pousadas_reservadas = set()
    
    for reserva in reservas:
        if reserva['tipo'] == 'reserva':
            pousadas_reservadas.add(reserva['pousada_id'])
    
    pousadas_livres_info = []
    pousadas = db.search(Query().tipo == 'pousada')
    
    for pousada in pousadas:
        if pousada['id'] not in pousadas_reservadas:
            pousadas_livres_info.append(pousada)
    
    return jsonify(pousadas_livres_info), 200

# Rota para remover reserva
@app.route('/remover_reserva', methods=['POST'])
def remover_reserva():
    cpf_cnpj = request.form.get('cpf_cnpj')
    pousada_id = request.form.get('pousada_id')

    if cpf_cnpj and pousada_id:
        Reserva = Query()
        reserva = db.search((Reserva.tipo == 'reserva') & (Reserva.cpf_cnpj == cpf_cnpj) & (Reserva.pousada_id == pousada_id))
        
        if reserva:
            db.remove((Reserva.tipo == 'reserva') & (Reserva.cpf_cnpj == cpf_cnpj) & (Reserva.pousada_id == pousada_id))
            return jsonify({'message': 'Reserva removida com sucesso!'}), 200
        return jsonify({'message': 'Reserva não encontrada!'}), 404
    return jsonify({'message': 'Falha ao remover reserva! Campos vazios.'}), 400

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Usando a porta 8080
