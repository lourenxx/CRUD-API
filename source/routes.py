from flask import Blueprint, jsonify, request, render_template, flash, redirect, url_for
from models import DiscordMembers
from db import db


members_blueprint = Blueprint('members', __name__)  

# Rota para listar todos os membros
@members_blueprint.route('/', methods=['GET'])
def get_member():
    members = DiscordMembers.query.all()
    return render_template("index.html", members=members)
    

# Rota pra criar os membros
@members_blueprint.route('/create')
def render_form():
     return render_template("new.html") 


@members_blueprint.route('/create', methods=["POST"])
def post_member():
    name = request.form['name']
    nickname = request.form['nickname']
    age = request.form['age']

    member = DiscordMembers.query.filter_by(nickname=nickname).first()

    if member:
         flash("Membro ja existente!")
         return redirect(url_for('members.get_member'))
    
    new_member = DiscordMembers(name=name, nickname=nickname, age=age)
    db.session.add(new_member)
    db.session.commit()

    flash("Membro adicionado com sucesso!")
    return redirect(url_for('members.get_member'))



# Rota para atualizar membros
@members_blueprint.route('/update/<int:id>')
def render_update(id):
    member = DiscordMembers.query.filter_by(id=id).first()
    return render_template("update.html", member=member)


@members_blueprint.route('/update/<int:id>', methods=['PUT', 'POST'])

def update_member(id):

    member = DiscordMembers.query.get(id)
    member.name = request.form.get('name', member.name)
    member.nickname = request.form.get('nickname', member.nickname)
    member.age = request.form.get('age', member.age)

    db.session.add(member)
    db.session.commit()

    flash("Membro atualizado com sucesso!")
    return redirect(url_for('members.get_member'))


# Rota para deletar membros
@members_blueprint.route('/delete/<int:id>', methods=['DELETE', 'POST'])
def delete_member(id):
     
    DiscordMembers.query.filter_by(id=id).delete()
    db.session.commit()

    flash("Membro deletado com sucesso!")
    return redirect(url_for('members.get_member'))


            





