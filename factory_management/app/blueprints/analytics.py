from flask import Blueprint, jsonify
from app.models import db

analytics_blueprint = Blueprint('analytics', __name__, url_prefix='/analytics')

# Task 1: Analyze Employee Performance
@analytics_blueprint.route('/employee-performance', methods=['GET'])
def analyze_employee_performance():
    query = """
        SELECT 
            e.name AS employee_name,
            SUM(p.quantity_produced) AS total_quantity_produced
        FROM 
            employees e
        JOIN 
            production p ON e.id = p.employee_id
        GROUP BY 
            e.name;
    """
    results = db.session.execute(query).fetchall()
    performance_data = [{"employee_name": row[0], "total_quantity_produced": row[1]} for row in results]
    return jsonify(performance_data)

# Task 2: Identify Top Selling Products
@analytics_blueprint.route('/top-selling-products', methods=['GET'])
def identify_top_selling_products():
    query = """
        SELECT 
            p.name AS product_name,
            SUM(o.quantity) AS total_quantity_sold
        FROM 
            products p
        JOIN 
            orders o ON p.id = o.product_id
        GROUP BY 
            p.name
        ORDER BY 
            total_quantity_sold DESC;
    """
    results = db.session.execute(query).fetchall()
    top_products = [{"product_name": row[0], "total_quantity_sold": row[1]} for row in results]
    return jsonify(top_products)

# Task 3: Determine Customer Lifetime Value
@analytics_blueprint.route('/customer-lifetime-value', methods=['GET'])
def calculate_customer_lifetime_value():
    query = """
        SELECT 
            c.name AS customer_name,
            SUM(o.total_price) AS lifetime_value
        FROM 
            customers c
        JOIN 
            orders o ON c.id = o.customer_id
        GROUP BY 
            c.name
        HAVING 
            SUM(o.total_price) > 1000; -- Threshold value can be adjusted
    """
    results = db.session.execute(query).fetchall()
    customer_ltv = [{"customer_name": row[0], "lifetime_value": row[1]} for row in results]
    return jsonify(customer_ltv)

# Task 4: Evaluate Production Efficiency
@analytics_blueprint.route('/production-efficiency', methods=['GET'])
def evaluate_production_efficiency():
    # Replace '2024-11-29' with the specific date passed as a query parameter
    date = '2024-11-29'
    query = f"""
        SELECT 
            p.name AS product_name,
            SUM(pr.quantity_produced) AS total_quantity_produced
        FROM 
            products p
        JOIN 
            production pr ON p.id = pr.product_id
        WHERE 
            pr.date_produced = '{date}'
        GROUP BY 
            p.name;
    """
    results = db.session.execute(query).fetchall()
    efficiency_data = [{"product_name": row[0], "total_quantity_produced": row[1]} for row in results]
    return jsonify(efficiency_data)
