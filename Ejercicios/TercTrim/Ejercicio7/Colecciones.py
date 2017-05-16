from Ejercicios.TercTrim.Ejercicio7 import Clases
from Ejercicios.TercTrim.Ejercicio7.ControlBD import ControlBD


class ColeccionClientes:
    def __init__(self):
        self.cbd = ControlBD()
        self.clientes = dict()
        self.cargar_clientes()

    def obtener_cliente(self, dni):
        return self.clientes[dni]

    def cargar_clientes(self):
        for cliente in self.cbd.obtener_clientes():
            ncliente, nombre, telefono, direccion, ciudad = cliente
            self.clientes[cliente[0]] = Clases.Cliente(ncliente, nombre, telefono, direccion, ciudad)
        self.cbd.descoenctar()

    def nuevo_cliente(self, ncliente, nombre, telefono, direccion, ciudad):
        cliente = Clases.Cliente(ncliente, nombre, telefono, direccion, ciudad)
        if ncliente not in self.clientes:
            self.clientes[ncliente] = cliente
            self.cbd.insertar_cliente(cliente)
        self.cbd.descoenctar()
        return cliente
