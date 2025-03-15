import logging

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.crud.user import get_user_by_userid, get_user_by_username, register_user
from app.api.dependencies import get_db, logger
from app.schemas.userdetails import UserDetails
from app.utils.security import (
    create_token,
    decode_token,
    hash_password,
    verify_password,
)

# Define a parent router for authentication
router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post("/login")
async def login(
    user_data: UserDetails,
    db: AsyncSession = Depends(get_db),
    logger: logging.Logger = Depends(logger),
):
    """Authentication function that handles login

    Creates a valid JSON Web Token if the provided user details are valid and exists in the database.

    Args:
        user_data: Pydantic object that contains the parameters sent by the frontend
        db: Async SQLAlchemy session to execute queries asynchronously
        logger: logger object for debugging.

    Raises:
        HTTPException: 404 NOT FOUND, error is raised if the  provided user details do not exists in
                       the database.
        HTTPException: 401 UNAUTHORIZED, error is raised if the username exists in the database but the
                       password provided does not match what exists in the database.
    """
    username = user_data.username
    password = user_data.password
    logger.debug(
        f"Recieved Login Details From User: {username}",
    )
    user_details = await get_user_by_username(username=username, db=db)
    if not user_details:
        logger.debug(f"Username :{username} not found in database")
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
            logger.debug(f"Invalid Credentials For User: {username}")
            raise HTTPException(401, detail="Uh Oh! Invalid Credentials")


@router.post("/register")
async def register(
    user_data: UserDetails,
    db: AsyncSession = Depends(get_db),
    logger: logging.Logger = Depends(logger),
):
    """adds user details

    Registers a user in the database if the credentials do not already exist.

    Args:
        user_data: a Pydantic model with username and password attributes 
        db: database dependency 
        logger: logging dependency 

    Raises:
        HTTPException: 400, if the user already is registered 
        HTTPException: 500, if the database commit fails. 
    """
    username = user_data.username
    password = user_data.password
    logger.debug(f"Recieved Register Request From User: {username}")
    existence_check = await get_user_by_username(username, db)
    password_hashed = hash_password(password)
    if existence_check:
        raise HTTPException(400, detail="User Already Exists!")
    result = await register_user(username=username, password=password_hashed, db=db)
    if not result:
        raise HTTPException(500, detail="Registering User Failed!")


@router.get("/me")
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
    logger: logging.Logger = Depends(logger),
):
    """Returns current user's details

    Returns the user id and username based on the jwt associated with that user.

    Args:
        token: JSON Web Token associated with the user.
        db: database dependency

    Raises:
        HTTPException: 401, if the token is expired or invalid.
        HTTPException: 404, if the token is valid but the user is not found in the database.
    """
    logger.debug(f"Recieved Ping, token: {token}")
    payload = decode_token(token)  # Decode JWT
    logger.debug(f"User Token Recieved: {payload}")
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload.get("user_id")
    user = await get_user_by_userid(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    logger.debug(f"Invite Code: {user.friend_code.hex()}")
    return {"username": user.user_name, "invite_code": str(user.friend_code.hex())}
