from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, Request
import httpx
import websockets
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth
import logging

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
async def websocket_endpoint(websocket: WebSocket, request: Request):
    try:
        query, _ = await gotify_auth(request)
        await websocket.accept()

        async with websockets.connect(
            f"{env_variables.GOTIFY_URL.replace('http', 'ws')}/stream?token={query}"
        ) as ws:
            async for message in ws:
                await websocket.send_text(message)
    except WebSocketDisconnect:
        logging.info("WebSocket connection closed by the client")
    except Exception as e:
        logging.error(f"Error in WebSocket endpoint: {e}")
        # Send error message to the WebSocket client (if needed)
        await websocket.send_text(f"Error: {e}")