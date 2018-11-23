"""empty message

Revision ID: 77876afc5ecf
Revises: 
Create Date: 2018-11-23 09:24:53.331135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77876afc5ecf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('bannerid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('bannerid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
