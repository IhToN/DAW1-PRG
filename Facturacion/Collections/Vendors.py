from Facturacion.Objects.Vendor import Vendor
from Facturacion.Controllers.ControlDB import VendorsController


class Vendors:
    vendedores = {}
    controller = VendorsController()

    @classmethod
    def load_vendors(cls):
        for vendedor in cls.controller.get_vendors():
            cls.vendedores[vendedor[0]] = Vendor(vendedor[0], vendedor[1], vendedor[2],
                                                 vendedor[3], vendedor[4], vendedor[5],
                                                 vendedor[6])

    @classmethod
    def add_vendor(cls, cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad):
        if cif in cls.vendedores:
            return
        vendedor = Vendor(cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad)
        cls.vendedores[cif] = vendedor
        cls.controller.add_vendor(vendedor)
