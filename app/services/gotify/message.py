import requests
from requests.auth import HTTPBasicAuth
from app.initializers import env_variables

def get_all_messages_from_app(username, password, app_id):
    url = f"{env_variables.GOTIFY_URL}/application/{app_id}/message"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    return response.json()
'''
{
  "messages": [
    {
      "appid": 5,
      "date": "2018-02-27T19:36:10.5045044+01:00",
      "extras": {
        "home::appliances::lighting::on": {
          "brightness": 15
        },
        "home::appliances::thermostat::change_temperature": {
          "temperature": 23
        }
      },
      "id": 25,
      "message": "**Backup** was successfully finished.",
      "priority": 2,
      "title": "Backup"
    }
  ],
  "paging": {
    "limit": 123,
    "next": "http://example.com/message?limit=50&since=123456",
    "since": 5,
    "size": 5
  }
}
'''

def delete_all_messages_from_app(username, password, app_id):
    url = f"{env_variables.GOTIFY_URL}/application/{app_id}/message"
    response = requests.delete(url, auth=HTTPBasicAuth(username, password))
    return response.json() # ok

def get_all_messages(username, password):
    url = f"{env_variables.GOTIFY_URL}/message"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    return response.json()
'''
{
  "messages": [
    {
      "appid": 5,
      "date": "2018-02-27T19:36:10.5045044+01:00",
      "extras": {
        "home::appliances::lighting::on": {
          "brightness": 15
        },
        "home::appliances::thermostat::change_temperature": {
          "temperature": 23
        }
      },
      "id": 25,
      "message": "**Backup** was successfully finished.",
      "priority": 2,
      "title": "Backup"
    }
  ],
  "paging": {
    "limit": 123,
    "next": "http://example.com/message?limit=50&since=123456",
    "since": 5,
    "size": 5
  }
}
'''

def create_message(app_token, title, message_body, priority=5):
    url = f"{env_variables.GOTIFY_URL}/message?token={app_token}"
    params = {
    'title': title,
    'message': message_body,
    'priority': priority
    }
    response = requests.post(url, data=params)
    return response.json()
# {'id': 1, 'appid': 4, 'message': 'xxxxxxxxxxxxx', 'title': 'xxxxx', 'priority': 5, 'date': '2025-01-08T22:06:48.131229606Z'}

def delete_all_messages(username, password):
    url = f"{env_variables.GOTIFY_URL}/message"
    response = requests.delete(url, auth=HTTPBasicAuth(username, password))
    return response.json() # ok

def delete_message(username, password, message_id):
    url = f"{env_variables.GOTIFY_URL}/message/{message_id}"
    response = requests.delete(url, auth=HTTPBasicAuth(username, password))
    return response.json() # ok
