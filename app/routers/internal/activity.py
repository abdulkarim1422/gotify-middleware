from fastapi import APIRouter, Request
from app.services import activity_service
from pydantic import BaseModel

router = APIRouter()

class UsersList(BaseModel):
    list_of_usernames: list

@router.post("/activity")
async def get_user_activity(
    request: Request,
    username: str
):
    user_last_activity = activity_service.get_user_last_active(username)
    return user_last_activity