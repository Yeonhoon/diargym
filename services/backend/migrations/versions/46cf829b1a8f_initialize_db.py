"""initialize db

Revision ID: 46cf829b1a8f
Revises: 
Create Date: 2021-10-05 16:19:50.954925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46cf829b1a8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('uid', sa.String(length=20), nullable=False, index=True),
                    sa.Column('uname', sa.String(length=20), nullable=False),
                    sa.Column('uemail',sa.String(length=30), nullable=False),
                    sa.Column('upw',sa.String(length=300), nullable=False),
                    sa.PrimaryKeyConstraint('uid'))



def downgrade():
    pass
