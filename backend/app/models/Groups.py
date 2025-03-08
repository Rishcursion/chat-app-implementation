import datetime

from sqlalchemy import (
    CHAR,
    TIMESTAMP,
    VARCHAR,
    Boolean,
    ForeignKey,
    Integer,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class GroupInfo(Base):
    # Metadata
    __tablename__ = "group_info"
    # Table Attributes
    group_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_by: Mapped[int] = mapped_column(
        Integer, ForeignKey("user_auth.user_id"), nullable=False
    )
    created_on: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    last_active: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=True)
    invite_code: Mapped[str] = mapped_column(CHAR(6), unique=True, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    group_name: Mapped[str] = mapped_column(Text, nullable=False)
    member_count: Mapped[int] = mapped_column(Integer, default=1)
    isprivate: Mapped[bool] = mapped_column(Boolean, default=True)
    isdeleted: Mapped[bool] = mapped_column(Boolean, default=False)
    # Relationships
    info_to_user = relationship("UserAuth", back_populates="user_to_info")
    group_to_members = relationship("GroupMembers", back_populates="members_to_groups")
    group_to_group_messages = relationship(
        "GroupMessages", back_populates="group_messages_to_group"
    )


class GroupMembers(Base):
    # Metadata
    __tablename__ = "group_members"
    # Table Attributes
    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("group_info.group_id"), nullable=False, primary_key=True
    )
    member_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user_auth.user_id"), nullable=False, primary_key=True
    )
    role: Mapped[str] = mapped_column(VARCHAR(5), nullable=False)
    # Relationships
    members_to_users = relationship("UserAuth", back_populates="users_to_members")
    members_to_groups = relationship("GroupInfo", back_populates="group_to_members")
