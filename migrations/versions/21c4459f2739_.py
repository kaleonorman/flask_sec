"""empty message

Revision ID: 21c4459f2739
Revises: d0f6f113fe08
Create Date: 2018-03-20 21:48:22.707076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c4459f2739'
down_revision = 'd0f6f113fe08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_constraint(u'user_password_bash_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['password_hash'])
    op.drop_column('user', 'password_bash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_bash', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint(u'user_password_bash_key', 'user', ['password_bash'])
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
