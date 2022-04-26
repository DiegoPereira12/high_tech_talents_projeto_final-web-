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

    #def __repr__(self):
    #    return f"<InquilinosModel {self.id}: {self.nome}, nascida(o) em {self.data_de_nascimento}.>"                 

    app.route("/")
    def index_inquilino():
        return render_template("index_inquilino.html")

    app.route("/cadastrar_inquilino")
    def cadastrar_inquilino():
        return render_template("cadastro_inquilino.html")

    @app.route("/cadastro_inquilino", methods=['GET', 'POST'])
    def cadastro_inquilino():
        if request.method == "POST":
            nome = request.form.get("nome")
            cpf = request.form.get("cpf")
            data_nascimento = request.form.get("data_nascimento")

            if nome and cpf and data_nascimento:
                inq = InquilinosModel(nome, cpf, data_nascimento)
                db.session.add(inq)
                db.session.commit()
        
        return redirect(url_for("index_inquilino"))

    @app.route("/lista_inquilino")
    def lista_inquilino():
        inq = InquilinosModel.query.all()
        return render_template("lista_inquilino.html", inq=inq)


    @app.route("/excluir_inquilino/<int:id>")
    def excluir_inquilino(id):
        inq = InquilinosModel.query.filter_by(_id=id).first()

        db.session.delete(inq)
        db.session.commit()

        inq = InquilinosModel.query.all()

        return render_template("lista_inquilinos.html", inq=inq)

    @app.route("/atualizar_inquilino/<int:id>", methods=['GET', 'POST'])
    def atualizar_inquilino(id):
        inq = InquilinosModel.query.filter_by(_id=id).first()

        if request.method == 'POST':
            nome = request.form.get("nome")
            cpf = request.form.get("cpf")
            data_nascimento= request.form.get("data_nascimento")

            if nome and cpf and data_nascimento:
                inq = InquilinosModel(nome, cpf, data_nascimento)
                db.session.add(inq)
                db.session.commit()

                return redirect(url_for("lista_inquilino"))

        return render_template("atualiza_inquilino.html", inq=inq)


############################################################################

class ImovelModel(db.Model):
    __tablename__ = 'imovel'

    id = db.Column(db.Integer, primary_key = True)
    logradouro = db.Column(db.String())
    cep = db.Column(db.String())
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())
    proprietario_id = db.Column(db.Integer)

    def __init__(self, logradouro, cep, bairro, cidade, proprietario_id):
        self.logradouro = logradouro
        self.cep = cep       
        self.bairro = bairro
        self.cidade = cidade
        self.proprietario_id = proprietario_id

    app.route("/")
    def index_imovel():
        return render_template("index_imovel.html")

    app.route("/cadastrar_imovel")
    def cadastrar_imovel():
        return render_template("cadastro_imovel.html")

    @app.route("/cadastro_imovel", methods=['GET', 'POST'])
    def cadastro_imovel():
        if request.method == "POST":
            logradouro = request.form.get("logradouro")
            cep = request.form.get("cep")
            bairro = request.form.get("bairro")
            cidade = request.form.get("cidade")
            proprietario_id = request.form.get("proprietario_id")
            
            if logradouro and cep and bairro and cidade and proprietario_id:
                imov = ImovelModel(logradouro, cep, bairro, cidade, proprietario_id)
                db.session.add(imov)
                db.session.commit()
        
        return redirect(url_for("index_imovel"))
  
    @app.route("/lista_imovel")
    def lista_imovel():
        imov = ImovelModel.query.all()
        return render_template("lista_imovel.html", imov=imov)

    @app.route("/excluir_imovel/<int:id>")
    def excluir_imovel(id):
        imov = ImovelModel.query.filter_by(_id=id).first()

        db.session.delete(imov)
        db.session.commit()

        imov = ImovelModel.query.all()

        return render_template("lista_imovel.html", imov=imov)

    @app.route("/atualizar_imovel/<int:id>", methods=['GET', 'POST'])
    def atualizar_imovel(id):
        imov = ImovelModel.query.filter_by(_id=id).first()

        if request.method == "POST":
            logradouro = request.form.get("logradouro")
            cep = request.form.get("cep")
            bairro = request.form.get("bairro")
            cidade = request.form.get("cidade")
            proprietario_id = request.form.get("proprietario_id")
            
            if logradouro and cep and bairro and cidade and proprietario_id:
                imov = ImovelModel(logradouro, cep, bairro, cidade, proprietario_id)
                db.session.add(imov)
                db.session.commit()

                return redirect(url_for("lista_imovel"))

        return render_template("atualiza_imovel.html", imov=imov)


#####################################################################################
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

    app.route("/")
    def index_proprietario():
        return render_template("index_proprietario.html")

    app.route("/cadastrar_proprietario")
    def cadastrar_index_proprietario():
        return render_template("cadastro_proprietario.html") 

    @app.route("/cadastro_proprietario", methods=['GET', 'POST'])
    def cadastro_proprietario():
        if request.method == "POST":
            nome = request.form.get("nome")
            cpf = request.form.get("cpf")
            data_nascimento = request.form.get("data_nascimento")

            if nome and cpf and data_nascimento:
                inq = ProprietarioModel(nome, cpf, data_nascimento)
                db.session.add(inq)
                db.session.commit()
        
        return redirect(url_for("index_proprietario"))

    @app.route("/lista_proprietario")
    def lista_proprietario():
        prop = ProprietarioModel.query.all()
        return render_template("lista_proprietario.html", prop=prop)

    @app.route("/excluir_proprietario/<int:id>")
    def excluir_proprietario(id):
        prop = ProprietarioModel.query.filter_by(_id=id).first()

        db.session.delete(prop)
        db.session.commit()

        prop = ProprietarioModel.query.all()

        return render_template("lista_proprietario.html", prop=prop)

    @app.route("/atualizar_proprietario/<int:id>", methods=['GET', 'POST'])
    def atualizar_proprietario(id):
        inq = ProprietarioModel.query.filter_by(_id=id).first()

        if request.method == 'POST':
            nome = request.form.get("nome")
            cpf = request.form.get("cpf")
            data_nascimento= request.form.get("data_nascimento")

            if nome and cpf and data_nascimento:
                prop = ProprietarioModel(nome, cpf, data_nascimento)
                db.session.add(prop)
                db.session.commit()

                return redirect(url_for("lista_proprietario"))

        return render_template("atualiza_proprietario.html", prop=prop)


##########################################################################
class AluguelModel(db.Model):
    __tablename__ = 'aluguel'

    id = db.Column(db.Integer, primary_key = True)
    id_imovel = db.Column(db.Integer) 
    id_inquilino = db.Column(db.Integer) 

    def __init__(self, id_imovel, id_inquilino):
        self.id_imovel = id_imovel
        self.id_inquilino = id_inquilino
    
    app.route("/")
    def index_aluguel():
        return render_template("index_aluguel.html")

    app.route("/cadastrar_aluguel")
    def cadastrar_aluguel():
        return render_template("cadastro_aluguel.html")

    @app.route("/cadastro_aluguel", methods=['GET', 'POST'])
    def cadastro_aluguel():
        if request.method == "POST":
            id_imovel = request.form.get("id_imovel")
            id_inquilino = request.form.get("id_inquilino")

            if id_imovel and id_inquilino:
                alug = AluguelModel(id_imovel, id_inquilino)
                db.session.add(alug)
                db.session.commit()
        
        return redirect(url_for("index_aluguel"))
    
    @app.route("/lista_aluguel")
    def lista_aluguel():
        alug = AluguelModel.query.all()
        return render_template("lista_aluguel.html", alug=alug)

    @app.route("/excluir_aluguel/<int:id>")
    def excluir_aluguel(id):
        alug = AluguelModel.query.filter_by(_id=id).first()

        db.session.delete(alug)
        db.session.commit()

        alug = AluguelModel.query.all()

        return render_template("lista_aluguel.html", alug=alug)

if __name__ == '__main__':
    app.run(debug=True) 

