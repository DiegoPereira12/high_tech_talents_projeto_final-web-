from flask import Flask,request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:diego@localhost:5432/imobiliaria_api"

app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class InquilinosModel(db.Model):
    __tablename__ = 'inquilinos'

    id = db.Column(db.Integer, autoincrement=True, primary_key = True)
    nome = db.Column(db.String())
    cpf = db.Column(db.String())
    data_nascimento = db.Column(db.String())

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome        
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    def __repr__(self):  
      return f"<Proprietário: id {self.id}, nome {self.nome}, cpf {self.cpf}, data de nascimento {self.data_nascimento}>"        

    @app.route('/')
    def index_inquilino():
        return render_template('index_inquilino.html', inquilinos = InquilinosModel.query.all())

    @app.route('/cadastro_inquilino')
    def cadastrar_inquilino():
        return render_template('cadastro_inquilino.html', inquilinos = InquilinosModel.query.all())
    
    @app.route('/cadastro_inquilino', methods = ['GET', 'POST'])
    def cadastro_inquilino():
        if request.method == 'POST':
            if not request.form['name'] or not request.form['cpf'] or not request.form['data_nascimento']:
                flash('Por favor, preencha todos os campos')
            else:
                inquilinos = InquilinosModel(request.form['name'], request.form['cpf'], request.form['data_nasciemnto'])

                db.session.add(inquilinos)
                db.session.commit()

                flash('Registro adicionado com sucesso')
                return redirect(url_for('casdastro_inquilino'))
        return render_template('index_inquilino.html')    

    @app.route('/')
    def lista_inquilino():
        return render_template('lista_inquilino.html', inquilinos = InquilinosModel.query.all())

    @app.route('/excluir_inquilino/<int:id>')
    def excluir_inquilino(id):
        inquilinos = InquilinosModel.query.filter_by(_id=id).first()
        db.session.delete(inquilinos)
        db.session.commit()
        inquilinos = InquilinosModel.query.all()

        return render_template('lista_inquilino.html', inquilinos = InquilinosModel.query())

    @app.route('/atualizar_inquilino/<int:id>', methods = ['GET', 'POST'])
    def atualizar_inquilino(id):
        inquilinos = InquilinosModel.query.filter_by(_id=id).first()

        if request.method == 'POST':
            if not request.form['name'] or not request.form['cpf'] or not request.form['data_nasciemnto']:
                flash('Por favor, preencha todos os campos')
            else:
                inquilinos = InquilinosModel(request.form['name'], request.form['cpf'], request.form['data_nasciemnto'])

                db.session.add(inquilinos)
                db.session.commit()

                flash('Registro adicionado com sucesso')
                return redirect(url_for('lista_inquilino'))
        return render_template('atualiza_inquilino.html')


class ImovelModel(db.Model):
    __tablename__ = 'imovel'

    id = db.Column(db.Integer, autoincrement=True, primary_key = True)
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
    
    def __repr__(self):
        return f'<Imóvel: id {self.id}, logradouro {self.logradouro}, cep {self.cep}, bairro {self.bairro}, cidade {self.cidade}, proprietario_id {self.proprietario_id})>'

    @app.route('/')
    def index_imovel():
        return render_template('index_imovel.html', imovel = ImovelModel.query.all())

    @app.route('/')
    def cadastrar_imovel():
        return render_template('cadastro_imovel.html', imovel = ImovelModel.query.all())

    @app.route('/cadastro_imovel', methods = ['GET', 'POST'])
    def cadastro_imovel():
        if request.method == 'POST':
            if not request.form['logradouro'] or not request.form['cep'] or not request.form['bairro'] or not request.form['cidade'] or not request.form['bairro'] or not request.form['proprietario_id']:
                flash('Por favor, preencha todos os campos')
            else:
                imovel = ImovelModel(request.form['logradouro'], request.form['cep'], request.form['bairro'], request.form['cidade'], request.form['bairro'], request.form['proprietario_id'])

                db.session.add(imovel)
                db.session.commit()

                flash('Registro adicionado com sucesso')
                return redirect(url_for('casdastro_imovel'))
        return render_template('index_imovel.html') 
               
    @app.route('/')
    def lista_imovel():
        return render_template('lista_imovel.html', imovel = ImovelModel.query.all())

    @app.route('/excluir_imovel/<int:id>')
    def excluir_imovel(id):
        imovel = ImovelModel.query.filter_by(_id=id).first()

        db.session.delete(imovel)
        db.session.commit()

        imovel = ImovelModel.query.all()

        return render_template('lista_imovel.html', imovel = ImovelModel.query.all())

    @app.route('/atualizar_imovel/<int:id>', methods=['GET', 'POST'])
    def atualizar_imovel(id):
        imovel = ImovelModel.query.filter_by(_id=id).first()

        if request.method == 'POST':
            if not request.form['logradouro'] or not request.form['cep'] or not request.form['bairro'] or not request.form['cidade'] or not request.form['bairro'] or not request.form['proprietario_id']:
                flash('Por favor, preencha todos os campos')
            else:
                imovel = ImovelModel(request.form['logradouro'], request.form['cep'], request.form['bairro'], request.form['cidade'], request.form['bairro'], request.form['proprietario_id'])

                db.session.add(imovel)
                db.session.commit()

                flash('Registro adicionado com sucesso')
                return redirect(url_for('lista_imovel'))
        return render_template('atualiza_imovel.html')


class ProprietarioModel(db.Model):
    __tablename__ = 'proprietario'

    id = db.Column(db.Integer, autoincrement=True, primary_key = True)
    nome = db.Column(db.String())
    cpf = db.Column(db.String())
    data_nascimento = db.Column(db.String())

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome        
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    
    def __repr__(self):  
      return f"<Proprietário: id {self.id}, nome {self.nome}, cpf {self.cpf}, data de nascimento {self.data_nascimento}>"

    @app.route('/')
    def index_proprietario():
        return render_template('index_proprietario.html', proprietario = ProprietarioModel.query.all())

    @app.route('/')
    def cadastrar_index_proprietario():
        return render_template('cadastro_proprietario.html', proprietario = ProprietarioModel.query.all()) 

    @app.route('/cadastro_proprietario', methods=['GET', 'POST'])
    def cadastro_proprietario():
        if request.method == 'POST':
            if not request.form['name'] or not request.form['cpf'] or not request.form['data_nasciemnto']:
                flash('Por favor, preencha todos os campos')
            else:
                inquilinos = ProprietarioModel(request.form['name'], request.form['cpf'], request.form['data_nasciemnto'])

                db.session.add(inquilinos)
                db.session.commit()

                flash('Registro adicionado com sucesso')
                return redirect(url_for('casdastro_proprietario'))
        return render_template('index_proprietario.html')

    @app.route('/')
    def lista_proprietario():
        return render_template('lista_proprietario.html', proprietario = ProprietarioModel)

    @app.route('/excluir_proprietario/<int:id>')
    def excluir_proprietario(id):
        proprietario = ProprietarioModel.query.filter_by(_id=id).first()

        db.session.delete(proprietario)
        db.session.commit()

        proprietario = ProprietarioModel.query.all()

        return render_template("lista_proprietario.html", proprietario = ProprietarioModel)

    @app.route('/atualizar_proprietario/<int:id>', methods=['GET', 'POST'])
    def atualizar_proprietario(id):
        proprietario = ProprietarioModel.query.filter_by(_id=id).first()

        if request.method == 'POST':
            if not request.form['name'] or not request.form['cpf'] or not request.form['data_nasciemnto']:
                flash('Por favor, preencha todos os campos')
            else:
                proprietario = ProprietarioModel(request.form['name'], request.form['cpf'], request.form['data_nasciemnto'])

                db.session.add(proprietario)
                db.session.commit()

                flash('Registro adicionado com sucesso')
                return redirect(url_for('lista_proprietario'))
        return render_template('atualiza_proprietario.html')


class AluguelModel(db.Model):
    __tablename__ = 'aluguel'

    id = db.Column(db.Integer,autoincrement=True, primary_key = True)
    id_imovel = db.Column(db.Integer) 
    id_inquilino = db.Column(db.Integer) 

    def __init__(self, id_imovel, id_inquilino):
        self.id_imovel = id_imovel
        self.id_inquilino = id_inquilino
    
    def __repr__(self):
      return f' <Aluguel: id {self.id}, id_imovel{self.id_imovel}, id_inquilino{self.inquilino_id}>'
    
    app.route('/')
    def index_aluguel():
        return render_template('index_aluguel.html', aluguel = AluguelModel.query.all())

    @app.route('/')
    def cadastrar_aluguel():
        return render_template('cadastro_aluguel.html', aluguel = AluguelModel.query.all())

    @app.route('/cadastro_aluguel', methods=['GET', 'POST'])
    def cadastro_aluguel():
        if request.method == 'POST':
            if not request.form['id_imovel'] or not request.form['id_inquilino']:
                flash('Por favor, preencha todos os campos')
            else:
                aluguel = AluguelModel(request.form['id_imovel'], request.form['id_inquilino'])

                db.session.add(aluguel)
                db.session.commit()

                return redirect(url_for('index_aluguel'))
        return render_template('index_aluguel.html')

    @app.route('/')
    def lista_aluguel():
        return render_template('lista_aluguel.html', aluguel = AluguelModel.query.all())

    @app.route('/excluir_aluguel/<int:id>')
    def excluir_aluguel(id):
        aluguel = AluguelModel.query.filter_by(_id=id).first()

        db.session.delete(aluguel)
        db.session.commit()

        aluguel = AluguelModel.query.all()

        return render_template('lista_aluguel.html', aluguel = AluguelModel.query.all())
        
    @app.route('/atualizar_aluguel/<int:id>', methods=['GET', 'POST'])
    def atualizar_aluguel(id):
        aluguel = AluguelModel.query.filter_by(_id=id).first()

        if request.method == 'POST':
            if not request.form['id_imovel'] or not request.form['id_inquilino']:
                flash('Por favor, preencha todos os campos')
            else:
                aluguel = AluguelModel(request.form['id_imovel'], request.form['id_inquilino'])

                db.session.add(aluguel)
                db.session.commit()

                flash('Registro adicionado com sucesso')
                return redirect(url_for('lista_aluguel'))
        return render_template('atualiza_aluguel.html')

if __name__ == '__main__':
    db.create_all() 
    app.run(debug=True)
  
