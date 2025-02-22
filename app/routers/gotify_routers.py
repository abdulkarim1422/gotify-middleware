from fastapi import APIRouter
from app.routers.gotify import application, client, health, message, plugin, user, version, static

router = APIRouter()

router.include_router(application.router, tags=["application"])
router.include_router(client.router, tags=["client"])
router.include_router(health.router, tags=["health"])
router.include_router(message.router, tags=["message"])
router.include_router(plugin.router, tags=["plugin"])
router.include_router(user.router, tags=["user"])
router.include_router(version.router, tags=["version"])
router.include_router(static.router, tags=["static"])