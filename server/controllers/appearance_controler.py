from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.app import db
from models.appearance import Appearance

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    
    new_appearance = Appearance(
        rating=data.get('rating'),
        guest_id=data.get('guest_id'),
        episode_id=data.get('episode_id')
    )
    
    db.session.add(new_appearance)
    db.session.commit()
    
    return jsonify(new_appearance.to_dict()), 201
