import fastapi
from app.routers import all_routers


app = fastapi.FastAPI()

# Include routers
app.include_router(all_routers.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gotify MiddleWare App, which acts as a middleware between Gotify and the client, all endpoints are the same as the Gotify API, but with an additional layer."}