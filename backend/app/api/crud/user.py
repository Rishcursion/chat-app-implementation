from fastapi.exceptions import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.User import UserAuth


async def get_user_by_username(username: str, db: AsyncSession):
    query = select(UserAuth).where(UserAuth.user_name == username)
    query_result = await db.execute(query)
    details = query_result.scalar_one_or_none()
    return details


async def get_user_by_userid(user_id: str, db: AsyncSession):
    query = select(UserAuth).where(UserAuth.user_id == user_id)
    query_result = await db.execute(query)
    details = query_result.scalar_one_or_none()
    if details:
        return details
    else:
        raise HTTPException(401, detail="User Does Not Exist?")


async def register_user(username: str, password: str, db: AsyncSession) -> bool:
    query = insert(UserAuth).values(user_name=username, password=password)
    result = await db.execute(query)
    await db.commit()
    return result.rowcount > 0
