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
        if not request.form['id_imovel'] or not request.form['id_inquilino']:
            flash('Por favor preencha todos os campos')
        else:
            aluguel = AluguelModel(request.form['id_imovel'], request.form['id_inquilino'])

            db.session.add(aluguel)
            db.session.commit()

            return redirect(url_for('lista_aluguel'))

    return render_template('cadastro_aluguel.html', imovel=ImovelModel.query.all(), inquilino=InquilinosModel.query.all())

@app.route('/update_aluguel/<id>', methods=['GET', 'POST'])
def update_aluguel(id):

    aluguel = AluguelModel.query.filter_by(id=id).first()
    
    if request.method == 'GET':
         return render_template('update_aluguel.html', aluguel=aluguel)

    if request.method == 'POST':
        aluguel.id_imovel = request.form["id_imovel"]
        aluguel.id_inquilino = request.form["id_inquilino"]
                
        db.session.add(aluguel)
        db.session.commit()

        return redirect(url_for('lista_aluguel'))

@app.route('/delete_aluguel/<id>', methods=['GET', 'POST'])
def delete_aluguel(id):

    aluguel = AluguelModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('delete_aluguel.html', aluguel=aluguel)

    if request.method == 'POST':
        db.session.delete(aluguel)
        db.session.commit()

        return redirect(url_for('lista_aluguel'))



