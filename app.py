from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota para a página principal (index.html)
@app.route('/')
def principal():
    return render_template('index.html')  # Renderiza o index.html

# Rota para a página "Sobre"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para a página "Galeria"
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# Rota para a página "Contato"
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        # Aqui você pode processar os dados do formulário (ex: enviar email, salvar no banco de dados, etc.)
        print(f"Nome: {nome}, Email: {email}, Mensagem: {mensagem}")
        return redirect(url_for('principal'))  # Redireciona para a página inicial após o envio
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)