"""records

Revision ID: 6dcd86690d88
Revises: 3eb6a5c55a79
Create Date: 2021-11-10 13:08:00.258107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dcd86690d88'
down_revision = '3eb6a5c55a79'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('records',
        sa.Column('rid', sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column('ruserid', sa.String(length=20)),
        sa.Column('rdate',sa.Date),
        sa.Column('rsmall', sa.String(length=100), nullable=False),
        sa.Column('rweight',sa.Float, nullable=True),
        sa.Column('runit', sa.String, nullable=False),
        sa.Column('rrep', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('rid')
    )

    op.create_foreign_key(
        constraint_name="uid_fk2",
        source_table='records',
        referent_table='users',
        local_cols=['ruserid'],
        remote_cols=['uid'])


def downgrade():
    op.drop_table('records')
