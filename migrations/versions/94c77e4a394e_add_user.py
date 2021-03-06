"""add user

Revision ID: 94c77e4a394e
Revises: 
Create Date: 2022-03-27 16:59:36.431928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94c77e4a394e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('firstname', sa.String(length=126), nullable=False),
    sa.Column('lastname', sa.String(length=126), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('iban', sa.String(length=200), nullable=True),
    sa.Column('role', sa.Enum('approver', 'seller', 'buyer', 'admin', name='roletype'), server_default='buyer', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
