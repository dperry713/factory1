from flask import Blueprint, request, jsonify
from app.models import Customer, db
from app.utils.pagination import paginate_query

customers_blueprint = Blueprint('customers', __name__, url_prefix='/customers')

@customers_blueprint.route('/', methods=['GET'])
def get_customers():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = Customer.query
    return jsonify(paginate_query(query, page, per_page))

@customers_blueprint.route('/', methods=['POST'])
def create_customer():
    data = request.json
    customer = Customer(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201

@customers_blueprint.route('/<int:customer_id>/', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify(customer.to_dict())
