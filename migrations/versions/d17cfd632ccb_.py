"""empty message

Revision ID: d17cfd632ccb
Revises: b3ea808ad928
Create Date: 2018-06-07 11:44:47.904989

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd17cfd632ccb'
down_revision = 'b3ea808ad928'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('showname', sa.String(length=50), nullable=True),
    sa.Column('shownameen', sa.String(length=50), nullable=True),
    sa.Column('director', sa.String(length=20), nullable=True),
    sa.Column('leadingRole', sa.String(length=200), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=20), nullable=True),
    sa.Column('language', sa.String(length=20), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningmodel', sa.String(length=20), nullable=True),
    sa.Column('openday', sa.DateTime(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=200), nullable=True),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('t_movies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_movies',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('showname', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('shownameen', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('director', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('leadingRole', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('type', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('language', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('duration', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('screeningmodel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('openday', mysql.DATETIME(), nullable=True),
    sa.Column('backgroundpicture', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('flag', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('isdelete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('movies')
    # ### end Alembic commands ###
