import datetime

from sqlalchemy import TIMESTAMP, BigInteger, Boolean, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class UserMessages(Base):
    __tablename__ = "user_messages"
    message_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    sender_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user_auth.user_id"), nullable=False
    )
    sent_time: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )
    message_content: Mapped[str] = mapped_column(Text, nullable=False)
    reply_to: Mapped[int] = mapped_column(
        Integer, ForeignKey("user_auth.user_id"), nullable=True
    )
    read_reciepts: Mapped[dict] = mapped_column(JSONB, nullable=True)
    edited_time: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    isdeleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    edited: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    messages_to_user = relationship(
        "UserAuth", back_populates="user_to_messages", foreign_keys=[sender_id]
    )
    messages_to_direct = relationship(
        "DirectMessages", back_populates="direct_to_messages"
    )
    messages_to_group_messages = relationship(
        "GroupMessages", back_populates="group_messages_to_messages"
    )
    messages_replies_to_user = relationship(
        "UserAuth", back_populates="user_to_messages_replies", foreign_keys=[reply_to]
    )


class DirectMessages(Base):
    __tablename__ = "direct_messages"
    message_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("user_messages.message_id"),
        nullable=False,
        primary_key=True,
    )
    reciever_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user_auth.user_id"), nullable=False
    )
    direct_to_messages = relationship(
        "UserMessages", back_populates="messages_to_direct"
    )
    direct_to_user = relationship("UserAuth", back_populates="user_to_direct")


class GroupMessages(Base):
    __tablename__ = "group_messages"
    message_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("user_messages.message_id"),
        nullable=False,
        primary_key=True,
    )
    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("group_info.group_id"), nullable=False
    )
    group_messages_to_messages = relationship(
        "UserMessages", back_populates="messages_to_group_messages"
    )
    group_messages_to_group = relationship("GroupInfo",back_populates="group_to_group_messages")
