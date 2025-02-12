import requests
from app.initializers import env_variables

def get_all_apps(client_token):
    url = f"{env_variables.GOTIFY_URL}/application?token={client_token}"
    response = requests.get(url)
    return response.json()
# [{'id': 1, 'name': 'xxxxxxx', 'description': 'xxxxxxx', 'defaultPriority': 5, "token": "xxXX.XXxx", "image": "image/image.jpeg", "internal": false,"lastUsed": "2019-01-01T00:00:00Z"}]

def create_app(client_token, name, description="", defaultPriority=5):
    url = f"{env_variables.GOTIFY_URL}/application?token={client_token}"
    app_data = {
    "name": name,
   "description": description,
    "defaultPriority": defaultPriority
    }

    response = requests.post(url, json=app_data)
    return response.json() 
# {'id': 2, 'name': 'xxxxxxx', 'description': 'xxxxxxx', 'defaultPriority': 5, "token": "xxXX.XXxx", "image": "image/image.jpeg", "internal": false,"lastUsed": "2019-01-01T00:00:00Z"}
    
def update_app(client_token, app_id, name, description, defaultPriority=5):
    url = f"{env_variables.GOTIFY_URL}/application/{app_id}?token={client_token}"
    app_data = {
    "name": name,
   "description": description,
    "defaultPriority": defaultPriority
    }

    response = requests.put(url, json=app_data)
    return response.json()
# {'id': 2, 'name': 'xxxxxxx', 'description': 'xxxxxxx', 'defaultPriority': 5, "token": "xxXX.XXxx", "image": "image/image.jpeg", "internal": false,"lastUsed": "2019-01-01T00:00:00Z"}

def delete_app(client_token, app_id):
    url = f"{env_variables.GOTIFY_URL}/application/{app_id}?token={client_token}"
    response = requests.delete(url)
    return response.json()

def upload_image(client_token, app_id, image_path):
    url = f"{env_variables.GOTIFY_URL}/application/{app_id}/image?token={client_token}"
    files = {'file': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()

def delete_image(client_token, app_id):
    url = f"{env_variables.GOTIFY_URL}/application/{app_id}/image?token={client_token}"
    response = requests.delete(url)
    return response.json()
