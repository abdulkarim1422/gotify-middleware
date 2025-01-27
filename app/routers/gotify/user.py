from fastapi import APIRouter, Depends
import httpx
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth

router = APIRouter()

@router.get("/current/user", summary="Return the current user.")
async def get_current_user(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/current/user?token={query}", headers={"Authorization": header})
        response = await client.send(req)
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
    

    


