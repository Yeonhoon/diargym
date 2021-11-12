"""users

Revision ID: a6db7397f80f
Revises: 
Create Date: 2021-11-10 13:06:59.044070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6db7397f80f'
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
    op.drop_table('users')
