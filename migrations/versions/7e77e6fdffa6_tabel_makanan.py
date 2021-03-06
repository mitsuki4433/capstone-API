"""tabel makanan

Revision ID: 7e77e6fdffa6
Revises: 8bd641b4aedb
Create Date: 2021-05-09 06:05:56.032274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e77e6fdffa6'
down_revision = '8bd641b4aedb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('makanan',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('kalori', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('makanan')
    # ### end Alembic commands ###
