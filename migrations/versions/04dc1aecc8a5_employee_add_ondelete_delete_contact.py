"""Employee add ondelete delete contact

Revision ID: 04dc1aecc8a5
Revises: c6e919b06fc8
Create Date: 2023-11-11 15:31:46.025482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04dc1aecc8a5'
down_revision: Union[str, None] = 'c6e919b06fc8'
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
