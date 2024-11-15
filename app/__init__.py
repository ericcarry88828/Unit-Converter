from flask import Flask

from config import DevelopmentConfig, ProductionConfig

import os


def create_app():
    app = Flask(__name__)
    app.config

    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    from app import length, weight, temperature
    app.register_blueprint(length.bp)
    app.register_blueprint(weight.bp)
    app.register_blueprint(temperature.bp)

    return app
