from app.initializers import db
from app import models
from sqlmodel import select

def get_all_users():
    with db.get_session() as session:
        users = session.exec(select(models.User)).all()
        return users

def get_user_by_id(user_id):
    with db.get_session() as session:
        user = session.get(models.User, user_id)
        return user
    
def get_user_by_username(username):
    with db.get_session() as session:
        user = session.exec(select(models.User).where(models.User.username == username)).first()
        return user
    
def create_user(user):
    with db.get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def update_user(user):
    with db.get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def delete_user(user):
    with db.get_session() as session:
        session.delete(user)
        session.commit()
        return user
    
