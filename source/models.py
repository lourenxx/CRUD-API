from db import db

# Classe que cria o modelo das tabelas do banco

class DiscordMembers(db.Model):

    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=False)
    nickname = db.Column(db.String(80), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, nickname, age):
        self.name = name
        self.nickname = nickname
        self.age = age
    
# Função que transforma os atributos da classe em json

    def json(self):
        return {
            'id': self.id, 
            'name': self.name,
            'nickname': self.nickname,
            'age': self.age
        }