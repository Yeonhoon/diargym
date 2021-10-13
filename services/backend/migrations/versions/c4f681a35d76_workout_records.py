"""workout records

Revision ID: c4f681a35d76
Revises: aa342a85814a
Create Date: 2021-10-09 15:56:57.629663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4f681a35d76'
down_revision = 'aa342a85814a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('records',
        sa.Column('rid', sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column('ruserid', sa.String(length=20)),
        sa.Column('rdate',sa.Date),
        sa.Column('rlarge', sa.String(length=100), nullable=False),
        sa.Column('rmid', sa.String(length=100), nullable=False),
        sa.Column('rsmall', sa.String(length=100), nullable=False),
        sa.Column('rweight',sa.Float, nullable=True),
        sa.Column('runit', sa.String, nullable=False),
        sa.Column('rrep', sa.Integer, nullable=False)
    )
    op.create_foreign_key(
        constraint_name="uid_fk2",
        source_table='records',
        referent_table='users',
        local_cols=['ruserid'],
        remote_cols=['uid'])


def downgrade():
    op.drop_table('records')
