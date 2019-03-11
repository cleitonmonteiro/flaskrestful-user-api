"""empty message

Revision ID: 30ad5e661ffc
Revises: 
Create Date: 2019-03-11 12:24:02.702895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30ad5e661ffc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('criterions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('init_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('contact_email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('submissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('note', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('reponsible_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('trail_description', sa.String(), nullable=True),
    sa.Column('subarea', sa.String(), nullable=True),
    sa.Column('init_date_submission', sa.Date(), nullable=True),
    sa.Column('end_date_submission', sa.Date(), nullable=True),
    sa.Column('number_measurer', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('institution', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('born_date', sa.Date(), nullable=True),
    sa.Column('sex', sa.String(length=1), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('user_type', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('trails')
    op.drop_table('submissions')
    op.drop_table('events')
    op.drop_table('criterions')
    # ### end Alembic commands ###