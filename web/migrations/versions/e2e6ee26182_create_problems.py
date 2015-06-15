"""create problems

Revision ID: e2e6ee26182
Revises: 42923dd2659
Create Date: 2015-06-15 21:17:14.089458

"""

# revision identifiers, used by Alembic.
revision = 'e2e6ee26182'
down_revision = '42923dd2659'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('problem',
    sa.Column('OJ_ID', sa.String(length=64), nullable=True),
    sa.Column('SID', sa.Integer(), nullable=False),
    sa.Column('PID', sa.Integer(), nullable=True),
    sa.Column('LastUpdate', sa.DateTime(), nullable=True),
    sa.Column('Title', sa.String(length=128), nullable=True),
    sa.Column('Total_Submissions', sa.Integer(), nullable=True),
    sa.Column('Accepted', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('SID')
    )
    op.create_index(op.f('ix_problem_LastUpdate'), 'problem', ['LastUpdate'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_problem_LastUpdate'), table_name='problem')
    op.drop_table('problem')
    ### end Alembic commands ###
