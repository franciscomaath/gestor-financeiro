from flask import Flask
from config import Config
from .extensions import db, migrate, cors
from .api.categorias import categorias_bp
from .api.transacoes import transacoes_bp

def create_app(config_class = Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    app.register_blueprint(categorias_bp, url_prefix = '/api')
    app.register_blueprint(transacoes_bp, url_prefix = '/api')

    return app