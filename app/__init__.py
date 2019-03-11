from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    from app import models

    # Blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app