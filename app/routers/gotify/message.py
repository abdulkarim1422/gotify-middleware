from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
import httpx
import websockets
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth

router = APIRouter()

@router.get("/application/{id}/message", summary="Return all messages for an application.")
async def get_messages(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/application/{id}/message?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    
@router.delete("/application/{id}/message", summary="Delete all messages for an application.")
async def delete_messages(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/application/{id}/message?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()

@router.get("/message", summary="Return all messages.")
async def get_all_messages(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/message?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    
@router.post("/message", summary="Create a message.")
async def create_message(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/message?token={query}", headers={"Authorization": header}, json=client.dict())
        response = await client.send(req)
        return response.json()
    
@router.delete("/message" , summary="Delete all messages.")
async def delete_all_messages(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/message?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    
@router.delete("/message/{id}", summary="Delete a message.")
async def delete_message(id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/message/{id}?token={query}", headers={"Authorization": header})
        response = await client.send(req)
        return response.json()
    
@router.websocket("/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        async with websockets.connect(f"{env_variables.GOTIFY_URL}/stream") as ws:
            async for message in ws:
                await websocket.send_text(message)
    except WebSocketDisconnect:
        pass
