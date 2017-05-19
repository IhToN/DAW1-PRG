from Facturacion.Objects.Vendor import Vendor
from Facturacion.Controllers.ControlDB import VendorsController


class Vendors:
    vendedores = {}
    controller = VendorsController()

    def load_clients(self):
        for vendedor in self.controller.get_vendors():
            self.vendedores[vendedor[0]] = Vendor(vendedor[0], vendedor[1], vendedor[2],
                                                  vendedor[3], vendedor[4], vendedor[5],
                                                  vendedor[6])
