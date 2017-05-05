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

    query = """SELECT O.orderNumber, OD.orderLineNumber, P.productCode, P.productName, OD.quantityOrdered, OD.priceEach 
    FROM orders O, products P, orderdetails OD
    WHERE O.orderNumber = OD.orderNumber AND OD.productCode = P.productCode
    AND O.customerNumber = {}
    ORDER BY O.orderNumber, OD.orderLineNumber""".format(clientid)
    subtotal = """SELECT OD.orderNumber, OD.priceEach * OD.quantityOrdered FROM orderdetails OD, orders o
    WHERE OD.orderNumber = O.orderNumber AND O.customerNumber = {}
    GROUP BY OD.orderNumber""".format(clientid)

    cursor.execute(query)
    print('Compras del cliente', clientid)
    # '(orderNumber, orderLineNumber, productCode, productName, quantityOrdered, priceEach)')
    for compra in cursor:
        print("· Pedido: {}\n· Linea de Pedido: {}\n· Código de Producto: {}\n· Nombre de Producto: {}\n· Cantidad "
              "Comprada: {}\n· Precio por Unidad: {}\n".format(*compra))
    cursor.execute(subtotal)

    total = 0
    for precio in cursor:
        print("· Pedido: {}     · Subtotal: {}".format(*precio))
        total += precio[1]
    print("· Monto total: {}".format(total))
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
