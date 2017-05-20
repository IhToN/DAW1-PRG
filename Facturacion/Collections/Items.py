from Facturacion.Objects.Item import Item
from Facturacion.Controllers.ControlDB import ItemsController


class Items:
    articulos = {}
    controller = ItemsController()

    @classmethod
    def load_items(cls):
        for item in cls.controller.get_items():
            cls.articulos[item[0]] = Item(item[0], item[1], item[2])

    @classmethod
    def get_max_code(cls):
        if not cls.articulos:
            return 1
        return max(cls.articulos, key=int) + 1

    @classmethod
    def add_item(cls, cod_articulo, nombre, precio):
        if cod_articulo in cls.articulos:
            return
        articulo = Item(cod_articulo, nombre, precio)
        cls.articulos[cod_articulo] = articulo
        cls.controller.add_item(articulo)
