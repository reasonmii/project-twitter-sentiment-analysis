import sqlite3
import pandas as pd

def get_connection(db):
    con = sqlite3.connect(f"{db}.db")
    return con

def get_table_names(connection):
    cursor = connection.cursor()
    return cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

def basic_look(connection, table_name):
    cursor = connection.cursor()
    result = cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    print('Total Number of Entries: ', result.fetchall())

    df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 10", connection)
    print(df)

    cursor.close()

def generic_query(connection, query_string):
    cursor = connection.cursor()

    return cursor.execute(query_string)








