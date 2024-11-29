from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configure the Flask application
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///factory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    return app

