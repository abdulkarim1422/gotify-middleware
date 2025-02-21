from fastapi import APIRouter, Request, Query
from app.services import activity_service

router = APIRouter()

@router.get("/activity")
async def get_users_activity(
    request: Request,
    list_of_users: list = Query(None, description="List of users") # list of usernames
):
    users_activity = []
    for username in list_of_users:
        user_last_activity = activity_service.get_user_last_active(username)
        users_activity.append({"username": username, "last_active": user_last_activity})
    return users_activity