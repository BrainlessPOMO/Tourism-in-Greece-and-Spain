import sqlite3 as sql

connection = sql.connect('webpageInfo.db')

c = connection.cursor()

#how to show info
c.execute("select * from nights_tour")
print(str(c.fetchall()) + '\n')
c.execute("select * from arrivals_tour")
print(str(c.fetchall()) + '\n')
c.execute("select * from nights_non_residents")
print(str(c.fetchall()) + '\n')
c.execute("select * from arrivals_non_residents")
print(str(c.fetchall()) + '\n')

connection.close()