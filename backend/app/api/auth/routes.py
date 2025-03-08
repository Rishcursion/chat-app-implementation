import logging

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.api.dependencies import get_db
from app.models import UserAuth
from app.schemas.userdetails import UserDetails

# Define a parent router for authentication
router = APIRouter(prefix="/auth", tags=["Authentication"])
logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)


@router.post("/login")
async def login(user_data: UserDetails, db: AsyncSession = Depends(get_db)):
    username = user_data.username
    password = user_data.password
    logger.debug(
        f"Recieved Login Details, details: {user_data}",
    )
    user_details = await db.execute(select(UserAuth))
    user = user_details.scalar()
    logger.debug(f"user_details : {user.created_on}")
    return {"access_token": "asdfjaklsdfjakdfjaldsfkjasdfs", "token_type": "bearer"}
