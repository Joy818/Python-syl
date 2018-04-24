"""create live table

Revision ID: 1fd41672414a
Revises: ee88e927e8cf
Create Date: 2018-04-22 20:32:25.028729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd41672414a'
down_revision = 'ee88e927e8cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('live',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('liver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['liver_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('live')
    # ### end Alembic commands ###