import datetime

from sqlalchemy import BOOLEAN, CHAR, TIMESTAMP, VARCHAR, Integer, Text, func, text
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class UserAuth(Base):
    __tablename__ = "user_auth"
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column(VARCHAR(64), nullable=False)
    password: Mapped[str] = mapped_column(CHAR(73), nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    friend_code: Mapped[str] = mapped_column(
        BYTEA,
        nullable=False,
        unique=True,
        server_default=text("encode(gen_random_bytes(4), 'hex')"),
    )
    created_on: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    is_active: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    last_active: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    user_to_messages = relationship(
        "UserMessages",
        back_populates="messages_to_user",
        foreign_keys="UserMessages.sender_id",
    )
    user_to_direct = relationship("DirectMessages", back_populates="direct_to_user")
    user_to_info = relationship("GroupInfo", back_populates="info_to_user")
    user_to_messages_replies = relationship(
        "UserMessages",
        back_populates="messages_replies_to_user",
        foreign_keys="UserMessages.reply_to",
    )
    users_to_members = relationship("GroupMembers", back_populates="members_to_users")
