"""
    Vamos a jugar con MySQL-connector.
        Sacar un listado de todas las tablas de ClassicModels
        Imprimir los clientes que son de un país
        Query que de todos los pedidos de un cliente - mostrar Orders(orderNumber), products(productCode, productName), orderdetails(quantityOrdered, priceEeach)
            Sacar un listado de todos los pedidos de un cliente, con el total de lineas, de pedidos y en total.
    
    Ahora toca hacer algo más curioso.
        Producir una lista con los pedidos de un cliente, con su fecha y su cuantía, comprobando si el cliente
            está al corriente de sus pagos o no.
        Procesar toda la lista de clientes para el conjunto de clientes de una lista.
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
    print('\nLista de tablas')
    for (tabla,) in cursor:
        print('·', tabla)
    cursor.close()


def show_clients_from(conn, country='Spain'):
    """Imprimir los clientes que son de un país"""
    cursor = conn.cursor()
    query = """SELECT C.customerNumber, C.customerName, C.phone, C.city , C.country
    FROM customers C WHERE C.country='{}'""".format(country)
    cursor.execute(query)
    print('\nClientes de', country)
    for cliente in cursor:
        print('·', cliente)
    cursor.close()


def show_client_buyouts(conn, clientid, print_info=False):
    """ Query que de todos los pedidos de un cliente - mostrar Orders(orderNumber), products(productCode, productName), orderdetails(quantityOrdered, priceEeach)
            Sacar un listado de todos los pedidos de un cliente, con el total de lineas y de pedidos.
    """
    cursor = conn.cursor()

    query = """SELECT O.orderNumber, OD.orderLineNumber, P.productCode, P.productName, OD.quantityOrdered, OD.priceEach 
    FROM orders O, products P, orderdetails OD
    WHERE O.orderNumber = OD.orderNumber AND OD.productCode = P.productCode
    AND O.customerNumber = {}
    ORDER BY O.orderNumber, OD.orderLineNumber""".format(clientid)
    subtotal = """SELECT OD.orderNumber, SUM(OD.priceEach * OD.quantityOrdered) FROM orderdetails OD, orders o
    WHERE OD.orderNumber = O.orderNumber AND O.customerNumber = {}
    GROUP BY OD.orderNumber""".format(clientid)

    if print_info:
        cursor.execute(query)
        print('\nCompras del cliente', clientid)
        # '(orderNumber, orderLineNumber, productCode, productName, quantityOrdered, priceEach)')
        for compra in cursor:
            print("· Pedido: {}\n· Linea de Pedido: {}\n· Código de Producto: {}\n· Nombre de Producto: {}\n· Cantidad "
                  "Comprada: {}\n· Precio por Unidad: {}\n".format(*compra))

    cursor.execute(subtotal)

    total = 0
    for precio in cursor:
        if print_info:
            print("· Pedido: {}     · Subtotal: {}".format(*precio))
        total += precio[1]
    if print_info:
        print("· Monto total: {}".format(total))
    cursor.close()

    return total


def show_client_payments(conn, clientid, print_info=False):
    """ Producir una lista con los pedidos de un cliente, con su fecha y su cuantía, comprobando
    si el cliente está al corriente de sus pagos o no.
    """
    cursor = conn.cursor()
    total_deuda = show_client_buyouts(conn, clientid, True)
    total_pagado = 0

    query = """SELECT P.paymentDate, P.amount 
        FROM payments P
        WHERE P.customerNumber = {}
        ORDER BY P.paymentDate""".format(clientid)

    cursor.execute(query)
    if print_info: print('\nPagos del cliente', clientid)
    # '(orderNumber, orderLineNumber, productCode, productName, quantityOrdered, priceEach)')
    for pago in cursor:
        if print_info: print("· Fecha: {}\n· Cantidad: {}\n".format(*pago))
        total_pagado += pago[1]

    cursor.close()

    if total_pagado < total_deuda:
        print("\033[91m\nEl cliente {} tiene una deuda de {} euros.\033[99m".format(clientid, total_deuda - total_pagado))
    else:
        print("\033[92m\nLas cuentas del cliente {} están saneadas.\033[99m".format(clientid))
    return total_pagado < total_deuda


def show_clients_payments(conn, clients=None):
    """ Procesar toda la lista de clientes para el conjunto de clientes de una lista.
    Si la lista original está vacía lo hará para todos los clientes de la base de datos.
    """
    if not clients:
        clients = []
        cursor = conn.cursor()
        query = "SELECT C.customerNumber FROM customers C"
        cursor.execute(query)
        for client in cursor:
            clients.append(client[0])
        cursor.close()

    for client in clients:
        print("\033[94m\n------ Cuentas del cliente {} ------\033[99m".format(client))
        show_client_payments(conn, client)


if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(**config)
        show_tables(cnx)
        #show_clients_from(cnx, 'Spain')
        show_client_payments(cnx, 450, True)
        #show_clients_payments(cnx)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
