"""table data

Revision ID: be00673653dc
Revises: fb01cb4bf401
Create Date: 2025-01-23 17:06:21.916828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be00673653dc'
down_revision: Union[str, None] = 'fb01cb4bf401'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        'satellites',
        'epoch',
        existing_type=sa.VARCHAR(),  # Replace with the original type of the column
        type_=sa.DateTime(),
        postgresql_using="epoch::timestamp without time zone"  # Conversion logic
    )

def downgrade():
    op.alter_column(
        'satellites',
        'epoch',
        existing_type=sa.VARCHAR(),
        type_=sa.String()  # Revert to the original type
    )