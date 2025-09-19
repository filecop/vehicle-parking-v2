from flask import Flask
from .config import DevConfig, ProdConfig, TestConfig
import os
from .db import db, migrate
from . import models
from .blueprints.web import web_bp
from .blueprints.api import api_bp

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

def create_app(config_setting:str | None = None):
    app = Flask(__name__)
    config_setting = (config_setting or os.getenv("FLASK_CONFIG","development")).lower()
    mapping = {"development":DevConfig, "prod":ProdConfig, "test":TestConfig}
    app.config.from_object(mapping[config_setting])

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
