from db import db
from instance.instace import server


app = server.app

def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    server.run()

