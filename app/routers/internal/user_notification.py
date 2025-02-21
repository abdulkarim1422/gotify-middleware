from fastapi import APIRouter, Request, Query
from app.services import user_service, notification_service

router = APIRouter()

@router.post("/user")
async def create_user(
    request: Request,
    username: str = Query(..., description="The username of the user"),
    password: str = Query(..., description="The password of the user")
):
    username = request.query_params.get("username")
    password = request.query_params.get("password")
    if not username or not password:
        return {"error": "Missing required query parameters"}
    user = user_service.create_and_store_user(username, password)
    return user.model_dump()


@router.post("/notification")
async def create_notification(
    request: Request,
    username: str = Query(..., description="The username of the user"),
    projectname: str = Query(None, description="The name of the project"),
    title: str = Query(..., description="The title of the notification"),
    content: str = Query(..., description="The content of the notification")
):
    username = request.query_params.get("username")
    projectname = request.query_params.get("projectname")
    title = request.query_params.get("title")
    content = request.query_params.get("content")
    if not username or not title or not content:
        return {"error": "Missing required query parameters"}
    notification_service.send_notification(username, projectname, title, content)
    return {"message": "Notification sent successfully"}

