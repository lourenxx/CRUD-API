from flask import Flask

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHMEY_TRACK_MODIFICATIONS'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

    def run(self):
        self.app.run(
            port=5000, 
            debug=True, 
            host='0.0.0.0')

server = Server()
 