import Facturacion.Controllers.DBManager as dbm
from Facturacion.Misc import Config
from collections import OrderedDict

class Table:
    def __init__(self, nombre):
        self.nombre = nombre
        self.columnas = OrderedDict()

    def add_column(self, columna, parametros):
        self.columnas[columna] = parametros

    def __repr__(self):
        query = 'CREATE TABLE IF NOT EXISTS {} ('.format(self.nombre)
        for columna in self.columnas:
            query += '{} {}, '.format(columna, self.columnas[columna])
        query = query[:-2] + ');'
        return query


class Creator:
    def __init__(self):
        self.tablas = []
        self.init_tables()

    def init_tables(self):
        self.tablas.append(self.clients())
        self.tablas.append(self.vendors())
        self.tablas.append(self.bills())
        self.tablas.append(self.items())
        self.tablas.append(self.itemlines())

    def clients(self):
        table = Table('Clients')
        table.add_column('cif', 'VARCHAR(9) PRIMARY KEY')
        table.add_column('nombre', 'VARCHAR(255)')
        table.add_column('apellido1', 'VARCHAR(255)')
        table.add_column('apellido2', 'VARCHAR(255)')
        table.add_column('direccion', 'VARCHAR(255)')
        table.add_column('cod_postal', 'INT')
        table.add_column('ciudad', 'VARCHAR(255)')
        return table

    def vendors(self):
        table = Table('Vendors')
        table.add_column('cif', 'VARCHAR(9) PRIMARY KEY')
        table.add_column('nombre', 'VARCHAR(255)')
        table.add_column('apellido1', 'VARCHAR(255)')
        table.add_column('apellido2', 'VARCHAR(255)')
        table.add_column('direccion', 'VARCHAR(255)')
        table.add_column('cod_postal', 'INT')
        table.add_column('ciudad', 'VARCHAR(255)')
        return table

    def bills(self):
        table = Table('Bills')
        table.add_column('cod_factura', 'INT PRIMARY KEY')
        table.add_column('vendedor', 'VARCHAR(9)')
        table.add_column('cliente', 'VARCHAR(9)')
        return table

    def items(self):
        table = Table('Items')
        table.add_column('cod_articulo', 'INT PRIMARY KEY')
        table.add_column('nombre', 'VARCHAR(255)')
        table.add_column('precio', 'FLOAT')
        return table

    def itemlines(self):
        table = Table('ItemLines')
        table.add_column('cod_factura', 'INT')
        table.add_column('cod_articulo', 'INT')
        table.add_column('cantidad', 'INT')
        return table

    def create_db(self, test=True):
        with dbm.DB(Config.database) as db:
            for tabla in self.tablas:
                if test:
                    print(tabla)
                else:
                    db.execute(repr(tabla))
