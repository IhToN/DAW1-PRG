"""
    Buscar los usuarios y sus permisos de la base de datos.
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


def show_grants(conn):
    """Sacar un listado de todas las tablas de ClassicModels"""
    cursor = conn.cursor()
    query = "SHOW GRANTS"
    cursor.execute(query)
    print('Lista de Permisos')
    for permiso in cursor:
        print('·', permiso)
    cursor.close()


if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(**config)
        show_grants(cnx)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
