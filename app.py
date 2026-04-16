from flask import Flask,render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/ola')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/usuario', defaults={"nome": "Desconhecido","sobrenome": "Desconhecido"})
@app.route('/usuario/<nome>/<sobrenome>')
def usuario(nome, sobrenome):
    info={"nome":nome, "sobrenome":sobrenome}
    return render_template('usuario.html', info=info)

@app.route('/semestre/<int:x>')
def semestre(x):
    dados={}
    dados["atual"]= x
    dados["anterior"]= x - 1
    return render_template('semestre.html', dados=dados)

@app.route('/curriculo')

@app.route('/disciplinas')

@app.route('/contato')
def contato():
    dados={"nome":'Evellyn', "email":'evellyn.s@escolar.ifrn.edu.br'}
    return render_template('contato.html', dados=dados)

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['GET', 'POST'])
def recebedados():
    nome = request.form['nome'] 
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    datanasc = request.form['datanasc']
    data_obj = datetime.strptime(datanasc, "%Y-%m-%d")
    data_formatada = data_obj.strftime("%d-%m-%Y")
    estado = request.form.get('estado')
    escola = request.form.get('escola')
    modalidade = request.form.getlist('modalidade')
    # info = request.args

    return render_template('recebedados.html', nome = nome, sobrenome = sobrenome, email = email, data_formatada = data_formatada, estado = estado, escola = escola, modalidade = modalidade)
    # return render_template('recebedados.html', info=info) #opcao p muitos dados
@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/recebecompras', methods=['POST'])
def recebecompras():
    itens = request.form.getlist('itens')
    return render_template('lista.html', itens = itens)

if __name__ == "__main__":
    app.run()
