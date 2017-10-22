from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

__version__ = 'v0.3.0'
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Config.init_app(app)
    db.init_app(app)

    from .api_error import api as api_error_blueprint
    app.register_blueprint(api_error_blueprint)
    from .api_stable import api as api_stable_blueprint
    app.register_blueprint(api_stable_blueprint, url_prefix='/api/s')
    from .api_dev import api as api_dev_blueprint
    app.register_blueprint(api_dev_blueprint, url_prefix='/api/dev')

    return app