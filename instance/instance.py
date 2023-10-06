from flask import Flask


    # Classe que instancia a aplicação e o banco de dados

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discord.db'

    def run(self):
        self.app.run(
            port=5000, 
            debug=True, 
            host='0.0.0.0')

server = Server()