from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader, APIKeyQuery
from pydantic import BaseModel
from typing import List
import httpx
from app.initializers import env_variables

router = APIRouter()

api_key_header = APIKeyHeader(name="X-Gotify-Key", auto_error=False)
api_key_query = APIKeyQuery(name="token", auto_error=False)

def get_api_key(
    api_key_header: str = Depends(api_key_header),
    api_key_query: str = Depends(api_key_query),
):
    if api_key_header:
        return api_key_header
    elif api_key_query:
        return api_key_query
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

@router.get("/client", summary="Return all clients")
async def get_clients(api_key: str = Depends(get_api_key)):
    async with httpx.AsyncClient() as client:
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/client?token={api_key}")
        print(req)
        response = await client.send(req)
        return response.json()
