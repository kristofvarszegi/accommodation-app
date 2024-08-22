"""Add created_at to Review

Revision ID: 77e6cb01c08e
Revises: cea8b99d3fad
Create Date: 2024-08-22 23:11:08.511958

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "77e6cb01c08e"
down_revision: Union[str, None] = "cea8b99d3fad"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("reviews", sa.Column("created_at", sa.DateTime(), nullable=False))
    op.alter_column(
        "reviews",
        "general_score",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "reviews",
        "general_score",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=True,
    )
    op.drop_column("reviews", "created_at")
    # ### end Alembic commands ###
