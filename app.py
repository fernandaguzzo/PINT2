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
    if nome:
        db.insert({'tipo': 'cliente', 'nome': nome})
        return jsonify({'message': 'Cliente cadastrado com sucesso!'}), 200
    return jsonify({'message': 'Falha ao cadastrar cliente!'}), 400

@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    Cliente = Query()
    clientes = db.search(Cliente.tipo == 'cliente')
    return jsonify(clientes), 200

@app.route('/cadastrar_pousada', methods=['POST'])
def cadastrar_pousada():
    nome = request.form.get('nome')
    if nome:
        db.insert({'tipo': 'pousada', 'nome': nome})
        return jsonify({'message': 'Pousada cadastrada com sucesso!'}), 200
    return jsonify({'message': 'Falha ao cadastrar pousada!'}), 400

@app.route('/listar_pousadas', methods=['GET'])
def listar_pousadas():
    Pousada = Query()
    pousadas = db.search(Pousada.tipo == 'pousada')
    return jsonify(pousadas), 200

if __name__ == '__main__':
    app.run(debug=True)
