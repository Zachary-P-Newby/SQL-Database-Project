import sqlite3

#Create Connection and cursor
def create_connection_and_cursor():
    connection = sqlite3.connect("..\databases\chinook.db")
    cursor = connection.cursor()
    return connection, cursor

#Close Connection
def end_connection(connection):
    connection.close()
    #print("Connection Closed")

def search_rowID(table,id):
    con, cur = create_connection_and_cursor()
    cur.execute(f"SELECT rowid, * FROM {table} WHERE rowid == {id}")
    result = cur.fetchone()
    end_connection(con)
    return result

def get_column(table,column):
    con, cur = create_connection_and_cursor()
    cur.execute(f"SELECT rowid, {column} FROM {table}")
    results = cur.fetchall()
    end_connection(con)
    return results

def search_column_by_attribute(table,column,attribute,):
    con, cur = create_connection_and_cursor()
    cur.execute(f"SELECT rowid, * FROM {table} WHERE {column} LIKE '%{attribute}%'")
    results = cur.fetchall()
    end_connection(con)
    return results

def display_results(results):
    for result in results:
        print(result)