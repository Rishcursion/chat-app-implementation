"""feat: fixed sqlalchemy models

Revision ID: 4de26ebbbc18
Revises: 3f70e0d0d582
Create Date: 2025-03-09 10:17:28.370545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4de26ebbbc18'
down_revision: Union[str, None] = '3f70e0d0d582'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group_info', 'created_by',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('group_info', 'created_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('group_info', 'member_count',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('1'))
    op.alter_column('group_info', 'isprivate',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('group_info', 'isdeleted',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('group_messages', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_auth', 'friend_code',
               existing_type=postgresql.BYTEA(),
               nullable=False,
               existing_server_default=sa.text('gen_random_bytes(4)'))
    op.alter_column('user_auth', 'created_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('user_auth', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('user_messages', 'sent_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('user_messages', 'reply_to',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('user_messages', 'isdeleted',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('user_messages', 'edited',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.drop_constraint('user_messages_reply_to_fkey', 'user_messages', type_='foreignkey')
    op.create_foreign_key(None, 'user_messages', 'user_auth', ['reply_to'], ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_messages', type_='foreignkey')
    op.create_foreign_key('user_messages_reply_to_fkey', 'user_messages', 'user_messages', ['reply_to'], ['message_id'])
    op.alter_column('user_messages', 'edited',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('user_messages', 'isdeleted',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('user_messages', 'reply_to',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('user_messages', 'sent_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('user_auth', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('user_auth', 'created_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('user_auth', 'friend_code',
               existing_type=postgresql.BYTEA(),
               nullable=True,
               existing_server_default=sa.text('gen_random_bytes(4)'))
    op.alter_column('group_messages', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('group_info', 'isdeleted',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('group_info', 'isprivate',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('group_info', 'member_count',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('1'))
    op.alter_column('group_info', 'created_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('group_info', 'created_by',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
