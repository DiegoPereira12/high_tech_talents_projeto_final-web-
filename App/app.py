from flask import Flask,request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:diego@localhost:5432/imobiliaria_api"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class InquilinosModel(db.Model):
    __tablename__ = 'inquilinos'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    cpf = db.Column(db.String())
    data_nascimento = db.Column(db.String())

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome        
        self.cpf = cpf
        self.data_nascimento = data_nascimento                         

app.route("/")
def index_inquilinos():
    return render_template("index_inquilino.html")

app.route("/cadastrar_inquilino")
def cadastrar_inquilino():
    return render_template("cadastro_inquilino.html")

@app.route("/cadastro_inquilino", methods=['GET', 'POST'])
def cadastro_inquilino():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        data_nascimento= request.form.get("data_nascimento")

        if nome and cpf and data_nascimento:
            inq = InquilinosModel(nome, cpf, data_nascimento)
            db.session.add(inq)
            db.session.commit()
    
    return redirect(url_for("index_inquilino"))

@app.route("/lista_inquilino")
def lista_inquilino():
    inq = InquilinosModel.query.all()
    return render_template("lista_inquilino.html", inq=inq)


@app.route("/excluir/<int:id>")
def excluir_inquilino(id):
    inq = InquilinosModel.query.filter_by(_id=id).first()

    db.session.delete(inq)
    db.session.commit()

    inq = InquilinosModel.query.all()

    return render_template("lista_inquilinos.html", inq=inq)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar_inquilinos(id):
    inq = InquilinosModel.query.filter_by(_id=id).first()

    if request.method == 'POST':
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        data_nascimento= request.form.get("data_nascimento")

        if nome and cpf and data_nascimento:
            inq = InquilinosModel(nome, cpf, data_nascimento)
            db.session.add(inq)
            db.session.commit()

            db.session.commit()

            return redirect(url_for("lista_inquilino"))

    return render_template("atualiza_inquilino.html", inq=inq)




class ImovelModel(db.Model):
    __tablename__ = 'imovel'

    id = db.Column(db.Integer, primary_key = True)
    logradouro = db.Column(db.String())
    cep = db.Column(db.String())
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())
    proprietario_id = db.Column(db.Integer)

    def __init__(self, logradouro, cep, bairro, cidade, proprietario):
        self.logradouro = logradouro
        self.cep = cep       
        self.bairro = bairro
        self.cidade = cidade
        self.proprietario = proprietario
        


class ProprietarioModel(db.Model):
    __tablename__ = 'proprietario'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    cpf = db.Column(db.String())
    data_nascimento = db.Column(db.String())

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome        
        self.cpf = cpf
        self.data_nascimento = data_nascimento 



class AluguelModel(db.Model):
    __tablename__ = 'aluguel'

    id = db.Column(db.Integer, primary_key = True)
    id_imovel = db.Column(db.Integer) 
    id_inquilino = db.Column(db.Integer) 

    def __init__(self, id_imovel, id_inquilino):
        self.id_imovel = id_imovel
        self.id_inquilino = id_inquilino
    


if __name__ == '__main__':
    app.run(debug=True) 

