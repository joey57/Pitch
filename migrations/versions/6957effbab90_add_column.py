"""Add column

Revision ID: 6957effbab90
Revises: 9e67400f72a8
Create Date: 2022-05-06 17:23:38.048079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6957effbab90'
down_revision = '9e67400f72a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
