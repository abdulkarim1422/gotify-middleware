from app.repositories import user_repo
from app.services import gotify
from app import models
import uuid

def create_and_store_user(username, password):
    # create user in gotify
    gotify.user.create_user(username, password)
    
    # create stable client for this uset in gotify
    client_token = create_client_for_user(username=username, password=password)

    # store user in db
    user = models.User(id=uuid.uuid4(), username=username, password=password, client_token=client_token)
    user_repo.create_user(user)

    return user

def create_client_for_user(username, password, client_name="stable"):
    # create client in gotify
    client = gotify.client.create_client(username, password, client_name)
    return client["token"]

def get_user_token(username):
    user = user_repo.get_user_by_username(username)
    return user.client_token

def get_user_by_username(username):
    # get user from db
    user = user_repo.get_user_by_username(username)

    # if user not found, look in gotify server
    if not user:
        user = check_and_update_user(username)     

    return user

def check_and_update_user(username):
    # bring all users from gotify server
    users = gotify.user.get_all_users()
    # search for the user in the list
    user = next((user for user in users if user["name"] == username), None)

    
    if user: # if user found, update the user password to username
        gotify.user.update_user(user_id=user["id"], username=username, password=username)
        client_token = create_client_for_user(username=username, password=username)
        user = models.User(username=username, password=username, client_token=client_token)
        user_repo.update_user(user)
        return user
    else: # if user not found, create the user in gotify
        user = gotify.user.create_user(username=username, password=username)
        # store user in db
        client_token = create_client_for_user(username=username, password=username)
        user = models.User(id=uuid.uuid4(), username=username, password=username, client_token=client_token)
        user_repo.create_user(user)
        return user
