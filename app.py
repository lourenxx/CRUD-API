from flask import Flask
from db import db
from routes import members_blueprint



app = Flask(__name__)


# Configuração do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discord.db'  # Substitua pelo URI do seu banco de dados

# Inicialização do SQLAlchemy
db.init_app(app)

# Registre o blueprint
app.register_blueprint(members_blueprint, url_prefix='/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)