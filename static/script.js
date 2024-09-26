function cadastrarCliente() {
    const nome = document.getElementById('nome_cliente').value;
    const cpf_cnpj = document.getElementById('cpf_cnpj').value;
    const telefone = document.getElementById('telefone').value;
    const email = document.getElementById('email').value;

    fetch('/cadastrar_cliente', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'nome': nome,
            'cpf_cnpj': cpf_cnpj,
            'telefone': telefone,
            'email': email
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.message;
        document.getElementById('nome_cliente').value = ''; // Limpar campo
        document.getElementById('cpf_cnpj').value = ''; // Limpar campo
        document.getElementById('telefone').value = ''; // Limpar campo
        document.getElementById('email').value = ''; // Limpar campo
    })
    .catch(error => console.error('Erro:', error));
}

function cadastrarPousada() {
    const id_pousada = document.getElementById('id_pousada').value;  
    const nome_pousada = document.getElementById('nome_pousada').value;

    fetch('/cadastrar_pousada', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'id_pousada': id_pousada,  
            'nome': nome_pousada
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.message;
        document.getElementById('id_pousada').value = ''; // Limpar campo
        document.getElementById('nome_pousada').value = ''; // Limpar campo
    })
    .catch(error => console.error('Erro:', error));
}

function reservarPousada() {
    const cpf_cnpj = document.getElementById('cpf_reserva').value;
    const pousada_id = document.getElementById('id_pousada_reserva').value;

    fetch('/reservar_pousada', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'cpf_cnpj': cpf_cnpj,
            'pousada_id': pousada_id
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.message;
        document.getElementById('cpf_reserva').value = ''; // Limpar campo
        document.getElementById('id_pousada_reserva').value = ''; // Limpar campo
    })
    .catch(error => console.error('Erro:', error));
}

function listarClientes() {
    fetch('/listar_clientes')
    .then(response => response.json())
    .then(data => {
        const lista = document.getElementById('lista_clientes');
        lista.innerHTML = '';
        data.forEach(cliente => {
            const li = document.createElement('li');
            li.textContent = `${cliente.nome} - CPF/CNPJ: ${cliente.cpf_cnpj}`;
            lista.appendChild(li);
        });
    });
}

function listarPousadas() {
    fetch('/listar_pousadas')
    .then(response => response.json())
    .then(data => {
        const lista = document.getElementById('lista_pousadas');
        lista.innerHTML = '';
        data.forEach(pousada => {
            const li = document.createElement('li');
            li.textContent = `${pousada.nome} - ID: ${pousada.id}`;
            lista.appendChild(li);
        });
    });
}

function listarPousadasReservadas() {
    fetch('/listar_pousadas_reservadas')
    .then(response => response.json())
    .then(data => {
        const lista = document.getElementById('lista_pousadas_reservadas');
        lista.innerHTML = '';
        data.forEach(pousada => {
            const li = document.createElement('li');
            li.textContent = `${pousada.nome} - ID: ${pousada.id}`;
            lista.appendChild(li);
        });
    });
}

function listarPousadasLivres() {
    fetch('/listar_pousadas_livres')
    .then(response => response.json())
    .then(data => {
        const lista = document.getElementById('lista_pousadas_livres');
        lista.innerHTML = '';
        data.forEach(pousada => {
            const li = document.createElement('li');
            li.textContent = `${pousada.nome} - ID: ${pousada.id}`;
            lista.appendChild(li);
        });
    });
}
