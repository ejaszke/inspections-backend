"""empty message

Revision ID: fe2cf1f4845e
Revises: 51e2c29ad95
Create Date: 2020-10-28 17:17:14.903959

"""

# revision identifiers, used by Alembic.
revision = 'fe2cf1f4845e'
down_revision = '51e2c29ad95'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inspections',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('street', sa.String(length=300), nullable=True),
    sa.Column('street_number', sa.String(length=10), nullable=True),
    sa.Column('staircases', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inspection_confirmations',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('inspection_id', sa.String(length=36), nullable=False),
    sa.Column('answer', sa.String(length=300), nullable=True),
    sa.Column('additional_notes', sa.String(length=300), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['inspection_id'], ['inspections.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inspection_times',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('inspection_id', sa.String(length=36), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['inspection_id'], ['inspections.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inspection_times')
    op.drop_table('inspection_confirmations')
    op.drop_table('inspections')
    # ### end Alembic commands ###