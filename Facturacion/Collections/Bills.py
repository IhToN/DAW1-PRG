from Facturacion.Controllers.ControlDB import BillsController
from Facturacion.Objects.Bill import Bill, ItemLine
from Facturacion.Misc import Collection


class Bills:
    def __init__(self):
        self.facturas = {}
        self.controller = BillsController()
        self.load_bills()

    def load_bills(self):
        for bill in self.controller.get_bills():
            self.facturas[bill[0]] = Bill(bill[0], Collection.clients.clientes[bill[1]])

    def load_items(self, cod_factura):
        factura = self.facturas[cod_factura]
        for item in self.controller.get_items(cod_factura):
            factura.add_item(ItemLine(Collection.items.articulos[item[0]], item[1], factura))
