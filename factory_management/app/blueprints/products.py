from flask import Blueprint, request, jsonify
from app.models import Product, db
from app.utils.pagination import paginate_query

products_blueprint = Blueprint('products', __name__, url_prefix='/products')

@products_blueprint.route('/', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = Product.query
    return jsonify(paginate_query(query, page, per_page))

@products_blueprint.route('/', methods=['POST'])
def create_product():
    data = request.json
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201
