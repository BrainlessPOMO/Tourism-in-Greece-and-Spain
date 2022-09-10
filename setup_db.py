import sqlite3 as sql
from os.path import exists as file_exists


def main():
    if file_exists('webpageInfo.db') == True:
        return 0

    connection = sql.connect('webpageInfo.db')

    c = connection.cursor()

    # setup table for Nights spent at tourist accommodation establishments - monthly data
    c.execute("""CREATE TABLE IF NOT EXISTS nights_tour (
            country text NOT NULL,
            Y2020M07 text default NULL,
            Y2020M08 text default NULL,
            Y2020M09 text default NULL,
            Y2020M10 text default NULL,
            Y2020M11 text default NULL,
            Y2020M12 text default NULL,
            Y2020M01 text default NULL,
            Y2020M02 text default NULL,
            Y2020M03 text default NULL,
            Y2020M04 text default NULL,
            primary key (country)
          )""")

    # setup table for Nights spent by non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data
    c.execute("""CREATE TABLE IF NOT EXISTS nights_non_residents (
            country text NOT NULL,
            Y2020M03 text default NULL,
            Y2020M04 text default NULL,
            Y2020M05 text default NULL,
            Y2020M06 text default NULL,
            Y2020M07 text default NULL,
            Y2020M08 text default NULL,
            Y2020M09 text default NULL,
            Y2020M10 text default NULL,
            Y2020M11 text default NULL,
            Y2020M12 text default NULL,
            primary key (country)
          )""")

    # setup table for Arrivals at tourist accommodation establishments - monthly data
    c.execute("""CREATE TABLE IF NOT EXISTS arrivals_tour (
            country text NOT NULL,
            Y2020M07 text default NULL,
            Y2020M08 text default NULL,
            Y2020M09 text default NULL,
            Y2020M10 text default NULL,
            Y2020M11 text default NULL,
            Y2020M12 text default NULL,
            Y2020M01 text default NULL,
            Y2020M02 text default NULL,
            Y2020M03 text default NULL,
            Y2020M04 text default NULL,
            primary key (country)
          )""")

    # setup table for Arrivals of non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data
    c.execute("""CREATE TABLE IF NOT EXISTS arrivals_non_residents (
            country text NOT NULL,
            Y2020M03 text default NULL,
            Y2020M04 text default NULL,
            Y2020M05 text default NULL,
            Y2020M06 text default NULL,
            Y2020M07 text default NULL,
            Y2020M08 text default NULL,
            Y2020M09 text default NULL,
            Y2020M10 text default NULL,
            Y2020M11 text default NULL,
            Y2020M12 text default NULL,
            primary key (country)
          )""")

    connection.commit()
    connection.close()

    return 1
