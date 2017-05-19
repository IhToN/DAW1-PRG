from Facturacion.Objects.Client import Client
from Facturacion.Controllers.ControlDB import ClientsController


class Clients:
    clientes = {}
    controller = ClientsController()

    def load_clients(self):
        for client in self.controller.get_clients():
            self.clientes[client[0]] = Client(client[0], client[1], client[2],
                                              client[3], client[4], client[5],
                                              client[6])
