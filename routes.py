from flask import Blueprint, jsonify
from models import DiscordMembers


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