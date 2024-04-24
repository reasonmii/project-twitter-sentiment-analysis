import pandas as pd
from sqlalchemy import create_engine
from mysql.connector import connection
from mysql.connector import Error
import os

creds_local = {'usr': 'root',
               'pwd': 'root1234',
               'hst': '127.0.0.1',
               'prt': 3306,
               'dbn': 'twitter'}

creds_aws = {'usr': 'admin',
             'pwd': 'admin123',
             'hst': 'twitter.co5nbj021rcu.us-east-1.rds.amazonaws.com',
             'prt': 3306,
             'dbn': 'twitter'}

creds_mysql_conn = {'user': 'admin',
                     'password': 'admin123',
                     'host': 'twitter.co5nbj021rcu.us-east-1.rds.amazonaws.com',
                     'database': 'twitter'}


def csv_to_sql(filename, creds, table_name):
    connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'  # MySQL connection string.
    engine = create_engine(connstr.format(**creds))  # Create sqlalchemy engine

    df = pd.read_csv('data_all/'+filename, index_col=False, low_memory=False)
    df = df.iloc[:, 1:]

    df.to_sql(name=table_name, con=engine, if_exists='append', chunksize=500)
    print('Completed: '+filename)


def sql_export(creds, query):
    connstr = 'mysql+mysqlconnector://{usr}:{pwd}@{hst}:{prt}/{dbn}'  # MySQL connection string.
    engine = create_engine(connstr.format(**creds))  # Create sqlalchemy engine

    df = pd.read_sql(sql=query, con=engine)
    return df


def mysql_connector_execute(creds, query, commit=False):
    try:
        conn = connection.MySQLConnection(**creds)
        cursor = conn.cursor()
        cursor.execute(query)
        print('query executed')
        if commit is True:
            conn.commit()
    except Error as e:
        print(e)
        return None

      
#Samples
# Upload data
filelist = os.listdir('data_all')
# for f in filelist:
    # csv_to_sql(f, creds_aws, 'data_all')


# Fetch data by SQL query
query_1 = '''select * from ukraine 
    WHERE language = 'en' 
    AND tweetcreatedts > '2022-08-08' 
    AND hashtags LIKE '%Putin%' 
    LIMIT 500'''
data = sql_export(creds_aws, query_1)
print(len(data))


# Execute SQL query in database
query_2 = "SELECT * FROM ukraine LIMIT 1000"
mysql_connector_execute(creds_mysql_conn, query_2)
