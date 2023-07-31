import mysql.connector

__cnx = None


def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root1234', database='grocery_store_database')

    return __cnx
