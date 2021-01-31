# import pandas as pd
# import pyarrow
import sqlalchemy
from sqlalchemy import create_engine


def save_to_parquet(df, path):
    df.to_parquet(path)


def save_to_postgres(df, server, database, username, password, table_name):
    engine = create_engine(f'postgresql://{username}:{password}@{server}/{database}')
    # check if table already exists. A proper solution may truncate this table, insert new data etc
    if engine.has_table(table_name):
        raise Exception("Table already exists")
    else:
        df.to_sql(table_name, engine, dtype={'Comics': sqlalchemy.types.JSON})
