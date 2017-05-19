from Facturacion.Objects.Item import Item
from Facturacion.Controllers.ControlDB import ItemsController


class Items:
    articulos = {}
    controller = ItemsController()

    def load_items(self):
        for item in self.controller.get_items():
            self.articulos[item[0]] = Item(item[0], item[1], item[2])
