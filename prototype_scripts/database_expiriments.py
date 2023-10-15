import sqlite3

#Connect ot database
con = sqlite3.connect("..\databases\customer.db")
print("Connected")
#create a cursor
cur = con.cursor()
print("Created Cursor")

#create a table
#cur.execute("""CREATE TABLE customers (
#            first_name text,
#            last_name text,
#            email text
#)""")
#
#many_customers = [
#    ("Barry", "Steakfries", "bs@halfbrick.com"), 
#    ("Mario", "Mario", "mario@smbplumbing.com"), 
#    ("Miles", "Prowers", "fixitfox@ringmail.com"),
#    ("Bill", "Mauer", "billm@kaizen.net"),
#    ("Luigi", "Mario", "superluigi@outlook.com"),
#    ("Bunsen", "Honeydew", "drhoneydew@muppetlabs.com"),
#    ("Beaker", "???", "beaker@muppetlabs.com"),
#    ("Phil", "Swift", "philswift@flex.org"),
#    ("Jacob", "Newby", "tanukijen@outlook.com")]
#
#

#cur.execute("""ALTER TABLE customers ADD COLUMN textDump TEXT""")
#text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Urna molestie at elementum eu facilisis. Et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque. Elementum facilisis leo vel fringilla est. Massa sapien faucibus et molestie ac feugiat. Vehicula ipsum a arcu cursus vitae congue mauris. Maecenas pharetra convallis posuere morbi leo. Ipsum dolor sit amet consectetur adipiscing elit. Pretium vulputate sapien nec sagittis. Quam pellentesque nec nam aliquam sem et tortor consequat. Eget dolor morbi non arcu risus. At elementum eu facilisis sed odio. Quis ipsum suspendisse ultrices gravida. Consequat mauris nunc congue nisi vitae suscipit tellus. Et ligula ullamcorper malesuada proin libero. Porttitor lacus luctus accumsan tortor. Adipiscing elit pellentesque habitant morbi tristique. Sit amet consectetur adipiscing elit duis tristique."
text = "Viente"
cur.execute("UPDATE customers SET textDump = '{text}' WHERE rowid = 1", text)

#cur.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
#cur.execute("INSERT INTO customers VALUES ('Zach', 'Newby', 'zpnewby@outlook.com')")
#cur.execute("INSERT INTO customers VALUES ('Jon', 'Arbuckle', 'polkaJon@geekmail.com')")
#cur.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
print("\n"*3)

#cur.execute("""
#UPDATE customers SET last_name = 'Thingy' WHERE first_name = 'Beaker'
#""")
#cur.execute("SELECT rowid, * FROM customers WHERE email NOT LIKE '%.com'")
#cur.execute("SELECT rowid, * FROM customers WHERE rowid %2 != 0")
#cur.execute("SELECT rowid, * FROM customers WHERE rowid %2 != 0 ORDER BY rowid DESC LIMIT 6")
#print(cur.fetchone()[0])
#cur.fetchmany(3)
#print(cur.fetchmany(6))
#print(cur.fetchall())

items = cur.fetchone()

#for item in items:
    #print(item[0] + " " + item[1] + "\t" + item[2])

print(items)

con.commit()
print("")
#input()
#Close COnnection
con.close()
#Sqlite Datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB