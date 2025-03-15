from fastapi import Depends
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.models.Groups import GroupInfo, GroupMembers


async def get_group_info(group_id: int, db: AsyncSession = Depends(get_db)):
    query = select(GroupInfo).where(GroupInfo.group_id == group_id)
    query_result = await db.execute(query)
    return query_result.scalar_one_or_none


async def get_group_members(group_id: int, db: AsyncSession = Depends(get_db)):
    query = select(GroupMembers).where(GroupMembers.group_id == group_id)
    query_result = await db.execute(query)
    return query_result.scalars().all()


async def get_user_groups(user_id: int, db: AsyncSession = Depends(get_db)):
    query = select(GroupMembers.group_id, GroupMembers.role).where(
        GroupMembers.member_id == user_id
    )
    query_result = await db.execute(query)
    return query_result.scalars().all()


async def create_group(
    name: str, description: str, creator_id: int, db: AsyncSession = Depends(get_db)
):
    query = (
        insert(GroupInfo)
        .values(
            group_name=name,
            group_description=description,
            creator_id=creator_id,
        )
        .returning(GroupInfo.group_id)
    )  # Return the created group's ID

    result = await db.execute(query)
    await db.commit()  # Commit transaction

    return {"group_id": result.scalar()}


async def add_group_member(
    group_id: int, member_id: int, role: str, db: AsyncSession = Depends(get_db)
):
    query = insert(GroupMembers).values(
        group_id=group_id, member_id=member_id, role=role
    )
    try:
        query_result = await db.execute(query)
    except TypeError:
        raise TypeError("Invalid Arguments")


async def remove_group_member(
    group_id: int, member_id: int, db: AsyncSession = Depends(get_db)
):
    query = delete(GroupMembers).where(
        (GroupMembers.group_id == group_id) and (GroupMembers.member_id == member_id)
    )
    query_result = await db.execute(query)
