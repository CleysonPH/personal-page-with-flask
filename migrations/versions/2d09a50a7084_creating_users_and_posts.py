"""Creating Users and Posts

Revision ID: 2d09a50a7084
Revises: 
Create Date: 2019-02-11 00:57:55.093320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d09a50a7084'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=120), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('certification_link', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('courses')
    # ### end Alembic commands ###
