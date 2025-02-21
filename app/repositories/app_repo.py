from app.initializers import db
from app.models import app_model
from sqlmodel import select

def get_all_apps():
    with db.get_session() as session:
        apps = session.exec(select(app_model.App)).all()
        return apps
    
def get_app_by_id(app_id):
    with db.get_session() as session:
        app = session.get(app_model.App, app_id)
        return app
    
def get_apps_by_user_id(user_id):
    with db.get_session() as session:
        apps = session.exec(select(app_model.App).where(app_model.App.user_id == user_id)).all()
        return apps
    
def get_apps_by_project_id(project_id):
    with db.get_session() as session:
        apps = session.exec(select(app_model.App).where(app_model.App.project_id == project_id)).all()
        return apps
    
def create_app(app):
    with db.get_session() as session:
        session.add(app)
        session.commit()
        session.refresh(app)
        return app
    
def update_app(app):
    with db.get_session() as session:
        session.add(app)
        session.commit()
        session.refresh(app)
        return app
    
def delete_app(app):
    with db.get_session() as session:
        session.delete(app)
        session.commit()
        return app
    
    