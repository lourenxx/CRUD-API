from db import db
from instance.instance import server
from models import DiscordMembers

# Função que cria as tabelas do banco e roda a aplicação

app = server.app

def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    create_tables()
    server.run()

