"""
    Vamos a jugar con MySQL-connector.
        Sacar un listado de todas las tablas de ClassicModels
        Imprimir los clientes que son de un país
        Query que de todos los pedidos de un cliente - mostrar Orders(orderNumber), products(productCode, productName), orderdetails(quantityOrdered, priceEeach)
            Sacar un listado de todos los pedidos de un cliente, con el total de lineas, de pedidos y en total.
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
    """Sacar un listado de todas las tablas de ClassicModels"""
    cursor = conn.cursor()
    query = "SHOW TABLES"
    cursor.execute(query)
    print('Lista de tablas')
    for (tabla,) in cursor:
        print('·', tabla)
    cursor.close()


def show_clients_from(conn, country='Spain'):
    """Imprimir los clientes que son de un país"""
    cursor = conn.cursor()
    query = """SELECT C.customerNumber, C.customerName, C.phone, C.city , C.country
    FROM customers C WHERE C.country='{}'""".format(country)
    cursor.execute(query)
    print('Clientes de', country)
    for cliente in cursor:
        print('·', cliente)
    cursor.close()


def show_clients_buyouts(conn, clientid):
    """Query que de todos los pedidos de un cliente - mostrar Orders(orderNumber), products(productCode, productName), orderdetails(quantityOrdered, priceEeach)
            Sacar un listado de todos los pedidos de un cliente, con el total de lineas y de pedidos."""
    cursor = conn.cursor()
    query = """SELECT O.orderNumber, P.productCode, P.productName, OD.quantityOrdered, OD.priceEach, 
    (SELECT COUNT(*) FROM orders WHERE orders.customerNumber = {}) as Compras,
    (SELECT COUNT(*) FROM orderdetails, orders WHERE orderdetails.orderNumber = orders.orderNumber AND orders.customerNumber = {}) as Lineas
    FROM orders O, products P, orderdetails OD
    WHERE O.orderNumber = OD.orderNumber AND OD.productCode = P.productCode
    AND O.customerNumber = {}""".format(clientid, clientid, clientid)
    cursor.execute(query)
    print('Compras del cliente ', clientid)
    print('·', '(orderNumber, productCode, productName, quantityOrdered, priceEach, Compras, Lineas)')
    for compra in cursor:
        print('·', compra)
    cursor.close()


if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(**config)
        show_tables(cnx)
        show_clients_from(cnx, 'Spain')
        show_clients_buyouts(cnx, 103)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
