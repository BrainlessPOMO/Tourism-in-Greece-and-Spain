import pandas as pd
import sqlite3 as sql


def main():
    connection = sql.connect('webpageInfo.db')

    df1 = pd.read_sql_query('SELECT * FROM nights_tour', connection)
    df2 = pd.read_sql_query('SELECT * FROM nights_non_residents', connection)
    df3 = pd.read_sql_query('SELECT * FROM arrivals_tour', connection)
    df4 = pd.read_sql_query('SELECT * FROM arrivals_non_residents', connection)

    connection.close()
    return df1, df2, df3, df4
