document.getElementById('contacto-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const submitButton = this.querySelector('button[type="submit"]');
    submitButton.classList.add('loading');

    const formData = new FormData(this);

    fetch('/send_email', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        showFlashMessage('Pedido enviado correctamente. Lo contactaremos para su consulta.', 'success');
        this.reset();
        submitButton.classList.remove('loading');
    })
    .catch(error => {
        showFlashMessage('Ocurrió un error al enviar el pedido. Inténtalo de nuevo más tarde.', 'danger');
        console.error('Error:', error);
        submitButton.classList.remove('loading');
    });
});

function showFlashMessage(message, category) {
    const flashContainer = document.getElementById('mensajes-flash');
    const flashMessage = document.createElement('div');
    flashMessage.className = `alert ${category}`;
    flashMessage.textContent = message;

    flashContainer.appendChild(flashMessage);
    
    setTimeout(() => {
        flashMessage.remove();
    }, 5000);
}