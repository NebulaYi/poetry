"""empty message

Revision ID: 012ba3b33f55
Revises: 377a20da13a4
Create Date: 2024-05-15 10:05:52.154839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '012ba3b33f55'
down_revision = '377a20da13a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('records', sa.Column('functionName', sa.String(length=40), nullable=True))
    op.add_column('users', sa.Column('username', sa.String(length=17), nullable=True))
    op.add_column('users', sa.Column('create_time', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'create_time')
    op.drop_column('users', 'username')
    op.drop_column('records', 'functionName')
    # ### end Alembic commands ###
