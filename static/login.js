// ------------------------------------------------
//            Manipulação do Formulário de Login
// ------------------------------------------------
// Este script intercepta o envio do formulário, envia os dados para o backend,
// e exibe um modal caso ocorra algum erro.

// Selecionando o formulário de login e adicionando um evento ao enviá-lo
document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Evita o envio padrão do formulário para podermos tratar as respostas
    event.preventDefault();

    // Coleta os dados do formulário
    const formData = new FormData(this);

    // Fazendo a requisição ao backend usando Fetch API
    fetch('/login', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            // Caso haja uma mensagem de erro, mostra o modal de erro
            showErrorModal(data.message);
        } else {
            // Se o login for bem-sucedido, redireciona o usuário
            window.location.href = '/index';
        }
    })
    .catch(error => {
        // Tratando o caso de falhas na requisição
        showErrorModal('Ocorreu um erro ao processar sua solicitação. Tente novamente.');
    });
});

// ------------------------------------------------
//            Função para Mostrar o Modal de Erro
// ------------------------------------------------
// Esta função mostra o modal de erro e permite ao usuário fechá-lo.
function showErrorModal(message) {
    // Seleciona o modal e a área da mensagem de erro
    const modal = document.getElementById('errorModal');
    const errorMessage = document.getElementById('errorMessage');

    // Define o texto da mensagem de erro
    errorMessage.textContent = message;

    // Exibe o modal
    modal.style.display = 'block';

    // Seleciona o botão de fechar no modal
    const closeButton = document.querySelector('.close-button');

    // Define o evento para fechar o modal ao clicar no botão de fechar
    closeButton.onclick = function() {
        modal.style.display = 'none';
    }

    // Define o evento para fechar o modal ao clicar fora da área do modal
    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }
}
