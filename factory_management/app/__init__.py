from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'app.config.{config_name}')
    
    db.init_app(app)
    limiter.init_app(app)
