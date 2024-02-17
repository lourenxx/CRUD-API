from flask import Flask
from db import db
from routes import members_blueprint



app = Flask(__name__)
app.secret_key = "XXXXX"


# Configuração do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discord.db'  # Substitua pelo URI do seu banco de dados

# Inicialização do SQLAlchemy
db.init_app(app)

# Registre o blueprint
app.register_blueprint(members_blueprint, url_prefix='/')

def create_tables():
    with app.app_context():
        db.create_all()



if __name__ == '__main__':
    create_tables()
    app.run(debug=True)