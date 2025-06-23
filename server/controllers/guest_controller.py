from flask import Blueprint, jsonify
from models.guest import Guest

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    result = [g.to_dict() for g in guests] 
    return jsonify(result), 200
