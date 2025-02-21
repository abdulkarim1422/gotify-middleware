import fastapi
from app.routers import gotify_routers
from app.routers import internal_routers

app = fastapi.FastAPI()

# Include routers
app.include_router(gotify_routers.router)
app.include_router(internal_routers.router, prefix="/api/v1", tags=["internal"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gotify MiddleWare App, which acts as a middleware between Gotify and the client, all endpoints are the same as the Gotify API, but with an additional layer."}