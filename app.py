from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contato.db'
db = SQLAlchemy(app)

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seu_email@example.com'
app.config['MAIL_PASSWORD'] = 'sua_senha'
app.config['MAIL_DEFAULT_SENDER'] = 'seu_email@example.com'
mail = Mail(app)

# Modelo para os dados do formulário
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para lidar com o formulário de contato
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Obter dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Criar uma instância do modelo Contato
        novo_contato = Contato(nome=nome, email=email, mensagem=mensagem)

        # Adicionar e commitar os dados no banco de dados
        db.session.add(novo_contato)
        db.session.commit()

        # Enviar e-mail
        send_email(nome, email, mensagem)

        # Redirecionar de volta à página principal após o envio do formulário
        return redirect(url_for('index'))

# Função para enviar e-mail
def send_email(nome, email, mensagem):
    subject = 'Novo Formulário de Contato'
    body = f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}'

    message = Message(subject, recipients=['seu_destinatario@example.com'], body=body)
    mail.send(message)

if __name__ == '__main__':
    # Criação do banco de dados
    db.create_all()
    
    # Inicia o aplicativo em modo de depuração
    app.run(debug=True)
