import sqlite3

connection = sqlite3.connect("..\databases\\testDatabase.db")
cursor = connection.cursor()

#cursor.execute("""CREATE TABLE test (
#                id INTEGER PRIMARY KEY,
#                info TEXT,
#                sublist TEXT
#);""")
#
#(3,"Jay","Bluejay|Hoojay|Ninja")
#cursor.execute(""" INSERT INTO test VALUES (?,?,?)""",(2,"Banana","Blob|Slob"))
    
#data = [
#    (4,"Todd","Ole"),
#    (5,"Mel","Mel|Minion"),
#    (6,"Good person","Corey|Ten|Boom"),
#    (7,"Tracy","Rundle|Tracy"),
#    (8,"Pappy","Pappy|O.|Daniels"),    
#    (9,"Who","whosit"),
#    (10,"What","Whatsit"),
#    (11,"Where","Waluigi|WAH|wah."),
#    (12,"Eevee Family","Eevee|Flareon|Jolteon|Vaporeon|Umbreon|Espeon|Glaceon|Leafeon|Sylveon"),
#    (13,"Iskall85","There|Must|Be|20|Ways|To|Fail|In|Minecraft")]
##
#
##
#cursor.executemany("INSERT INTO test VALUES (?,?,?)", data)
#
#cursor.execute("SELECT rowid, * FROM test")
#
#print(cursor.fetchall())
#cursor.execute("""CREATE TABLE blobby (
#            id INTEGER PRIMARY KEY,
#            data BLOB
#);""")

#cursor.execute("""INSER INTO blobby""")
cursor.execute("""SELECT * FROM test WHERE sublist LIKE '%Umbreon%' """)
print(cursor.fetchall())
print("Great Success")
connection.commit()
connection.close()











#connection.close()