"""empty message

Revision ID: 437ccdfbafc4
Revises: 
Create Date: 2019-11-03 12:35:56.743810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '437ccdfbafc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('image2', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'image2')
    # ### end Alembic commands ###