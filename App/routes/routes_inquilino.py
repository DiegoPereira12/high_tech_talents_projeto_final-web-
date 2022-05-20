from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *


@app.route('/')
def main():

    return render_template('main.html')

@app.route('/menu_inquilino')
def menu_inquilino():

    return render_template('menu_inquilino.html')

@app.route('/lista_inquilino')
def lista_inquilino():

    return render_template('/lista_inquilino.html', inquilino = InquilinosModel.query.all() )

@app.route('/cadastro_inquilino', methods = ['GET', 'POST'])
def cadastro_inquilino():

    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cpf'] or not request.form['data_nascimento']:
            flash('Por favor preencha todos os campos')
        else:
            inquilino = InquilinosModel(request.form['nome'], request.form['cpf'], request.form['data_nascimento'])

            db.session.add(inquilino)
            db.session.commit()

            return redirect(url_for('lista_inquilino'))
    return render_template('cadastro_inquilino.html')

@app.route('/update_inquilino/<id>', methods=['GET', 'POST'])
def update_inquilino(id):

    inquilino = InquilinosModel.query.filter_by(id=id).first()
    
    if request.method == 'GET':
         return render_template('update_inquilino.html', inquilino=inquilino)

    if request.method == 'POST':
        inquilino.nome = request.form["nome"]
        inquilino.cpf = request.form["cpf"]
        inquilino.data_nascimento = request.form["data_nascimento"]
        
        db.session.add(inquilino)
        db.session.commit()

        return redirect(url_for('lista_inquilino'))

@app.route('/delete_inquilino/<id>', methods=['GET', 'POST'])
def delete_inquilino(id):

    inquilino = InquilinosModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('delete_inquilino.html', inquilino=inquilino)

    if request.method == 'POST':
        db.session.delete(inquilino)
        db.session.commit()

        return redirect(url_for('lista_inquilino'))

   