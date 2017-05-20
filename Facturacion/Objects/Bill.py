from Facturacion.Misc import Config


class Bill:
    def __init__(self, cod_factura, vendedor, cliente, fecha, articulos=None):
        if articulos is None:
            articulos = []

        self.cod_factura = cod_factura
        self.vendedor = vendedor
        self.cliente = cliente
        self.fecha = fecha
        self.articulos = articulos
        self.calc_total()

    def __repr__(self):
        return '{} ({})'.format(self.cod_factura, self.fecha)

    def add_item(self, linea_articulo):
        self.articulos.append(linea_articulo)
        self.calc_total()

    def calc_total(self):
        self.total = 0
        self.iva = 0

        if not self.articulos:
            return
        for lp in self.articulos:
            self.total += lp.articulo.precio * lp.cantidad

        self.iva = self.total * (1 + Config.IVA / 100)


class ItemLine:
    def __init__(self, factura, articulo, cantidad):
        self.factura = factura
        self.articulo = articulo
        self.cantidad = cantidad

    def __repr__(self):
        return '{} - {} x {}'.format(self.factura, self.articulo, self.cantidad)
