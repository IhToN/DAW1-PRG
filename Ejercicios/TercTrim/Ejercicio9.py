"""
    a) Crear una tiqueta y un botón. Cuando pulsamos el botón, la etiqueta va cambiando.
    b) Cada vez que cuente, que cambie alternativamente de color.
"""

from tkinter import Tk, Frame, Button, BOTH, Label


class Ventana(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')

        print("Init Frame")

        self.parent = parent
        self.contador = 0
        self.color = 'yellow'

        self.initUI()

    def initUI(self):
        '''Interfaz Gráfico'''
        self.parent.title('Ejercicio 9')
        self.grid()

        print("Init GUI")

        self.texto = Label(self, text='cuenta: {}'.format(self.contador), background='yellow')
        self.texto.grid(row=1, column=1)

        self.boton = Button(self, text='Pulsador', command=self.contar, background='cyan')
        self.boton.grid(row=1, column=2)

    def contar(self):
        self.contador += 1
        self.texto['text'] = 'cuenta: {}'.format(self.contador)
        print('Contador + 1 = {}'.format(self.contador))


def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()


if __name__ == "__main__":
    main()
