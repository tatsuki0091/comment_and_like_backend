"""empty message

Revision ID: fc388dd585b5
Revises: e7f2c873df70
Create Date: 2021-06-21 16:01:48.643139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc388dd585b5'
down_revision = 'e7f2c873df70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_user_id_key', 'comments', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('comments_user_id_key', 'comments', ['user_id'])
    # ### end Alembic commands ###
