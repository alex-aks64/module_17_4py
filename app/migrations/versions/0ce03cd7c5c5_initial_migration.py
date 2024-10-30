"""Initial migration

Revision ID: 0ce03cd7c5c5
Revises: 4e6ff49212c0
Create Date: 2024-10-15 00:30:02.666695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ce03cd7c5c5'
down_revision: Union[str, None] = '4e6ff49212c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('slug', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_slug'), 'users', ['slug'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_slug'), table_name='users')
    op.drop_column('users', 'slug')
    # ### end Alembic commands ###