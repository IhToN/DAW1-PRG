from Ejercicios.TercTrim.VentaDispositivo import Clases, ControlBD


class ColeccionClientes:
    def __init__(self):
        self.clientes = dict()
        self.cargar_clientes()

    def obtener_cliente(self, dni):
        return self.clientes[dni]

    def cargar_clientes(self):
        for cliente in ControlBD.obtener_clientes():
            self.clientes[cliente[0]] = Clases.Cliente(*cliente)

    def nuevo_cliente(self, ncliente, nombre, telefono, direccion, ciudad):
        cliente = Clases.Cliente(ncliente, nombre, telefono, direccion, ciudad)
        if ncliente not in self.clientes:
            self.clientes[ncliente] = cliente
            ControlBD.insertar_cliente(cliente)
        return cliente
