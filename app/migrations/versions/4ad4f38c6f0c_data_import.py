"""data import

Revision ID: 4ad4f38c6f0c
Revises: eab55a90bde6
Create Date: 2024-10-07 15:27:09.222771

"""
import pandas as pd
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ad4f38c6f0c'
down_revision = 'eab55a90bde6'
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData() 
    acronyms = sa.Table('acronyms', meta, autoload_with=op.get_bind())

    df_acronyms = pd.read_csv('main_acronyms_df_rated_cleaned.csv', dtype=str, na_filter=False)
    df_acronyms = df_acronyms.rename(columns={
        'Abbreviation': 'abbreviation',
        'Definition': 'definition',
        'URL': 'url',
        'Info': 'description'
        })
    df_acronyms = df_acronyms[['abbreviation', 'definition', 'url', 'description']]
    df_acronyms = df_acronyms.where(pd.notnull(df_acronyms), None)

    acronyms_to_insert = df_acronyms.to_dict(orient='records')
    op.bulk_insert(acronyms, acronyms_to_insert)


def downgrade(): 
    meta = sa.MetaData()
    acronyms = sa.Table('acronyms', meta, autoload_with=op.get_bind())

    df_acronyms = pd.read_csv('main_acronyms_df_rated_cleaned.csv', dtype=str, na_filter=False)
    df_acronyms = df_acronyms.rename(columns={
        'Abbreviation': 'abbreviation',
        'Definition': 'definition',
        'URL': 'url',
        'Info': 'description'
    })
    df_acronyms = df_acronyms[['abbreviation', 'definition', 'url', 'description']]
    df_acronyms = df_acronyms.where(pd.notnull(df_acronyms), None)


    acronyms_to_delete = df_acronyms.to_dict(orient='records')

    for acronym in acronyms_to_delete:
        op.execute(
            acronyms.delete().where(
                (acronyms.c.abbreviation == acronym['abbreviation']) 
            )
        )