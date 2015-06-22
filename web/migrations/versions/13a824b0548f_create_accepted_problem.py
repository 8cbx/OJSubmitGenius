"""create Accepted_Problem

Revision ID: 13a824b0548f
Revises: 286ae72ba518
Create Date: 2015-06-22 16:34:32.797090

"""

# revision identifiers, used by Alembic.
revision = '13a824b0548f'
down_revision = '286ae72ba518'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AC_problems',
    sa.Column('problems_SID', sa.Integer(), nullable=False),
    sa.Column('AC_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['problems_SID'], ['problems.SID'], ),
    sa.PrimaryKeyConstraint('problems_SID')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('AC_problems')
    ### end Alembic commands ###
