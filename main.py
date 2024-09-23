import sqlite3

def cadastrar_pousada():
    nome = input("Nome da pousada: ")
    localizacao = input("Localização: ")
    preco_diaria_str = input("Preço da diária: ")

    # Substitui vírgula por ponto antes de converter para float
    preco_diaria = float(preco_diaria_str.replace(',', '.'))

    conn = sqlite3.connect('tynedb.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Pousada (nome, localizacao, preco_diaria)
        VALUES (?, ?, ?)
    ''', (nome, localizacao, preco_diaria))
    conn.commit()
    conn.close()

    print("Pousada cadastrada com sucesso!\n")

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    contato = input("Contato: ")

    conn = sqlite3.connect('tynedb.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Cliente (nome, contato)
        VALUES (?, ?)
    ''', (nome, contato))
    conn.commit()
    conn.close()

    print("Cliente cadastrado com sucesso!\n")

def fazer_reserva():
    cliente_id = int(input("ID do cliente: "))
    pousada_id = int(input("ID da pousada: "))
    data_inicio = input("Data de início (YYYY-MM-DD): ")
    data_fim = input("Data de fim (YYYY-MM-DD): ")

    conn = sqlite3.connect('tynedb.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Reserva (cliente_id, pousada_id, data_inicio, data_fim)
        VALUES (?, ?, ?, ?)
    ''', (cliente_id, pousada_id, data_inicio, data_fim))
    conn.commit()
    conn.close()

    print("Reserva feita com sucesso!\n")

def listar_pousadas():
    conn = sqlite3.connect('tynedb.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Pousada')
    pousadas = cursor.fetchall()
    conn.close()

    for pousada in pousadas:
        print(f"ID: {pousada[0]}, Nome: {pousada[1]}, Localização: {pousada[2]}, Preço: {pousada[3]}")
    print()

def listar_clientes():
    conn = sqlite3.connect('tynedb.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cliente')
    clientes = cursor.fetchall()
    conn.close()

    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Contato: {cliente[2]}")
    print()

def menu():
    while True:
        print("1. Cadastrar Pousada")
        print("2. Cadastrar Cliente")
        print("3. Fazer Reserva")
        print("4. Listar Pousadas")
        print("5. Listar Clientes")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pousada()
        elif opcao == '2':
            cadastrar_cliente()
        elif opcao == '3':
            fazer_reserva()
        elif opcao == '4':
            listar_pousadas()
        elif opcao == '5':
            listar_clientes()
        elif opcao == '6':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
