from flask import Blueprint, jsonify, request, render_template
from models import DiscordMembers
from db import db


members_blueprint = Blueprint('members', __name__)  

# Rota para listar todos os membros
@members_blueprint.route('/members', methods=['GET'])
def get_member():
    members = DiscordMembers.query.all()
    return render_template("members.html", members=members)
    
    

# Rota para listar membros por id 
@members_blueprint.route('/members/<id>', methods=['GET'])
def get_member_by_id(id):
    try:
        member_id = DiscordMembers.query.filter_by(id=id).first()
        member_id_list = member_id.json()
        return jsonify({'member': member_id_list}), 200
    except Exception as e:
        return jsonify({'message': 'Erro ao buscar membro por id'}), 500
    

# Rota pra criar os membros  
@members_blueprint.route('members', methods=["POST"])
def post_member():
    try:
        data = request.get_json()
        new_member = DiscordMembers(name=data['name'], nickname=data['nickname'], age=data['age'])
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Membro criado com sucesso', 'member': new_member.json()}), 201
    except Exception as e:
        return jsonify({'message': 'Erro ao criar membro'}), 500
    

# Rota para atualizar membros
@members_blueprint.route('/update/<int:id>', methods=['PUT'])
def uptade_member(id):
    try:
        data = request.get_json()
        member = DiscordMembers.query.get(id)

        if member:
            member.name = data.get('name', member.name)
            member.nickname = data.get('nickname', member.nickname)
            member.age = data.get('age', member.age)

            db.session.commit()

            return jsonify({'message': 'Membro atualizado com sucesso', 'member': member.json()}), 200
        else:
                return jsonify({'message': 'Membro não encontrado'}), 404
        
    except Exception as e:
            return jsonify({'message': 'Erro ao atualizar membro'}), 500
            

# Rota para deletar membros
@members_blueprint.route('/delete/<int:id>', methods=['DELETE'])
def delete_member(id):
     
     try:
        member = DiscordMembers.query.get(id)

        if member:
            db.session.delete(member)
            db.session.commit()
            return jsonify({'message' : f' Membro excluido {member} com sucesso'}), 204
        else:
            return jsonify({'message' : f' Membro não encontrado'}), 404
        
     except Exception as e:
         return jsonify({'message' : 'Erro ao excluir membro'}), 500


            





