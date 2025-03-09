import logging

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.schemas.userdetails import UserDetails
from app.utils.security import create_token, verify_password

# Define a parent router for authentication
router = APIRouter(prefix="/auth", tags=["Authentication"])
logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)


@router.post("/login")
async def login(user_data: UserDetails):
    username = user_data.username
    password = user_data.password
    logger.debug(
        f"Recieved Login Details From User: {username}",
    )
    user_details = get_user(username)
    if not user_details:
        raise HTTPException(404, detail="User Not Found!")
    else:
        hashed_password = user_details.password
        match = verify_password(password=password, hash=hashed_password)
        if match:
            return {
                "access_token": create_token(
                    {
                        "user_id": user_details.user_id,
                        "user_name": user_details.user_name,
                    }
                ),
                "token_type": "bearer",
            }
        else:
            raise HTTPException(401, detail="Uh Oh! Invalid Credentials")
