from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração da conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

# Criar cursor para executar queries
cursor = db.cursor()

# 1) Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

    # 2) Rota para o formulário de criação de livro
    @app.route('/criar')
def pagina_criar():
    return render_template('criar.html')

# 3) Rota para criação de livro no banco de dados
    @app.route('/criar/novo', methods=['POST'])
def criar_livro():
    titulo = request.form['titulo']
    ano_publicacao = request.form['ano_publicacao']
    editora = request.form['editora']
    isbn = request.form['isbn']
    
    query = "INSERT INTO livro (titulo, ano_publicacao, editora, isbn) VALUES (%s, %s, %s, %s)"
    values = (titulo, ano_publicacao, editora, isbn)
    
    cursor.execute(query, values)
    db.commit()
    
    return redirect('/')

# Inicialização do servidor Flask
if __name__ == '__main__':
    app.run(debug=True)

    # 3) Rota para criação de livro no banco de dados
    @app.route('/criar/novo', methods=['POST'])
def criar_livro():
    titulo = request.form['titulo']
    ano_publicacao = request.form['ano_publicacao']
    editora = request.form['editora']
    isbn = request.form['isbn']
    
    query = "INSERT INTO livro (titulo, ano_publicacao, editora, isbn) VALUES (%s, %s, %s, %s)"
    values = (titulo, ano_publicacao, editora, isbn)
    
    cursor.execute(query, values)
    db.commit()
    
    return redirect(url_for('index'))


