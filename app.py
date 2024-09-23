from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('tynedb.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para criar tabelas (executar uma vez)
@app.route('/criar_tabelas', methods=['GET'])
def criar_tabelas():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pousada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            localizacao TEXT NOT NULL,
            preco_diaria REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            contato TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Reserva (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            pousada_id INTEGER NOT NULL,
            data_inicio TEXT NOT NULL,
            data_fim TEXT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
            FOREIGN KEY (pousada_id) REFERENCES Pousada(id)
        )
    ''')

    conn.commit()
    conn.close()
    return "Tabelas criadas com sucesso!"

# Rota para cadastrar pousada
@app.route('/cadastrar_pousada', methods=['POST'])
def cadastrar_pousada():
    dados = request.json
    nome = dados.get('nome')
    localizacao = dados.get('localizacao')
    preco_diaria = float(dados.get('preco_diaria'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Pousada (nome, localizacao, preco_diaria)
        VALUES (?, ?, ?)
    ''', (nome, localizacao, preco_diaria))
    conn.commit()
    conn.close()

    return jsonify({"message": "Pousada cadastrada com sucesso!"})

# Rota para cadastrar cliente
@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    dados = request.json
    nome = dados.get('nome')
    contato = dados.get('contato')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Cliente (nome, contato)
        VALUES (?, ?)
    ''', (nome, contato))
    conn.commit()
    conn.close()

    return jsonify({"message": "Cliente cadastrado com sucesso!"})

# Rota para fazer reserva
@app.route('/fazer_reserva', methods=['POST'])
def fazer_reserva():
    dados = request.json
    cliente_id = int(dados.get('cliente_id'))
    pousada_id = int(dados.get('pousada_id'))
    data_inicio = dados.get('data_inicio')
    data_fim = dados.get('data_fim')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Reserva (cliente_id, pousada_id, data_inicio, data_fim)
        VALUES (?, ?, ?, ?)
    ''', (cliente_id, pousada_id, data_inicio, data_fim))
    conn.commit()
    conn.close()

    return jsonify({"message": "Reserva feita com sucesso!"})

# Rota para listar pousadas
@app.route('/listar_pousadas', methods=['GET'])
def listar_pousadas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Pousada')
    pousadas = cursor.fetchall()
    conn.close()

    pousada_list = [{"id": pousada["id"], "nome": pousada["nome"], "localizacao": pousada["localizacao"], "preco_diaria": pousada["preco_diaria"]} for pousada in pousadas]
    return jsonify(pousada_list)

# Rota para listar clientes
@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cliente')
    clientes = cursor.fetchall()
    conn.close()

    cliente_list = [{"id": cliente["id"], "nome": cliente["nome"], "contato": cliente["contato"]} for cliente in clientes]
    return jsonify(cliente_list)

if __name__ == "__main__":
    app.run(debug=True)
