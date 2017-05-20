from Facturacion.Objects.Client import Client
from Facturacion.Controllers.ControlDB import ClientsController


class Clients:
    clientes = {}
    controller = ClientsController()

    @classmethod
    def load_clients(cls):
        for client in cls.controller.get_clients():
            cls.clientes[client[0]] = Client(client[0], client[1], client[2],
                                             client[3], client[4], client[5],
                                             client[6])

    @classmethod
    def add_client(cls, cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad):
        if cif in cls.clientes:
            return
        cliente = Client(cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad)
        cls.clientes[cif] = cliente
        cls.controller.add_client(cliente)
