from Facturacion.Objects.Vendor import Vendor
from Facturacion.Controllers.ControlDB import VendorsController


class Vendors:
    vendedores = {}
    controller = VendorsController()

    def load_vendors(self):
        for vendedor in Vendors.controller.get_vendors():
            Vendors.vendedores[vendedor[0]] = Vendor(vendedor[0], vendedor[1], vendedor[2],
                                                     vendedor[3], vendedor[4], vendedor[5],
                                                     vendedor[6])

    def add_vendor(self, cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad):
        if cif in Vendors.vendedores:
            return
        vendedor = Vendor(cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad)
        Vendors.vendedores[cif] = vendedor
        Vendors.controller.add_vendor(vendedor)
