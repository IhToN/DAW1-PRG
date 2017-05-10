import mysql.connector

cnxConfig = {
    'user': 'root',
    'password': '159753',
    'host': '127.0.0.1',
    'database': 'classicmodels',
    'raise_on_warnings': True,
}


def conectar(config=cnxConfig):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
    return cnx


# region Cliente
def insertar_cliente(cliente):
    cnx = conectar()
    cursor = cnx.cursor()

    query = """INSERT INTO customers(customerNumber, customerName, phone, addressLine1, city)
                VALUES ({}, {}, {}, {}, {})""".format(cliente.ncliente, cliente.nombre, cliente.telefono,
                                                      cliente.direccion, cliente.ciudad)
    try:
        cursor.execute(query)
        cnx.commit()
    except mysql.connector.Error as err:
        print('Error en la inserción de un nuevo cliente:', err)
    finally:
        cursor.close()
        cnx.close()


def obtener_clientes():
    cnx = conectar()
    cursor = cnx.cursor()

    query = """SELECT customerNumber, customerName, phone, addressLine1, city FROM customers"""
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print('Error en la inserción de un nuevo cliente:', err)
    finally:
        cnx.close()
        return cursor

# endregion Cliente
