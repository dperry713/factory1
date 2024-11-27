# Factory Management System API

A robust Flask-based REST API for managing factory operations including employees, products, orders, customers and production tracking.

## Features

- Employee Management 
- Product Catalog
- Order Processing
- Customer Database
- Production Tracking
- Rate Limiting
- Pagination Support
- SQLite Database
- Blueprint Architecture

## Tech Stack

- Flask 2.2.2
- Flask-SQLAlchemy 3.0.0 
- Flask-Limiter 2.6.1
- Python-dotenv

## Installation

1. Clone the repository
2. Create virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
FLASK_ENV=development
FLASK_APP=run.py
FLASK_DEBUG=True
DATABASE_URL=sqlite:///factory.db
python run.py
The API will be available at http://localhost:5000

API Endpoints
Employees
GET /employees/ - List all employees
POST /employees/ - Create employee
Products
GET /products/ - List all products
POST /products/ - Create product
Orders
GET /orders/ - List all orders
GET /orders/<id>/ - Get order details
POST /orders/ - Create order
Customers
GET /customers/ - List all customers
GET /customers/<id>/ - Get customer details
POST /customers/ - Create customer
Production
GET /production/ - List production records
GET /production/<id>/ - Get production details
POST /production/ - Create production record