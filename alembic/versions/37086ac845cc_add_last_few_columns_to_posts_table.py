"""add last few columns to posts table

Revision ID: 37086ac845cc
Revises: 858c33745bd0
Create Date: 2026-08-22 00:40:05.060368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37086ac845cc'
down_revision: Union[str, Sequence[str], None] = '858c33745bd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
