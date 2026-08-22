"""add user table

Revision ID: 8c30ccbee505
Revises: 564094e273ee
Create Date: 2026-08-22 00:24:29.721430

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c30ccbee505'
down_revision: Union[str, Sequence[str], None] = '564094e273ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
