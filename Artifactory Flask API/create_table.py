from app import app
from model import db, ArtifactLog


def create_table():

    with app.app_context():
        try:
            db.create_all()
        except:
            print('Database table creation failed')
        