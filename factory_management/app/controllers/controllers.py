from flask import Blueprint, request, jsonify
from models import Employee, db
from utils.util import token_required, role_required

employee_bp = Blueprint('employees', __name__)

@employee_bp.route('/employees', methods=['POST'])
@token_required
@role_required(['admin'])  # Only admins can create employees
def create_employee(user_id):
    data = request.json
    name = data.get('name')
    position = data.get('position')

    if not name or not position:
        return jsonify({'message': 'Invalid input'}), 400

    employee = Employee(name=name, position=position)
    db.session.add(employee)
    db.session.commit()

    return jsonify({'message': 'Employee created successfully'}), 201

@employee_bp.route('/employees', methods=['GET'])
@token_required
def get_employees(user_id):
    employees = Employee.query.all()
    result = [{'id': e.id, 'name': e.name, 'position': e.position} for e in employees]
    return jsonify(result), 200
