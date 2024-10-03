Uso de Portas e Implementação de HTML no Projeto Flask
Este documento fornece informações sobre como usar portas em uma aplicação Flask, além de orientações sobre como implementar sua própria interface HTML.

Índice
Introdução
Configuração do Ambiente
Uso de Portas no Flask
Estrutura do Projeto
Implementação do HTML
Exemplo de Código HTML
Executando a Aplicação
Considerações Finais
Introdução
Este projeto utiliza Python com o framework Flask para criar uma aplicação de gerenciamento de pousadas. A aplicação usa TinyDB como banco de dados e permite funcionalidades como cadastro de clientes e pousadas, reserva de pousadas, e listagem de informações.

Configuração do Ambiente
Antes de começar, certifique-se de que você possui o Python 3.x instalado em sua máquina. Você também precisará instalar o Flask e o TinyDB. Para instalar, execute os seguintes comandos:

bash
Copiar código
pip install Flask
pip install tinydb
Uso de Portas no Flask
Ao executar uma aplicação Flask, você pode especificar a porta em que a aplicação será acessível. A porta padrão é 5000, mas você pode escolher outras portas que não sejam consideradas "inseguras" (como 80, 443, 8080, etc.).

Portas Seguras
Algumas portas seguras que você pode usar incluem:

8080 - Usada frequentemente para aplicações web em desenvolvimento.
3000 - Usada em muitas aplicações Node.js e outros frameworks.
5001 - Comum para desenvolvimento.
8000 - Usada frequentemente em ambientes de teste.
No código do Flask, você pode especificar a porta ao iniciar a aplicação:

python
Copiar código
if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Usando a porta 8080
Estrutura do Projeto
A estrutura básica do projeto deve ser semelhante a esta:

bash
Copiar código
/seu_projeto
│
├── app.py               # Código da aplicação Flask
├── db.json              # Banco de dados TinyDB
└── templates
    └── index.html       # Página HTML para interação com o usuário
Implementação do HTML
Para implementar sua própria interface HTML, você deve criar um arquivo HTML na pasta templates. O Flask irá renderizar esse arquivo ao acessar a rota principal (/).

Como Funciona
Quando um usuário acessa a aplicação, a rota @app.route('/') renderiza o arquivo index.html.
Você pode criar formulários e botões para interagir com as rotas da API definidas no Flask.
Exemplo de Código HTML
Aqui está um exemplo simples de como você pode estruturar seu arquivo index.html:

html
Copiar código
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Pousadas</title>
    <script src="script.js" defer></script>
</head>
<body>
    <h1>Cadastro de Pousadas</h1>
    <form id="form_pousada">
        Nome da Pousada: <input type="text" id="nome" required><br>
        ID da Pousada: <input type="text" id="id_pousada" required><br>
        <button type="submit">Cadastrar Pousada</button>
    </form>

    <div id="resultado"></div>
</body>
</html>
Neste exemplo, o formulário coleta o nome e o ID da pousada. Você deve adicionar um arquivo JavaScript (script.js) para enviar as informações para o backend via AJAX.

Executando a Aplicação
Para executar sua aplicação Flask, navegue até o diretório do projeto no terminal e execute o seguinte comando:

bash
Copiar código
python app.py
A aplicação estará disponível no navegador em http://localhost:8080 (ou a porta que você escolheu).

Uso das Rotas da Aplicação Flask
Esta seção do README fornece uma descrição detalhada das rotas disponíveis na aplicação Flask, incluindo como cada uma funciona e suas funcionalidades.

Rotas Disponíveis
/ - Página Inicial

Método: GET
Descrição: Renderiza a página HTML principal (index.html), onde os usuários podem interagir com o sistema.
Uso: Acesse diretamente no navegador: http://localhost:8080.
/cadastrar_cliente - Cadastro de Cliente

Método: POST
Descrição: Recebe dados de um cliente e os insere no banco de dados. Os dados devem incluir nome, CPF ou CNPJ, telefone e e-mail.
Parâmetros Requeridos:
nome: Nome do cliente.
cpf_cnpj: CPF ou CNPJ do cliente.
telefone: Telefone do cliente.
email: E-mail do cliente.
Resposta:
200: Cliente cadastrado com sucesso.
400: Falha ao cadastrar cliente (campos vazios).
Uso: Enviar os dados do cliente via um formulário HTML utilizando AJAX.
/listar_clientes - Listar Clientes

Método: GET
Descrição: Retorna uma lista de todos os clientes cadastrados no banco de dados.
Resposta: Lista em formato JSON com as informações dos clientes.
Uso: Acessar a rota para obter os dados de clientes cadastrados.
/cadastrar_pousada - Cadastro de Pousada

Método: POST
Descrição: Recebe dados de uma pousada e os insere no banco de dados. Os dados devem incluir nome da pousada e ID da pousada.
Parâmetros Requeridos:
nome: Nome da pousada.
id_pousada: ID da pousada.
Resposta:
200: Pousada cadastrada com sucesso.
400: Falha ao cadastrar pousada (campos vazios).
Uso: Enviar os dados da pousada via um formulário HTML utilizando AJAX.
/listar_pousadas - Listar Pousadas

Método: GET
Descrição: Retorna uma lista de todas as pousadas cadastradas no banco de dados.
Resposta: Lista em formato JSON com as informações das pousadas.
Uso: Acessar a rota para obter os dados de pousadas cadastradas.
/reservar_pousada - Reservar Pousada

Método: POST
Descrição: Recebe dados de reserva e adiciona a reserva ao banco de dados, relacionando o CPF ou CNPJ do cliente com o ID da pousada. Verifica se a pousada já está reservada antes de realizar a reserva.
Parâmetros Requeridos:
cpf_cnpj: CPF ou CNPJ do cliente que está reservando.
pousada_id: ID da pousada a ser reservada.
Resposta:
200: Reserva feita com sucesso.
400: Pousada já reservada ou campos vazios.
Uso: Enviar os dados de reserva via um formulário HTML utilizando AJAX.
/listar_pousadas_reservadas - Listar Pousadas Reservadas

Método: GET
Descrição: Retorna uma lista de todas as pousadas que já foram reservadas, incluindo informações do cliente e da pousada.
Resposta: Lista em formato JSON com as informações das pousadas reservadas e dos clientes.
Uso: Acessar a rota para obter os dados das pousadas reservadas.
/listar_pousadas_livres - Listar Pousadas Livres

Método: GET
Descrição: Retorna uma lista de todas as pousadas que ainda estão disponíveis para reserva.
Resposta: Lista em formato JSON com as informações das pousadas livres.
Uso: Acessar a rota para obter os dados das pousadas disponíveis.
/remover_reserva - Remover Reserva

Método: POST
Descrição: Remove uma reserva existente, utilizando o CPF ou CNPJ do cliente e o ID da pousada.
Parâmetros Requeridos:
cpf_cnpj: CPF ou CNPJ do cliente que fez a reserva.
pousada_id: ID da pousada cuja reserva será removida.
Resposta:
200: Reserva removida com sucesso.
404: Reserva não encontrada.
400: Falha ao remover reserva (campos vazios).
Uso: Enviar os dados da reserva a ser removida via um formulário HTML utilizando AJAX.
Como Usar as Rotas
As rotas podem ser acessadas diretamente via chamadas HTTP, e o uso do JavaScript (AJAX) é recomendado para interagir com essas rotas. Ao implementar seu próprio HTML, você pode criar formulários que se conectem às rotas apropriadas, utilizando o método correspondente (GET ou POST) e enviando os parâmetros necessários.

Exemplo de uma chamada AJAX para cadastrar um cliente:

javascript
Copiar código
fetch('/cadastrar_cliente', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
        'nome': 'João da Silva',
        'cpf_cnpj': '12345678901',
        'telefone': '1234567890',
        'email': 'joao@example.com'
    })
})
.then(response => response.json())
.then(data => console.log(data.message))
.catch(error => console.error('Error:', error));
Considerações Finais
Essas rotas formam a espinha dorsal da sua aplicação de gerenciamento de pousadas. Ao integrar suas próprias páginas HTML com essas rotas, você poderá criar uma interface rica e funcional que se comunica perfeitamente com o backend da aplicação.

Se tiver dúvidas sobre como implementar ou interagir com essas rotas, consulte a documentação do Flask ou entre em contato para obter suporte.

Erros frequentes:

1-Pagina carregando infinitamente

Soluções:

1-No app.py, ao final do codigo pode se ver uma area com port, use algumas das seguintes portas no lugar da atual:

80, 443, 8080, 8443, 3000, 3001, 5001, 5002, 7000, 7001, 8000, 8001, 9000, 9001, 9999, 30000, 40000, 50000, 60000, 80000, 10000, 20000, 25432, 65000, 58000, 8081, 8888, 3002, 3003, 5003


