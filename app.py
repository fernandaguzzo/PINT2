from flask import Flask, request, jsonify, render_template
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    Cliente = Query()
    clientes = db.search(Cliente.tipo == 'cliente')
    return jsonify(clientes), 200

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

@app.route('/listar_pousadas', methods=['GET'])
def listar_pousadas():
    Pousada = Query()
    pousadas = db.search(Pousada.tipo == 'pousada')
    return jsonify(pousadas), 200

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

@app.route('/listar_pousadas_reservadas', methods=['GET'])
def listar_pousadas_reservadas():
    reservas = db.all()
    pousadas_reservadas = set()
    for reserva in reservas:
        if reserva['tipo'] == 'reserva':
            pousadas_reservadas.add(reserva['pousada_id'])
    
    pousadas_reservadas_info = []
    for pousada_id in pousadas_reservadas:
        pousada_info = db.search((Query().tipo == 'pousada') & (Query().id == pousada_id))
        if pousada_info:
            pousadas_reservadas_info.append(pousada_info[0])  # Adiciona a pousada correspondente
    
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

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Usando a porta 8080
