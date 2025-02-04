"""empty message

Revision ID: 0a03332c6974
Revises: d49216dd81a8
Create Date: 2017-12-21 10:19:46.411670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a03332c6974'
down_revision = 'd49216dd81a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweets', sa.Column('email', sa.String(length=80), nullable=True))
    op.add_column('tweets', sa.Column('profile_photo', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tweets', 'profile_photo')
    op.drop_column('tweets', 'email')
    # ### end Alembic commands ###
