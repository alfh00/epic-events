"""Employee add ondelete delete contact

Revision ID: c6e919b06fc8
Revises: 892670d6b826
Create Date: 2023-11-11 15:15:23.549426

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6e919b06fc8'
down_revision: Union[str, None] = '892670d6b826'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Employees', sa.Column('contact_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Employees', 'Contacts', ['contact_id'], ['contact_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Employees', type_='foreignkey')
    op.drop_column('Employees', 'contact_id')
    # ### end Alembic commands ###
