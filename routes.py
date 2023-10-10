from flask import Blueprint, jsonify, request
from models import DiscordMembers
from db import db


members_blueprint = Blueprint('members', __name__)

# Rota para listar todos os membros
@members_blueprint.route('/members', methods=['GET'])
def get_members():
    try:
        members = DiscordMembers.query.all()
        member_list = [member.json() for member in members]
        return jsonify({'members': member_list}), 200
    except Exception as e:
        return jsonify({'message': 'Erro ao buscar membros'}), 500
    
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
