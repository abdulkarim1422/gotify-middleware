from app.services.gotify.user import current_user_via_token
from app.repositories import user_repo
from datetime import datetime

def update_user_last_active(x_gotify_key):
    # get user via x-gotify-key
    user_json = current_user_via_token(x_gotify_key)
    
    # get user from db
    user_obj = user_repo.get_user_by_username(user_json["name"])

    # update user last active
    user_obj.last_active = datetime.now()
    user_repo.update_user(user_obj)

def get_user_last_active(username):
    # get user from db
    user_obj = user_repo.get_user_by_username(username)
    if user_obj:
        return user_obj.last_active
    return None