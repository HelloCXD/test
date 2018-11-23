"""empty message

Revision ID: 88c2218762b3
Revises: e9fa0521ab33
Create Date: 2018-11-23 10:17:29.909692

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '88c2218762b3'
down_revision = 'e9fa0521ab33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('pel', sa.Integer(), nullable=True))
    op.drop_index('tel', table_name='user')
    op.create_unique_constraint(None, 'user', ['pel'])
    op.drop_column('user', 'tel')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('tel', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('tel', 'user', ['tel'], unique=True)
    op.drop_column('user', 'pel')
    # ### end Alembic commands ###
