"""Initial migration

Revision ID: 2d5ccd2f24c2
Revises: 0ce03cd7c5c5
Create Date: 2024-10-30 02:57:59.901605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d5ccd2f24c2'
down_revision: Union[str, None] = '0ce03cd7c5c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
