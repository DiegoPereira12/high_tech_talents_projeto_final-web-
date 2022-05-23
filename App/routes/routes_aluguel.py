from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *


@app.route('/menu_aluguel')
def menu_aluguel():

    return render_template('menu_aluguel.html')

@app.route('/lista_aluguel')
def lista_aluguel():

    return render_template('/lista_aluguel.html', aluguel = AluguelModel.query.all() )

@app.route('/cadastro_aluguel', methods = ['GET', 'POST'])
def cadastro_aluguel():

    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cpf'] or not request.form['data_nascimento']:
            flash('Por favor preencha todos os campos')
        else:
            aluguel = AluguelModel(request.form['nome'], request.form['cpf'], request.form['data_nascimento'])

            db.session.add(aluguel)
            db.session.commit()

            return redirect(url_for('lista_inquilino'))
    return render_template('cadastro_inquilino.html')
