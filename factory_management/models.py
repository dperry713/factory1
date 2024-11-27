from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

# Initialize SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Store hashed passwords
    role = db.Column(db.String(50), nullable=False)  # e.g., 'admin' or 'user'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "position": self.position}

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Relationships
    orders = db.relationship('Order', back_populates='product', lazy='dynamic')
    productions = db.relationship('Production', back_populates='product', lazy='dynamic')

    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "price": self.price
        }

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    # Relationships
    customer = db.relationship('Customer', back_populates='orders')
    product = db.relationship('Product', back_populates='orders')

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price,
        }

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)

    # Relationships
    orders = db.relationship('Order', back_populates='customer', lazy='dynamic')

    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "email": self.email, 
            "phone": self.phone
        }

class Production(db.Model):
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity_produced = db.Column(db.Integer, nullable=False)
    date_produced = db.Column(db.Date, nullable=False, default=date.today)

    # Relationships
    product = db.relationship('Product', back_populates='productions')

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity_produced": self.quantity_produced,
            "date_produced": self.date_produced.isoformat(),
        }

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_management.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a real secret key
    
    # Initialize extensions
    db.init_app(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

# Example of how to use the models
def setup_sample_data():
    app = create_app()
    with app.app_context():
        # Create a sample user
        admin_user = User(username='admin', role='admin')
        admin_user.set_password('admin_password')
        db.session.add(admin_user)
        
        # Create a sample customer
        customer = Customer(name='John Doe', email='john@example.com', phone='123-456-7890')
        db.session.add(customer)
        
        # Create a sample product
        product = Product(name='Sample Product', price=19.99)
        db.session.add(product)
        
        # Create a sample order
        order = Order(
            customer_id=customer.id, 
            product_id=product.id, 
            quantity=2, 
            total_price=39.98
        )
        db.session.add(order)
        
        # Create a sample production record
        production = Production(
            product_id=product.id, 
            quantity_produced=100, 
            date_produced=date.today()
        )
        db.session.add(production)
        
        # Commit the changes
        db.session.commit()

# Uncomment the following line to create sample data when the script is run
# if __name__ == '__main__':
#     setup_sample_data()