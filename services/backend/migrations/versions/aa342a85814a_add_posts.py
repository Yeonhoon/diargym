"""add_posts

Revision ID: aa342a85814a
Revises: 46cf829b1a8f
Create Date: 2021-10-05 16:58:20.811797

"""
from sqlalchemy.sql.schema import Constraint
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa342a85814a'
down_revision = '46cf829b1a8f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                   sa.Column('pid', sa.Integer, primary_key=True, index=True),
                   sa.Column('ptitle',sa.String(length=100), nullable=False),
                   sa.Column('pcontent', sa.Text, index=True, nullable=False),
                   sa.Column('author', sa.String(length=20), nullable=False)
                  )
    op.create_foreign_key(
        constraint_name="uid_fk",
        source_table='posts',
        referent_table='users',
        local_cols=['author'],
        remote_cols=['uid'])


def downgrade():
    pass
