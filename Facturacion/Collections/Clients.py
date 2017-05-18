from Facturacion.Controllers.ControlDB import ClientsController
from Facturacion.Objects.Client import Client


class Clients:
    def __init__(self):
        self.clientes = {}
        self.controller = ClientsController()
        self.load_clients()

    def load_clients(self):
        for client in self.controller.get_clients():
            self.clientes[client[0]] = Client(client[0], client[1], client[2],
                                              client[3], client[4], client[5],
                                              client[6])
