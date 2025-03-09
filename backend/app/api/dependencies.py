import logging

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.db import SessionLocal
from app.utils.security import decode_token


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


security = HTTPBearer()


def logger() -> logging.Logger:
    logger = logging.getLogger("uvicorn.error")
    logger.setLevel(logging.DEBUG)
    return logger


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    token = credentials.credentials
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload  # Returns decoded token data (e.g., user ID, username)
