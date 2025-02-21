from fastapi import APIRouter, Request
from app.services import activity_service
from pydantic import BaseModel

router = APIRouter()

class UsersList(BaseModel):
    list_of_usernames: list

@router.post("/activitise")
async def get_users_activity(
    request: Request,
    users_list: UsersList
):
    users_activity = []
    for username in users_list.list_of_usernames:
        user_last_activity = activity_service.get_user_last_active(username)
        users_activity.append({"username": username, "last_active": user_last_activity})
    return users_activity

@router.post("/activity")
async def get_user_activity(
    request: Request,
    username: str
):
    user_last_activity = activity_service.get_user_last_active(username)
    return user_last_activity