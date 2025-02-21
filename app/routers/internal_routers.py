from fastapi import APIRouter
from app.routers.internal import activity, user_notification

router = APIRouter()

router.include_router(activity.router)
router.include_router(user_notification.router)