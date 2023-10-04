import sqlite3

#Connect ot database
con = sqlite3.connect("customer.db")
print("Connected")
#create a cursor
cur = con.cursor()
print("Created Cursor")

#create a table
cur.execute("""CREATE TABLE customers (
            first_name text,
            last_name text,
            email text,
            address text,
            favourite_food text
)""")
print("Created table")

con.commit()
print("table commited")

#Close COnnection
con.close()
print("CLosed.")
#Sqlite Datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB