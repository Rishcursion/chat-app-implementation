from app.api.auth.routes import router
from app.core.config import variables
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": f"Server Running On {variables.SERVER_DOMAIN}"}
