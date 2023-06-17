from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class DatabaseConnection:
    def __init__(self, app):
        self.app = app

    def init_app(self):
        db.init_app(self.app)
        migrate.init_app(self.app, db)

    def create_api_key_table(self):
        with self.app.app_context():
            db.create_all()

    def insert_api_keys(self, api_keys):
        with self.app.app_context():
            for key in api_keys:
                api_key = ApiKey(key=key)
                db.session.add(api_key)
            db.session.commit()

    def verify_api_key(self, key):
        with self.app.app_context():
            api_key = ApiKey.query.filter_by(key=key).first()
            if api_key:
                return True
            return False


class ApiKey(db.Model):
    __tablename__ = 'api_keys'
    key = db.Column(db.String(100), primary_key=True)

    def __init__(self, key):
        self.key = key
