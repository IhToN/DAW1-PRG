import mysql.connector

cnxConfig = {
    'user': 'root',
    'password': '159753',
    'host': '127.0.0.1',
    'database': 'classicmodels',
    'raise_on_warnings': True,
}


class ControlBD:
    def __init__(self, auto_initialize=True):
        self.cnx = None
        if auto_initialize:
            self.conectar()

    def conectar(self, config=cnxConfig):
        try:
            self.cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cnx.close()

    def descoenctar(self):
        self.cnx.close()
        self.cnx = None

    def insertar_cliente(self, cliente):
        cursor = self.cnx.cursor()

        query = """INSERT INTO customers(customerNumber, customerName, phone, addressLine1, city)
                    VALUES ({}, {}, {}, {}, {})""".format(cliente.ncliente, cliente.nombre, cliente.telefono,
                                                          cliente.direccion, cliente.ciudad)
        try:
            cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print('Error en la inserción de un nuevo cliente:', err)
        finally:
            cursor.close()

    def obtener_clientes(self):
        cursor = self.cnx.cursor()

        query = """SELECT customerNumber, customerName, phone, addressLine1, city FROM customers"""
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print('Error en la inserción de un nuevo cliente:', err)
        finally:
            return cursor
