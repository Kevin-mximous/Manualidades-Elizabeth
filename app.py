from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY', '1200')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        pedido = request.form['pedido']

        # Enviar el mensaje
        msg = Message('Nuevo mensaje de contacto',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        
        msg.body = f"Nombre: {nombre}\nCorreo: {correo}\nTeléfono: {telefono}\nPedido: {pedido}"

        # Enviar el mensaje
        mail.send(msg)
        
        flash("Pedido enviado correctamente. Lo contactaremos para su consulta.", "success")
        
    except Exception as e:
        print(f"Error: {e}")
        flash("Ocurrió un error al enviar el pedido. Inténtalo de nuevo más tarde.", "danger")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
