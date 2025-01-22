from fastapi import APIRouter, Request, Query
from app.routers.gotify import application, client, health, message, plugin, user, version

router = APIRouter()

# router.include_router(application.router)
# router.include_router(client.router)
router.include_router(health.router)
# router.include_router(message.router)
# router.include_router(plugin.router)
# router.include_router(user.router)
router.include_router(version.router)
