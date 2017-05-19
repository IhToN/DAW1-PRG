import Facturacion.Controllers.DBManager as dbm
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
            query = 'SELECT * FROM ItemLines WHERE cod_factura = {}'.format(cod_factura)
            return db.execute(query)


class ClientsController:
    def get_clients(self):
        with dbm.DB(Config.database) as db:
            query = 'SELECT * FROM Clients'
            return db.execute(query)


class VendorsController:
    def get_vendors(self):
        with dbm.DB(Config.database) as db:
            query = 'SELECT * FROM Vendors'
            return db.execute(query)

    def add_vendor(self, vendor):
        with dbm.DB(Config.database) as db:
            # cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad
            query = "INSERT INTO Vendors VALUES ('{}', '{}', '{}', '{}', '{}', {}, '{}');"
            query = query.format(vendor.cif, vendor.nombre, vendor.apellido1, vendor.apellido2, vendor.direccion,
                                 vendor.cod_postal, vendor.ciudad)
            db.execute(query)
