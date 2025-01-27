from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, Request
import httpx
import websockets
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth
import logging
from urllib.parse import parse_qs
import json

router = APIRouter()

@router.get("/application/{id}/message", summary="Return all messages for an application.")
async def get_messages(request: Request, id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/application/{id}/message?token={query}", headers=dict(request.headers))
        response = await client.send(req)
        return response.json()
    
@router.delete("/application/{id}/message", summary="Delete all messages for an application.")
async def delete_messages(request: Request, id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/application/{id}/message?token={query}", headers=dict(request.headers))
        response = await client.send(req)
        return response.json()

@router.get("/message", summary="Return all messages.")
async def get_all_messages(request: Request, limit: int = 100, since: int = 0, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request(
            "GET",
            f"{env_variables.GOTIFY_URL}/message?token={query}&limit={limit}&since={since}",
            headers=dict(request.headers)
        )
        response = await client.send(req)
        return response.json()
    
@router.post("/message", summary="Create a message.")
async def create_message(request: Request, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        body = await request.json()
        print(body)
        body = json.dumps(body)
        print(body)
        query, _ = query_header
        req = client.build_request("POST", f"{env_variables.GOTIFY_URL}/message?token={query}", headers=dict(request.headers), json=body)
        response = await client.send(req)
        return response.json()
    
@router.delete("/message" , summary="Delete all messages.")
async def delete_all_messages(request: Request, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/message?token={query}", headers=dict(request.headers))
        response = await client.send(req)
        return response.json()
    
@router.delete("/message/{id}", summary="Delete a message.")
async def delete_message(request: Request, id: int, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, _ = query_header
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/message/{id}?token={query}", headers=dict(request.headers))
        response = await client.send(req)
        return response.json()
    
@router.websocket("/stream")
async def websocket_endpoint(websocket: WebSocket):
    print(websocket)
    query_params = parse_qs(websocket.url.query)
    gotify_key = query_params.get("token", [None])[0]
    # gotify_key = websocket.headers.get("x-gotify-key")
    if not gotify_key:
        await websocket.close(code=1008)  # Close with an error code
        return

    await websocket.accept()

    try:
        async with websockets.connect(
            f"{env_variables.GOTIFY_URL.replace('http', 'ws')}/stream?token={gotify_key}"
        ) as ws:
            async for message in ws:
                await websocket.send_text(message)
    except WebSocketDisconnect:
        logging.info("WebSocket connection closed by the client")
    except Exception as e:
        logging.error(f"Error in WebSocket endpoint: {e}")
        await websocket.close(code=1011)  # Internal server error

