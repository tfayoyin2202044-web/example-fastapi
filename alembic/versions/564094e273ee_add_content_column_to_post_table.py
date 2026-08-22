"""add content column to post table

Revision ID: 564094e273ee
Revises: 95d8dff5814c
Create Date: 2026-08-22 00:09:15.811620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '564094e273ee'
down_revision: Union[str, Sequence[str], None] = '95d8dff5814c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
