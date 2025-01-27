from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/static/defaultapp.png")
async def get_default_app_image():
    file_path = "defaultapp.png"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")