from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth.routes import router
from app.core.config import variables

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": f"Server Running On {variables.SERVER_DOMAIN}"}
