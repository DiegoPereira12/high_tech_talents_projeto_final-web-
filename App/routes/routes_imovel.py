from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.models import *


@app.route('/menu_imovel')
def menu_imovel():

    return render_template('menu_imovel.html')

@app.route('/lista_imovel')
def lista_imovel():

    return render_template('/lista_imovel.html', imovel = ImovelModel.query.all() )

@app.route('/cadastro_imovel', methods = ['GET', 'POST'])
def cadastro_imovel():

    if request.method == 'POST':
        if not request.form['logradouro'] or not request.form['cep'] or not request.form['bairro'] or not request.form['cidade'] or not request.form['proprietario']:
            flash('Por favor preencha todos os campos')
        else:
            imovel = ImovelModel(request.form['logradouro'], request.form['cep'], request.form['bairro'], request.form['cidade'], request.form['proprietario'])

            db.session.add(imovel)
            db.session.commit()

            return redirect(url_for('lista_imovel'))
    return render_template('cadastro_imovel.html')

@app.route('/update_imovel/<id>', methods=['GET', 'POST'])
def update_imovel(id):

    imovel = ImovelModel.query.filter_by(id=id).first()
    
    if request.method == 'GET':
         return render_template('update_imovel.html', imovel=imovel)

    if request.method == 'POST':
        imovel.logradouro = request.form["logradouro"]
        imovel.cep = request.form["cep"]
        imovel.bairro = request.form["bairro"]
        imovel.cidade = request.form["cidade"]
        imovel.proprietario = request.form["proprietario"]
        
        db.session.add(imovel)
        db.session.commit()

        return redirect(url_for('lista_imovel'))

@app.route('/delete_imovel/<id>', methods=['GET', 'POST'])
def delete_imovel(id):

    imovel = ImovelModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('delete_imovel.html', imovel=imovel)

    if request.method == 'POST':
        db.session.delete(imovel)
        db.session.commit()

        return redirect(url_for('lista_imovel'))