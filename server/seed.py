from app import app
from models import db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from werkzeug.security import generate_password_hash

def seed():
    with app.app_context():
        
        
        db.drop_all()
        db.create_all()

        
        user1 = User(username="admin", password_hash=generate_password_hash("admin123"))
        db.session.add(user1)

        
        guest1 = Guest(name="Emma Stone", occupation="Actor")
        guest2 = Guest(name="Trevor Noah", occupation="Comedian")

        
        episode1 = Episode(date="2023-06-01", number=101)
        episode2 = Episode(date="2023-06-02", number=102)

        db.session.add_all([guest1, guest2, episode1, episode2])
        db.session.commit()

        
        appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)

        db.session.add_all([appearance1, appearance2])
        db.session.commit()

        

if __name__ == "__main__":
    seed()
