"""lighting_type

Revision ID: 32179c948ef9
Revises: 
Create Date: 2022-08-17 15:39:51.703757

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '32179c948ef9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lighting_type',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('UUID', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('watt', sa.Integer(), nullable=True),
    sa.Column('connection_type', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('UUID')
    )
    op.create_index(op.f('ix_lighting_type_id'), 'lighting_type', ['id'], unique=True)
    op.create_table('lighting',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('UUID', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('lighting_type', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['lighting_type'], ['lighting_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('UUID')
    )
    op.create_index(op.f('ix_lighting_id'), 'lighting', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_lighting_id'), table_name='lighting')
    op.drop_table('lighting')
    op.drop_index(op.f('ix_lighting_type_id'), table_name='lighting_type')
    op.drop_table('lighting_type')
    # ### end Alembic commands ###