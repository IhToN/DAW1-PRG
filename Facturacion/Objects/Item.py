class Item:
    def __init__(self, cod_articulo, nombre, precio):
        self.cod_articulo = cod_articulo
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return '{} - {} ({})'.format(self.cod_articulo, self.nombre, self.precio)