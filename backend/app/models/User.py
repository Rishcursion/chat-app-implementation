import datetime

from db import Base
from sqlalchemy import BIGINT, TIMESTAMP, Boolean, Column, Integer, String, Text, func
from sqlalchemy.orm import mapped_column, relationship


class UserAuth(Base):
    __tablename__ = "user_auth"
    user_id = mapped_column(Integer, primary_key=True, index=True)
    user_name = mapped_column(String(64), nullable=False)
    password = mapped_column(String(73), nullable=False)
    created_on = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    is_deleted = mapped_column(Boolean, default=False)
    bio = mapped_column(Text, nullable=True)
    friend_code = mapped_column(String(4), unique=True, nullable=False)

    # Relationships
    messages_sender = relationship("Messages", back_populates="sender")
    direct_messages = relationship("DirectMessages", back_populates="reciever")
    groups_created = relationship("GroupInfo", back_populates="creator")
