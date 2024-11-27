import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import HTTPException

# Initialize extensions
db = SQLAlchemy()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def register_blueprints(app):
    from app.blueprints.employees import employees_blueprint
    from app.blueprints.products import products_blueprint
    from app.blueprints.orders import orders_blueprint
    from app.blueprints.customers import customers_blueprint
    from app.blueprints.production import production_blueprint

    app.register_blueprint(employees_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(orders_blueprint)
    app.register_blueprint(customers_blueprint)
    app.register_blueprint(production_blueprint)

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Set database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///factory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    limiter.init_app(app)
    
    # Register blueprints
    register_blueprints(app)
    
    return app
