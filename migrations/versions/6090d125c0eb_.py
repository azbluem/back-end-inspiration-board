"""empty message

Revision ID: 6090d125c0eb
Revises: 9c2454f722e1
Create Date: 2023-01-03 10:53:29.190014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6090d125c0eb'
down_revision = '9c2454f722e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('board_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'card', 'board', ['board_id'], ['board_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.drop_column('card', 'board_id')
    # ### end Alembic commands ###
