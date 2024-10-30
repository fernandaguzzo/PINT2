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
    const valor_pousada = document.getElementById('valor_pousada').value;

    fetch('/cadastrar_pousada', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'id_pousada': id_pousada,
            'nome': nome_pousada,
            'valor': valor_pousada,
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.message;
        // Limpar campos após o cadastro
        document.getElementById('id_pousada').value = '';
        document.getElementById('nome_pousada').value = '';
        document.getElementById('valor_pousada').value = '';
    })
    .catch(error => console.error('Erro:', error));
}

function reservarPousada() {
    const cpf_cnpj = document.getElementById('cpf_reserva').value;
    const pousada_id = document.getElementById('id_pousada_reserva').value;
    const data_fim = document.getElementById('data_fim_reserva').value;  // Data de término da reserva

    fetch('/reservar_pousada', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'cpf_cnpj': cpf_cnpj,
            'pousada_id': pousada_id,
            'data_fim': data_fim  // Envia a data de término
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.message;
        // Limpar campos após reserva
        document.getElementById('cpf_reserva').value = '';
        document.getElementById('id_pousada_reserva').value = '';
        document.getElementById('data_fim_reserva').value = '';
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
        lista.style.display = 'block';  // Exibe a lista
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
            li.textContent = `${pousada.nome} - ID: ${pousada.id} - Valor: R$${pousada.valor}`;  // Inclui o valor
            lista.appendChild(li);
        });
        lista.style.display = 'block';  // Exibe a lista
    });
}



function listarPousadasReservadas() {
    fetch('/listar_pousadas_reservadas')
    .then(response => response.json())
    .then(data => {
        const lista = document.getElementById('lista_pousadas_reservadas');
        lista.innerHTML = '';
        lista.style.display = 'block';

        data.forEach(pousada => {
            const li = document.createElement('li');
            const nomePousada = pousada.pousada_nome || 'Nome não disponível';
            const idPousada = pousada.pousada_id || 'ID não disponível';
            const dataInicio = pousada.data_inicio || 'Data de início não disponível';
            const dataFim = pousada.data_fim || 'Data de término não disponível';
            
            li.textContent = `${nomePousada} - ID: ${idPousada}, Início: ${dataInicio}, Término: ${dataFim}`;
            lista.appendChild(li);
        });
    })
    .catch(error => console.error('Erro ao listar pousadas reservadas:', error));
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
        lista.style.display = 'block';  // Exibe a lista
    });
}

function ocultarTabela(idTabela) {
    const lista = document.getElementById(idTabela);
    if (lista.style.display === 'none') {
        lista.style.display = 'block';  // Exibe a lista se estiver oculta
    } else {
        lista.style.display = 'none';   // Oculta a lista se estiver visível
    }
};

function formatCurrencyMachineInput(input) {
    let value = input.value.replace(/\D/g, ""); // Remove qualquer caractere não numérico
    value = (parseInt(value) / 100).toFixed(2); // Divide por 100 para adicionar a vírgula
    input.value = value.replace(".", ","); // Substitui ponto por vírgula para formato brasileiro
}
