from models.users import User
from sqlalchemy.orm import Session


def create_user(db: Session):
    user = db.add(User)

    
