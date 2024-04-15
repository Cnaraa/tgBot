import pandas as pd
import sqlite3


def conversion_to_df():
    with sqlite3.Connection('./db/realty.db') as connection:
      cursor = connection.cursor()
      sql_query = 'SELECT * FROM offers'
      df = pd.read_sql_query(sql_query, connection)
    return df