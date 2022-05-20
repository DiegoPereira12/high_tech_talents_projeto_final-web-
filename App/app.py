from operator import imod
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:diego@localhost:5432/diego_imobiliaria"
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from routes.routes_inquilino import *
from routes.routes_imovel import * 

if __name__ == '__main__':
   app.run(debug=True)          
