# app.py
from flask import Flask, render_template, request, redirect, Session, g
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'authentication.log_in_user'
login_manager.session_protection = 'strong'

def create_app():
    # app
    app = Flask(__name__, instance_relative_config=True)
    # Load the config variables
    app.config.from_object('config.BaseConfig')
    #configuration = os.path.join(os.getcwd(), 'config', config_type + ".py")
    #app.config.from_pyfile(configuration)
    with app.app_context():
        db.init_app(app)
        bootstrap.init_app(app)
        login_manager.init_app(app)
        bcrypt.init_app(app)

        from app.module1 import bp
        app.register_blueprint(bp)

        return app



# @app.route('/')
# def index():
#     return "Basic setup!"