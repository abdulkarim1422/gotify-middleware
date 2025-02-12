from app.services import user_service
from app.services import gotify
from app.services import application_service

def send_notification(username, projectname, title, content):
    if not projectname:
        projectname = "default"
    app = application_service.check_app(username=username, app_name=projectname)
    gotify.message.create_message(app_token=app.app_token, title=title, message_body=content)
    return True


