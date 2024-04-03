"""fix products table

Revision ID: 30610c531812
Revises: f94a24daa23e
Create Date: 2024-04-03 18:13:20.558010

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "30610c531812"
down_revision: Union[str, None] = "f94a24daa23e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "products",
        "slug",
        existing_type=sa.TEXT(),
        type_=sa.String(length=100),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "products",
        "slug",
        existing_type=sa.String(length=100),
        type_=sa.TEXT(),
        nullable=True,
    )
    # ### end Alembic commands ###