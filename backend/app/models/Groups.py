from db import Base
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey, Integer, String, Text, func, null
from sqlalchemy.orm import Mapped, mapped_column, relationship


class GroupInfo(Base):
    __tablename__ = "group_info"
    group_id = mapped_column(Integer, primary_key=True)
    created_by = mapped_column(Integer, ForeignKey("user_auth.user_id"), nullable=False)
    created_on = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_active = mapped_column(TIMESTAMP, nullable=True)
    invite_code = mapped_column(Text, nullable=True)
    description = mapped_column(Text, nullable=True)
    group_name = mapped_column(Text, nullable=False)
    member_count = mapped_column(Integer, default=1)
    isprivate = mapped_column(Boolean, default=True)
    isdeleted = mapped_column(Boolean, default=False)

    # Relationships
    creator = relationship("UserAuth", back_populates="groups_created")
    group_messages = relationship("GroupMessages", back_populates="group")


class GroupMember(Base):
    __tablename__ = "group_members"
    group_id = mapped_column(
        Integer, ForeignKey("group_info.group_id"), primary_key=True
    )
    member_id = mapped_column(
        Integer, ForeignKey("user_auth.user_id"), primary_key=True
    )
    member_role = mapped_column(String(5), nullable=False)

    # Relationships
    group = relationship("GroupInfo")
    user = relationship("UserAuth")
