from db import db

# Classe que cria o modelo das tabelas do banco

class DiscordMembers(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    name = db.Collumn(db.String(80), nullable=False, unique=False)
    nickname = db.Collumn(db.String(80), nullable=False, unique=True)
    age = db.Collumn(db.Integer(80), nullable=False)

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

