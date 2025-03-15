from typing import Literal

from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.models.Groups import GroupMembers
from app.models.Messages import DirectMessages, GroupMessages, UserMessages

# async def get_user_by_username(username: str, db: AsyncSession):
#     query = select(UserAuth).where(UserAuth.user_name == username)
#     query_result = await db.execute(query)
#     details = query_result.scalar_one_or_none()
#     return details


# Get All Direct Messages Involving The User, Will Be Used If User Is Syncing Messages, Due To Heavy Read Operations
async def get_direct_messages(user_id: int, db: AsyncSession = Depends(get_db)):
    query = (
        select(UserMessages)
        .join(DirectMessages, DirectMessages.message_id == UserMessages.message_id)
        .where(
            UserMessages.sender_id == user_id or DirectMessages.reciever_id == user_id
        )
    )
    query_result = await db.execute(query)
    direct_chats = query_result.scalars().all()
    return direct_chats

# Persists user messages in server database
async def persist_user_message(
    user_id: int,
    chat_type: Literal["group", "direct"],
    content: str = "",
    receiver_id: int = -1,
    reply_to: int = -1,
    group_id: int = -1,
    db: AsyncSession = Depends(get_db),
):
    # Validate input parameters
    if (chat_type == "group" and group_id == -1) or (
        chat_type == "direct" and receiver_id == -1
    ):
        return

    # Insert message into UserMessages
    message_data = {"user_id": user_id, "message_content": content}
    if reply_to != -1:
        message_data["reply_to"] = reply_to

    result = await db.execute(
        insert(UserMessages).values(**message_data).returning(UserMessages.message_id)
    )
    message_id = result.scalar()  # Fetch the newly inserted message_id

    # Insert into either GroupMessages or DirectMessages
    if chat_type == "group":
        await db.execute(
            insert(GroupMessages).values(group_id=group_id, message_id=message_id)
        )
    else:
        await db.execute(
            insert(DirectMessages).values(
                receiver_id=receiver_id, message_id=message_id
            )
        )

    await db.commit()  # Commit all changes


async def get_group_messages(user_id: int, db: AsyncSession = Depends(get_db)):
    query = (
        select(
            GroupMessages.group_id,
            UserMessages.message_id,
            UserMessages.sender_id,
            UserMessages.message_content,
            UserMessages.sent_time,
            GroupMessages.read_reciepts,
        )
        .join(GroupMessages, GroupMessages.message_id == UserMessages.message_id)
        .join(GroupMembers, GroupMembers.group_id == GroupMessages.group_id)
        .where(GroupMembers.member_id == user_id)
        .order_by(
            GroupMessages.group_id, UserMessages.sent_time
        )  # Ensure correct grouping
    )
    result = await db.execute(query)
    messages = result.scalars().all()
    return messages
