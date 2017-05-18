import random


class Estampita:
    def __init__(self, id, nombre, imagen, valor=0):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen
        self.valor = valor

    def __repr__(self):
        return "Cromo({}, n={}, i={}, v={})".format(self.id, self.nombre, self.imagen, self.valor)


class Album:
    def __init__(self):
        self.estampitas = dict()
        self.i = -1

    def add_estampita(self, nombre, imagen):
        id = self.get_last_estampita() + 1
        valor = random.randint(0, 99)
        self.estampitas[id] = Estampita(id, nombre, imagen, valor)

    def get_last_estampita(self):
        if not self.estampitas:
            return 0
        return max(self.estampitas, key=int)

    def __next__(self):
        self.i += 1
        if self.i < len(self.estampitas):
            key = list(self.estampitas)[self.i]
            value = self.estampitas[key]
            return value
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    album = Album()

    for id in range(1,21):
        album.add_estampita('abc{}'.format(id), 'imagen{}.png'.format(id))

    for cromo in album:
        print(cromo)
