import pandas as pd
import sqlite3 as sql
from os.path import exists as file_exists


def main():
    if file_exists('webpageInfo.db') == False:
        return 0
    connection = sql.connect('webpageInfo.db')

    df1 = pd.read_sql_query('SELECT * FROM nights_tour', connection)
    df2 = pd.read_sql_query('SELECT * FROM nights_non_residents', connection)
    df3 = pd.read_sql_query('SELECT * FROM arrivals_tour', connection)
    df4 = pd.read_sql_query('SELECT * FROM arrivals_non_residents', connection)

    # create CSVs
    df1.to_csv(r'csv files/Nights spent at tourist accommodation establishments - monthly data.csv',
               index=False, header=True)
    df2.to_csv(r'csv files/Nights spent by non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data.csv', index=False, header=True)
    df3.to_csv(r'csv files/Arrivals at tourist accommodation establishments - monthly data.csv',
               index=False, header=True)
    df4.to_csv(r'csv files/Arrivals of non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data.csv', index=False, header=True)

    connection.close()
    return 1
