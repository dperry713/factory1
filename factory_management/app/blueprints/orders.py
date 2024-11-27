from flask import Blueprint, request, jsonify
from app.models import Order, db
from app.utils.pagination import paginate_query

orders_blueprint = Blueprint('orders', __name__, url_prefix='/orders')

@orders_blueprint.route('/', methods=['GET'])
def get_orders():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = Order.query
    return jsonify(paginate_query(query, page, per_page))

@orders_blueprint.route('/', methods=['POST'])
def create_order():
    data = request.json
    order = Order(
        customer_id=data['customer_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        total_price=data['total_price']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201

@orders_blueprint.route('/<int:order_id>/', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.to_dict())
