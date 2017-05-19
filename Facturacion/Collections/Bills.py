from Facturacion.Objects.Bill import Bill, ItemLine
from Facturacion.Controllers.ControlDB import BillsController
from Facturacion.Collections.Vendors import Vendors
from Facturacion.Collections.Clients import Clients
from Facturacion.Collections.Items import Items


class Bills:
    facturas = {}
    controller = BillsController()

    def load_bills(self):
        for bill in self.controller.get_bills():
            self.facturas[bill[0]] = Bill(bill[0], Vendors.vendedores[bill[1]], Clients.clientes[bill[2]])

    def load_items(self, cod_factura):
        factura = self.facturas[cod_factura]
        for item in self.controller.get_items(cod_factura):
            factura.add_item(ItemLine(factura, Items.articulos[item[0]], item[1]))
