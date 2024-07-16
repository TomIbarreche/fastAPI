"""add content column to posts table

Revision ID: 52e1587d3daa
Revises: 8e723b354f45
Create Date: 2024-07-16 12:06:59.436677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52e1587d3daa'
down_revision: Union[str, None] = '8e723b354f45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
