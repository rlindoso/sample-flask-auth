"""Create table User

Revision ID: 2acd0f248f1b
Revises: 
Create Date: 2025-02-02 13:15:43.991746

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String


# revision identifiers, used by Alembic.
revision: str = '2acd0f248f1b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
        'users',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('username', String(80), nullable=False, unique=True),
        Column('password', String, nullable=False),
        Column('role',String(80), nullable=False, default='user'),
    )


def downgrade() -> None:
    op.drop_table('users')
