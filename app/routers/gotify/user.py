from fastapi import APIRouter, Depends, HTTPException, Request
import httpx
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth
from pydantic import BaseModel
from app.middlewares import gotify_middleware
import json

router = APIRouter()

class User(BaseModel):
    admin: bool
    id: int
    name: str

@router.get("/current/user", response_model=User)
async def get_current_user(request: Request, query_header: tuple = Depends(gotify_auth)):
    print("Incoming request:", dict(request))
    print("Incoming request headers:", dict(request.headers))
    print("Incoming request body:", await request.body())
    # token = gotify_middleware.extract_token_from_request(request)
    # body = await request.body()
    query, header = query_header
    async with httpx.AsyncClient() as client:
        req = client.build_request(
            "GET",
            f"{env_variables.GOTIFY_URL}/current/user?token={query}",
            headers={"Authorization": header}
        )
        response = await client.send(req)
        if response.status_code == 401:
            raise HTTPException(status_code=401, detail="Unauthorized")
        if response.status_code == 403:
            raise HTTPException(status_code=403, detail="Forbidden")
        if response.status_code in [200, 201]:
            if not response.content:
                raise HTTPException(status_code=500, detail="Empty response from external service.")
            return response.json()
        return response.json()
    
@router.post("/current/user/password", summary="Update the current user's password.")
async def update_current_user_password(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/current/user/password?token={query}", headers={"Authorization": header}, json=client.dict())
        response = await client.send(req)
        return response.json()

@router.get("/user", summary="Return all users.")
async def get_users(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/user?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    
@router.post("/user", summary="Create a user.")
async def create_user(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/user?token={query}", headers={"Authorization": header}, json=client.dict())
        response = await client.send(req)
        return response.json()
    
@router.get("/user/{id}", summary="Get a user.")
async def get_user(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/user/{id}?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()

@router.post("/user/{id}", summary="Update a user.")
async def update_user(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/user/{id}?token={query}", headers={"Authorization": header}, json=client.dict())
        response = await client.send(req)
        return response.json()
    
@router.delete("/user/{id}", summary="Delete a user.")
async def delete_user(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/user/{id}?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    

    


