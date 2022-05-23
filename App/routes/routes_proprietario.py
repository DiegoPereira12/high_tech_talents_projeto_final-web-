from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *


@app.route('/menu_proprietario')
def menu_proprietario():

    return render_template('menu_proprietario.html')

@app.route('/lista_proprietario')
def lista_proprietario():

    return render_template('/lista_proprietario.html', proprietario = ProprietarioModel.query.all() )

@app.route('/cadastro_proprietario', methods = ['GET', 'POST'])
def cadastro_proprietario():

    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cpf'] or not request.form['data_nascimento']:
            flash('Por favor preencha todos os campos')
        else:
            proprietario = ProprietarioModel(request.form['nome'], request.form['cpf'], request.form['data_nascimento'])

            db.session.add(proprietario)
            db.session.commit()

            return redirect(url_for('lista_proprietario'))
    return render_template('cadastro_proprietario.html')

@app.route('/update_proprietario/<id>', methods=['GET', 'POST'])
def update_proprietario(id):

    proprietario = ProprietarioModel.query.filter_by(id=id).first()
    
    if request.method == 'GET':
         return render_template('update_proprietario.html', proprietario=proprietario)

    if request.method == 'POST':
        proprietario.nome = request.form["nome"]
        proprietario.cpf = request.form["cpf"]
        proprietario.data_nascimento = request.form["data_nascimento"]
        
        db.session.add(proprietario)
        db.session.commit()

        return redirect(url_for('lista_proprietario'))

@app.route('/delete_proprietario/<id>', methods=['GET', 'POST'])
def delete_proprietario(id):

    proprietario = ProprietarioModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('delete_proprietario.html', proprietario=proprietario)

    if request.method == 'POST':
        db.session.delete(proprietario)
        db.session.commit()

        return redirect(url_for('lista_proprietario'))