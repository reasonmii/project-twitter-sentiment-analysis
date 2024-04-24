import sqlite3
import os
import pandas

# Assumes your data is stored in a top level directory 
# and that all csvs are unzipped and put into a single directory
DATA_DIR = '../data/'
DB_DIR = 'dbs/'
DB_NAME = 'tweets'
TABLE_NAME = 'raw_tweets'

# Create the Database 
con = sqlite3.connect(f'{DB_DIR}{DB_NAME}.db')
cur = con.cursor()

# If the table already exists drop it and start from scratch
try:
    cur.execute(f"DROP TABLE {TABLE_NAME}")
except Exception as e:
    print(e)
    
# Add each individual dataset csv file's data
for fil in os.listdir(DATA_DIR):
    df = pandas.read_csv(f"{DATA_DIR}{fil}")
    df.drop(columns=['Unnamed: 0'])
    df.to_sql(TABLE_NAME, con, if_exists='append', index=False)




