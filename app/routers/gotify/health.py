from fastapi import APIRouter
import httpx
from app.initializers import env_variables

router = APIRouter()

@router.get("/health")
async def get_health():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{env_variables.GOTIFY_URL}/health")
        return response.json()