from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.auth.auth import auth_bp
from app.blueprints.employees import employees_blueprint as employee_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///factory.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(employee_bp, url_prefix='/api')

    return app
