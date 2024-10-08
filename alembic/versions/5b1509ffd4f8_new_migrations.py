"""New migrations

Revision ID: 5b1509ffd4f8
Revises: 
Create Date: 2024-09-04 02:20:47.858163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b1509ffd4f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('popcorns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_on', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('quantity', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_popcorns_create_on'), 'popcorns', ['create_on'], unique=False)
    op.create_index(op.f('ix_popcorns_description'), 'popcorns', ['description'], unique=False)
    op.create_index(op.f('ix_popcorns_id'), 'popcorns', ['id'], unique=False)
    op.create_index(op.f('ix_popcorns_name'), 'popcorns', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_popcorns_name'), table_name='popcorns')
    op.drop_index(op.f('ix_popcorns_id'), table_name='popcorns')
    op.drop_index(op.f('ix_popcorns_description'), table_name='popcorns')
    op.drop_index(op.f('ix_popcorns_create_on'), table_name='popcorns')
    op.drop_table('popcorns')
    # ### end Alembic commands ###
