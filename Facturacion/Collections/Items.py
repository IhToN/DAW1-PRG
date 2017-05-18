from Facturacion.Controllers.ControlDB import ItemsController
from Facturacion.Objects.Item import Item


class Items:
    def __init__(self):
        self.articulos = {}
        self.controller = ItemsController()
        self.load_items()

    def load_items(self):
        for item in self.controller.get_items():
            self.articulos[item[0]] = Item(item[0], item[1], item[2])
