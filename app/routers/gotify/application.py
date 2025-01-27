from fastapi import APIRouter, Depends, Request
import httpx
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth

router = APIRouter()

@router.get("/application", summary="Return all applications.")
async def get_apps(request: Request, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/application?token={query}", headers=dict(request.headers))
        response = await client.send(req)
        return response.json()

@router.post("/application", summary="Create an application.")
async def create_app(request: Request, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/application?token={query}", headers=dict(request.headers), json=client.dict())
        response = await client.send(req)
        return response.json()
    
@router.put("/application/{id}", summary="Update an application.")
async def update_app(request: Request, id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request("PUT", f"{env_variables.GOTIFY_URL}/application/{id}?token={query}", headers=dict(request.headers), json=client.dict())
        response = await client.send(req)
        return response.json()
    
@router.delete("/application/{id}", summary="Delete an application.")
async def delete_app(request: Request, id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/application/{id}?token={query}", headers=dict(request.headers))
        response = await client.send(req)
        return response.json()
    
@router.post("/application/{id}/image", summary="Upload an image for an application.")
async def upload_image(request: Request, id: int, file: bytes, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/application/{id}/image?token={query}", headers=dict(request.headers), files={"file": file})
        response = await client.send(req)
        return response.json()
    
@router.delete("/application/{id}/image", summary="Delete an image for an application.")
async def delete_image(request: Request, id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/application/{id}/image?token={query}", headers=dict(request.headers))
        response = await client.send(req)
        return response.json()
    


