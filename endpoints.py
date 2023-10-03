from flask import Flask, request, jsonify
from models import DiscordMembers
from app import app


# GET ALL

@app.route("/members", methods=["GET"])
def get_member():
    member_get = DiscordMembers.query.all()
    member_get_json = [member.json() for member in member_get]

    return jsonify(member_get_json)


@app.route("members/<id>")
def get_member_id(id):
    member_id = DiscordMembers.query.filter_by(id=id).first()
    member_id_json = [id.json() for id in member_id]

    return jsonify(member_id_json)
