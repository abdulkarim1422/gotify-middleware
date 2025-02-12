import requests
from requests.auth import HTTPBasicAuth
from app.initializers import env_variables

def get_all_clients(username, password):
    url = f"{env_variables.GOTIFY_URL}/client"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    return response.json() # [{'id': 1, 'name': 'xxxxxxx', 'token': 'xxXX.XXxx', 'lastUsed': '2019-01-01T00:00:00Z'}]

def create_client(username, password, name):
    url = f"{env_variables.GOTIFY_URL}/client"
    client_data = {
    "name": name
    }

    response = requests.post(url, json=client_data, auth=HTTPBasicAuth(username, password))
    return response.json() # {'id': 2, 'name': 'xxxxxxx', 'token': 'xxXX.XXxx', 'lastUsed': '2019-01-01T00:00:00Z'}

def get_client_by_name(username, password, name):
    clients = get_all_clients(username, password)
    for client in clients:
        if client['name'] == name:
            return client # {'id': 2, 'name': 'xxxxxxx', 'token': 'xxXX.XXxx', 'lastUsed': '2019-01-01T00:00:00Z'}
        
def update_client(username, password, client_id, name):
    url = f"{env_variables.GOTIFY_URL}/client/{client_id}"
    client_data = {
    "name": name
    }

    response = requests.put(url, json=client_data, auth=HTTPBasicAuth(username, password))
    return response.json() # {'id': 2, 'name': 'xxxxxxx', 'token': 'xxXX.XXxx', 'lastUsed': '2019-01-01T00:00:00Z'}

def delete_client(username, password, client_id):
    url = f"{env_variables.GOTIFY_URL}/client/{client_id}"
    response = requests.delete(url, auth=HTTPBasicAuth(username, password))
    return response.json() # ok