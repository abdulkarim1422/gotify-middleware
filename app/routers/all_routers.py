from fastapi import APIRouter, Request, Query
from app.routers.gotify import application, client, health, message, plugin, user, version

router = APIRouter()

router.include_router(application.router, tags=["application"])
router.include_router(client.router, tags=["client"])
router.include_router(health.router, tags=["health"])
router.include_router(message.router, tags=["message"])
# router.include_router(plugin.router)
# router.include_router(user.router)
router.include_router(version.router, tags=["version"])
