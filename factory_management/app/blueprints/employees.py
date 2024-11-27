from flask import Blueprint, request, jsonify
from app.models import Employee, db

employees_blueprint = Blueprint('employees', __name__, url_prefix='/employees')

@employees_blueprint.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])

@employees_blueprint.route('/', methods=['POST'])
def create_employee():
    data = request.json
    employee = Employee(name=data['name'], position=data['position'])
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee.to_dict()), 201
