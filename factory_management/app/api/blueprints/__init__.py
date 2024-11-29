from flask import Flask
from app.models import db
from app.blueprints.customers import customers_blueprint
from app.blueprints.employees import employees_blueprint
from app.blueprints.orders import orders_blueprint
from app.blueprints.production import production_blueprint
from app.blueprints.products import products_blueprint
from app.blueprints.analytics import analytics_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///factory_management.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(customers_blueprint)
    app.register_blueprint(employees_blueprint)
    app.register_blueprint(orders_blueprint)
    app.register_blueprint(production_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(analytics_blueprint)  # Register the new analytics blueprint

    return app
