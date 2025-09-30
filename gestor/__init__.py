from flask import Flask
from config import Config
from .extensions import db, migrate, cors

def create_app(config_class = Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    return app