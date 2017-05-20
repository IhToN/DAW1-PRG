from Facturacion.Objects.Bill import Bill, ItemLine
from Facturacion.Controllers.ControlDB import BillsController
from Facturacion.Collections.Vendors import Vendors
from Facturacion.Collections.Clients import Clients
from Facturacion.Collections.Items import Items


class Bills:
    facturas = {}
    controller = BillsController()

    @classmethod
    def load_bills(cls):
        for bill in cls.controller.get_bills():
            cls.facturas[bill[0]] = Bill(bill[0], Vendors.vendedores[bill[1]], Clients.clientes[bill[2]])

    @classmethod
    def load_items(cls, cod_factura):
        factura = cls.facturas[cod_factura]
        for item in cls.controller.get_items(cod_factura):
            factura.add_item(ItemLine(factura, Items.articulos[item[0]], item[1]))
