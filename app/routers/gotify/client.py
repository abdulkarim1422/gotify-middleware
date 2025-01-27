from fastapi import APIRouter, Depends
import httpx
from app.initializers import env_variables
from app.services.gotify_auth import gotify_auth

router = APIRouter()

@router.get("/client", summary="Return all clients")
async def get_clients(query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        query, header = query_header
        req = client.build_request("GET", f"{env_variables.GOTIFY_URL}/client?token={query}", headers={"Authorization": header})
        print(req)
        response = await client.send(req)
        return response.json()

@router.post("/client", summary="Create a client")
async def create_client(request_body: dict, query_header: tuple = Depends(gotify_auth)):
    async with httpx.AsyncClient() as async_client:
        query, header = query_header
        req = async_client.build_request(
            "POST",
            f"{env_variables.GOTIFY_URL}/client?token={query}",
            headers={"Authorization": header},
            json=request_body
        )
        response = await async_client.send(req)
        return response.json()


@router.put("/client/{id}", summary="Update a client")
async def update_client(id: int, client: dict, api_key: str = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        req = client.build_request("PUT", f"{env_variables.GOTIFY_URL}/client/{id}?token={api_key}", json=client)
        response = await client.send(req)
        return response.json()

@router.delete("/client/{id}", summary="Delete a client")
async def delete_client(id: int, api_key: str = Depends(gotify_auth)):
    async with httpx.AsyncClient() as client:
        req = client.build_request("DELETE", f"{env_variables.GOTIFY_URL}/client/{id}?token={api_key}")
        response = await client.send(req)
        return response.json()
