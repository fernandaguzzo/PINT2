function cadastrarCliente() {
    const nome = document.getElementById('nome_cliente').value;

    fetch('/cadastrar_cliente', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'nome': nome
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.message;
        document.getElementById('nome_cliente').value = ''; // Limpar campo
    })
    .catch(error => console.error('Erro:', error));
}

function cadastrarPousada() {
    const nome = document.getElementById('nome_pousada').value;

    fetch('/cadastrar_pousada', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'nome': nome
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.message;
        document.getElementById('nome_pousada').value = ''; // Limpar campo
    })
    .catch(error => console.error('Erro:', error));
}

function listarClientes() {
    fetch('/listar_clientes')
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById('lista_clientes');
            lista.innerHTML = ''; // Limpar lista existente
            data.forEach(cliente => {
                const li = document.createElement('li');
                li.innerText = cliente.nome;
                lista.appendChild(li);
            });
        })
        .catch(error => console.error('Erro:', error));
}

function listarPousadas() {
    fetch('/listar_pousadas')
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById('lista_pousadas');
            lista.innerHTML = ''; // Limpar lista existente
            data.forEach(pousada => {
                const li = document.createElement('li');
                li.innerText = pousada.nome;
                lista.appendChild(li);
            });
        })
        .catch(error => console.error('Erro:', error));
}
