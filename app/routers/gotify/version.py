from fastapi import APIRouter
import httpx
from app.initializers import env_variables

router = APIRouter()

@router.get("/version")
async def get_version():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{env_variables.GOTIFY_URL}/version")
        return response.json()