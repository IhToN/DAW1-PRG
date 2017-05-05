"""
    Vamos a jugar con MySQL-connector.
        Sacar un listado de todas las tablas de ClassicModels
"""
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '159753',
    'host': '127.0.0.1',
    'database': 'classicmodels',
    'raise_on_warnings': True,
}


def show_tables(conn):
    cursor = conn.cursor()
    query = "SHOW TABLES"
    cursor.execute(query)
    print('Lista de tablas')
    for (tabla,) in cursor:
        print('·', tabla)
    cursor.close()


def show_clients_from(conn, country='Spain'):
    cursor = conn.cursor()
    query = """SELECT C.customerNumber, C.customerName, C.phone, C.city , C.country
    FROM customers C WHERE C.country='{}'""".format(country)
    cursor.execute(query)
    print('Clientes de', country)
    for cliente in cursor:
        print('·', cliente)
    cursor.close()


if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(**config)
        show_tables(cnx)
        show_clients_from(cnx, 'Spain')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
