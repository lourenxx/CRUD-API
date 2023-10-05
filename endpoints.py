from flask import Flask, request, jsonify
from models import DiscordMembers
from app import app
from db import db

#Endpoint da aplicação

# GET ALL

@app.route("/members", methods=["GET"])
def get_member():
    member_get = DiscordMembers.query.all()
    member_get_json = [member.json() for member in member_get]

    return jsonify(member_get_json)


# GET BY ID

@app.route("/members/<id>", methods=["GET"])
def get_member_id(id):
    member_id = DiscordMembers.query.filter_by(id=id).first()
    member_id_json = [id.json() for id in member_id]

    return jsonify(member_id_json)

# POST

@app.route("/create", methods=["POST"])
def post_member():
    body = request.get_json()

# VALIDATING THE PARAMETERS

    try:
        member = DiscordMembers(name=body["name"], nickname=body["nickname"], age=body["age"])
        db.session.add(member)
        db.session.commit()
        return jsonify(201, "member", member.to_json(), "Succesfully created!")
    
    except Exception as e:
        print(e)
        return jsonify(400, "member", {}, "Register error!")

    
