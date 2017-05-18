import Facturacion.DBManager as dbm
from Facturacion.Misc import Config


class ItemsController:
    def get_items(self):
        with dbm.DB(Config.database) as db:
            query = 'SELECT * FROM Items;'
            return db.execute(query)


class BillsController:
    def get_bills(self):
        with dbm.DB(Config.database) as db:
            query = 'SELECT * FROM Bills;'
            return db.execute(query)

    def get_items(self, cod_factura):
        with dbm.DB(Config.database) as db:
            query = 'SELECT * FROM ItemLine WHERE cod_factura = {}'.format(cod_factura)
            return db.execute(query)


class ClientsController:
    def get_clients(self):
        with dbm.DB(Config.database) as db:
            query = 'SELECT * FROM Clients'
            return db.execute(query)
