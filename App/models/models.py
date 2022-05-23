from flask_sqlalchemy import SQLAlchemy
from app import db


class InquilinosModel(db.Model):
    __tablename__ = 'inquilino'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String())
    cpf = db.Column(db.String())
    data_nascimento = db.Column(db.String())

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome        
        self.cpf = cpf
        self.data_nascimento = data_nascimento   

class ImovelModel(db.Model):
    __tablename__ = 'imovel'

    id = db.Column(db.Integer, primary_key = True)
    logradouro = db.Column(db.String())
    cep = db.Column(db.String()) 
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())
    proprietario = db.Column(db.String())

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
    id_inquilino = db.Column(db.Integer(), db.ForeignKey('inquilino.id'), nullable=False)
    id_imovel = db.Column(db.Integer(), db.ForeignKey('imovel.id'), nullable=False)

    def __init__(self, id_inquilino, id_imovel):
        self.id_inquilino = id_inquilino
        self.id_imovel = id_imovel
        
        

