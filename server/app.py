
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
# from flask_cors import CORS
from models import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
# CORS(app)

from controllers.auth_controller import auth_bp
from controllers.episode_controller import episode_bp
from controllers.guest_controller import guest_bp
from controllers.appearance_controler import appearance_bp


app.register_blueprint(auth_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(appearance_bp)


if __name__ == '__main__':
    app.run(debug=True)