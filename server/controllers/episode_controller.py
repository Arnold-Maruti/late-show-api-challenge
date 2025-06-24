from flask import Blueprint, jsonify, request
from app import db
from models.episode import Episode
from models.appearance import Appearance
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    result = [e.to_dict() for e in episodes] 
    return jsonify(result), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    episode_data = episode.to_dict()
    episode_data['appearances'] = [a.to_dict() for a in appearances]
    return jsonify(episode_data), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"msg": "Episode deleted"}), 200
