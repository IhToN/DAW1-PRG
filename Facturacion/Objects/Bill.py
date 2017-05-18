class Bill:
    def __init__(self, cod_factura, cliente, articulos=None):
        if articulos is None:
            articulos = []

        self.cod_factura = cod_factura
        self.cliente = cliente
        self.articulos = articulos

    def add_item(self, linea_articulo):
        self.articulos.append(linea_articulo)


class ItemLine:
    def __init__(self, articulo, cantidad, factura):
        self.articulo = articulo
        self.cantidad = cantidad
        self.factura = factura
