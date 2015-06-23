"""change contest

Revision ID: fc684e2ac1
Revises: 95b162124d3
Create Date: 2015-06-23 21:28:56.538924

"""

# revision identifiers, used by Alembic.
revision = 'fc684e2ac1'
down_revision = '95b162124d3'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Add_contests')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Add_contests',
    sa.Column('Manager_ID', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('Contest_ID', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('ADD_time', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['Contest_ID'], [u'contests.id'], name=u'Add_contests_ibfk_1'),
    sa.ForeignKeyConstraint(['Manager_ID'], [u'users.id'], name=u'Add_contests_ibfk_2'),
    sa.PrimaryKeyConstraint('Manager_ID', 'Contest_ID'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
