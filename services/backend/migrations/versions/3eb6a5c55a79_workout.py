"""workout

Revision ID: 3eb6a5c55a79
Revises: a6db7397f80f
Create Date: 2021-11-10 13:07:30.127291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eb6a5c55a79'
down_revision = 'a6db7397f80f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('workout',
            sa.Column('wname', sa.String(length=100), primary_key=True, nullable=False),
            sa.Column('wcategory', sa.String(length=100), nullable=False),
            sa.Column('wtype', sa.String(length=100), nullable=False),
            sa.PrimaryKeyConstraint('wname'))


def downgrade():
    op.drop_table('workout')
