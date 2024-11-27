# Factory Management System

A Flask-based REST API for managing factory operations including products, orders, customers, employees, and production tracking.

## Features

- User Authentication with JWT
- Role-based Access Control
- Rate Limiting Protection
- RESTful API Endpoints
- Database Models:
  - Users
  - Employees
  - Products
  - Orders
  - Customers
  - Production Records

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd factory_management
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
FLASK_ENV=development
FLASK_APP=run.py
FLASK_DEBUG=True
DATABASE_URL=sqlite:///factory.db
python run.py
The API will be available at http://localhost:5000

API Endpoints
Authentication
POST /auth/login - User login
POST /auth/register - User registration
Employees
GET /employees/ - List all employees
POST /employees/ - Create new employee
Products
GET /products/ - List all products
POST /products/ - Create new product
Orders
GET /orders/ - List all orders
POST /orders/ - Create new order
GET /orders/<id>/ - Get specific order
Customers
GET /customers/ - List all customers
POST /customers/ - Create new customer
GET /customers/<id>/ - Get specific customer
Production
GET /production/ - List production records
POST /production/ - Create production record
GET /production/<id>/ - Get specific production record
Security Features
JWT Authentication
Rate Limiting (5 requests per minute)
Password Hashing
Role-based Access Control
Database Schema
The system uses SQLAlchemy with SQLite database, featuring relationships between:

Products and Orders
Customers and Orders
Products and Production Records
Development
The application uses Flask development server with debug mode enabled in development environment.

Requirements
Python 3.7+
Flask 2.2.2
Flask-SQLAlchemy 3.0.0
Flask-Limiter 2.6.1
Additional dependencies in requirements.txt
