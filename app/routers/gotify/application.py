from fastapi import APIRouter, Depends, HTTPException, status
import httpx
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth

router = APIRouter()

@router.get("/application", summary="Return all applications.")
async def get_apps(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/application?token={query}", headers={"Authorization": header})
        print(req)
        response = await client.send(req)
        return response.json()

