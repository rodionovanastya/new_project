"""Третий коммит

Revision ID: 9db6053366ed
Revises: ab8a78285404
Create Date: 2025-06-30 01:45:04.659102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9db6053366ed'
down_revision: Union[str, Sequence[str], None] = 'ab8a78285404'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('fullname', sa.VARCHAR(length=129), nullable=True),
    sa.Column('username', sa.VARCHAR(length=32), nullable=True),
    sa.Column('locale', sa.VARCHAR(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
