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
    
    def __repr__(self):
      return f"<Inquilinos {self.nome}>"