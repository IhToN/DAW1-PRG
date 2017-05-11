class Cliente:
    def __init__(self, ncliente, nombre, telefono, direccion, ciudad):
        self.ncliente = ncliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad

    def __repr__(self):
        return 'Cliente({}, {}, {}, {}, {})'.format(self.ncliente, self.nombre, self.telefono, self.direccion,
                                                    self.ciudad)
