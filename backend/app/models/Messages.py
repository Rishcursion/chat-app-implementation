import datetime

from db import Base
from sqlalchemy import (
    Boolean,
    JSON,
    TIMESTAMP,
    BigInteger,
    ForeignKey,
    Integer,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, Relationship, mapped_column, relationship


class Messages(Base):
    __tablename__ = "user_messages"
    message_id = mapped_column(BigInteger, primary_key=True)
    sender_id = mapped_column(Integer, ForeignKey("user_auth.user_id"), nullable=False)
    sent_time = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    message_content = mapped_column(Text, nullable=False)
    reply_to = mapped_column(Integer, ForeignKey("user_messages.message_id"), nullable=True)
    read_reciepts = mapped_column(JSON, nullable=True)
    edited_time = mapped_column(TIMESTAMP, nullable=True)
    isdeleted = mapped_column(Boolean, default=False)
    edited = mapped_column(Boolean, default=False)

    # Relationships
    sender = relationship("UserAuth", back_populates="messages_sender")
    replies = relationship("Messages", remote_side=[message_id])

class DirectMessages(Base):
    __tablename__ = "direct_messages"
    message_id = mapped_column(BigInteger, ForeignKey("user_messages.message_id"), primary_key=True)
    reciever_id = mapped_column(Integer, ForeignKey("user_auth.user_id"), nullable=False)

    # Relationships
    reciever = relationship("UserAuth", back_populates="direct_messages")


class GroupMessages(Base):
    __tablename__ = "group_messages"
    message_id = mapped_column(BigInteger, ForeignKey("user_messages.message_id"), primary_key=True)
    group_id = mapped_column(Integer, ForeignKey("group_info.group_id"), nullable=False)

    # Relationships
    group = relationship("GroupInfo", back_populates="group_messages")
    message = relationship("Messages", back_populates="group_messages")
