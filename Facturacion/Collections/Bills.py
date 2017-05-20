import time
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
            cls.facturas[bill[0]] = Bill(bill[0], Vendors.vendedores[bill[1]], Clients.clientes[bill[2]], bill[3])
            cls.load_items(bill[0])

    @classmethod
    def load_items(cls, cod_factura):
        factura = cls.facturas[cod_factura]
        for item in cls.controller.get_items(cod_factura):
            factura.add_item(ItemLine(factura, Items.articulos[item[0]], item[1]))

    @classmethod
    def get_max_code(cls):
        if not cls.facturas:
            return 1
        return max(cls.facturas, key=int) + 1

    @classmethod
    def items_to_il(cls, cod_factura, dict_articulos):
        il_list = []
        for item, cant in dict_articulos.items():
            il_list.append(ItemLine(Bills.facturas[cod_factura], item, cant))
        return il_list

    @classmethod
    def add_bill(cls, cod_factura, cif_vendedor, cif_cliente, dict_articulos):
        if cod_factura in cls.facturas:
            return
        vendedor = Vendors.vendedores[cif_vendedor]
        cliente = Clients.clientes[cif_cliente]
        fecha = time.strftime("%d/%m/%Y")
        factura = Bill(cod_factura, vendedor, cliente, fecha)
        cls.facturas[cod_factura] = factura
        cls.controller.add_bill(factura)

        for linea in cls.items_to_il(cod_factura, dict_articulos):
            factura.add_item(linea)
            cls.controller.add_line(linea)
