from flask import Blueprint, make_response
from models.guest import Guest

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    result = [g.to_dict() for g in guests] 
    return make_response(result,200)
