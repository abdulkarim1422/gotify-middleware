from fastapi import APIRouter, Depends
import httpx
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth

router = APIRouter()

@router.get("/plugin", summary="Return all plugins.")
async def get_plugins(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/plugin?token={query}", headers={"Authorization": header})
        print(req)
        response = await client.send(req)
        return response.json()
    
@router.get("/plugin/{id}/config", summary="Get YAML configuration for Configurer plugin.")
async def get_plugin_config(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/plugin/{id}/config?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    
@router.post("/plugin/{id}/config", summary="Update YAML configuration for Configurer plugin.")
async def update_plugin_config(id: int, config: dict, api_key: str = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/plugin/{id}/config?token={api_key}", json=config)
        response = await client.send(req)
        return response.json()
    
@router.post("/plugin/{id}/disable", summary="Disable a plugin.")
async def disable_plugin(id: int, api_key: str = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/plugin/{id}/disable?token={api_key}")
        response = await client.send(req)
        return response.json()
    
@router.get("/plugin/{id}/display", summary="Get display information for a Displayer plugin.")
async def get_plugin_display(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/plugin/{id}/display?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    
@router.post("/plugin/{id}/enable", summary="Enable a plugin.")
async def enable_plugin(id: int, api_key: str = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/plugin/{id}/enable?token={api_key}")
        response = await client.send(req)
        return response.json()
    
    


