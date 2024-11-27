from flask import Blueprint, request, jsonify
from app.models import Production, db
from app.utils.pagination import paginate_query

production_blueprint = Blueprint('production', __name__, url_prefix='/production')

@production_blueprint.route('/', methods=['GET'])
def get_production():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = Production.query
    return jsonify(paginate_query(query, page, per_page))

@production_blueprint.route('/', methods=['POST'])
def create_production():
    data = request.json
    production = Production(
        product_id=data['product_id'],
        quantity_produced=data['quantity_produced'],
        date_produced=data['date_produced']
    )
    db.session.add(production)
    db.session.commit()
    return jsonify(production.to_dict()), 201

@production_blueprint.route('/<int:production_id>/', methods=['GET'])
def get_production_record(production_id):
    production = Production.query.get_or_404(production_id)
    return jsonify(production.to_dict())
