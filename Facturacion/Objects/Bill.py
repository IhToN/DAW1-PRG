from Facturacion.Misc import Config

class Bill:
    def __init__(self, cod_factura, vendedor, cliente, articulos=None):
        if articulos is None:
            articulos = []

        self.cod_factura = cod_factura
        self.vendedor = vendedor
        self.cliente = cliente
        self.articulos = articulos
        self.total = 0
        self.calc_total()

    def add_item(self, linea_articulo):
        self.articulos.append(linea_articulo)

    def calc_total(self):
        self.total = 0
        if not self.articulos:
            return

        for lp in self.articulos:
            self.total += lp.articulo.precio * lp.cantidad * (1 + Config.IVA/100)


class ItemLine:
    def __init__(self, factura, articulo, cantidad):
        self.factura = factura
        self.articulo = articulo
        self.cantidad = cantidad

