"""empty message

Revision ID: e9fa0521ab33
Revises: 6ec2795cdff4
Create Date: 2018-11-23 10:15:46.964063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9fa0521ab33'
down_revision = '6ec2795cdff4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tel', sa.Integer(), nullable=True),
    sa.Column('mail', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('token', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tel')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
