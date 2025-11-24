"""add content column to posts tables

Revision ID: c0a5b01f2e3e
Revises: 4fc0ed62c754
Create Date: 2025-11-23 18:55:52.794395

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0a5b01f2e3e'
down_revision: Union[str, Sequence[str], None] = '4fc0ed62c754'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass