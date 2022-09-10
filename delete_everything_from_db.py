import sqlite3 as sql


def main():
    connection = sql.connect('webpageInfo.db')

    c = connection.cursor()

    # delete from nights_tour, table 1
    c.execute("DELETE FROM nights_tour WHERE country ='GREECE'")
    c.execute("DELETE FROM nights_tour WHERE country ='SPAIN'")

    # delete from arrivals_tour, table 2
    c.execute("DELETE FROM arrivals_tour WHERE country ='GREECE'")
    c.execute("DELETE FROM arrivals_tour WHERE country ='SPAIN'")

    # delete from nights_non_residents, table 3
    c.execute("DELETE FROM nights_non_residents WHERE country ='GREECE'")
    c.execute("DELETE FROM nights_non_residents WHERE country ='SPAIN'")

    # delete from arrivals_non_residents, table 4
    c.execute("DELETE FROM arrivals_non_residents WHERE country ='GREECE'")
    c.execute("DELETE FROM arrivals_non_residents WHERE country ='SPAIN'")

    connection.commit()
    connection.close()
