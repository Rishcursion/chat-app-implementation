from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db, logger
from app.schemas.userdetails import UserDetails
