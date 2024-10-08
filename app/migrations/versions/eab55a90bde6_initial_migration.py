"""initial migration

Revision ID: eab55a90bde6
Revises: 
Create Date: 2024-10-04 17:26:51.098320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eab55a90bde6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(): 
    op.create_table('acronyms',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('abbreviation', sa.String(), nullable=False),
    sa.Column('definition', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('abbreviation', 'definition', name='_abbreviation_definition_uc')
    )


def downgrade(): 
    op.drop_table('acronyms')
