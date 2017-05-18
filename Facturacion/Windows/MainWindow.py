import tkinter


class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        print("Iniciando ventana principal")

        self.parent = parent
        self.vc_cls = tkinter.DoubleVar()
        self.vc_kel = tkinter.DoubleVar()
        self.vc_fah = tkinter.DoubleVar()

        self.initUI()

        self.bind("<Button-1>", self.callback)

    def initUI(self):
        '''Interfaz Gráfico'''
        self.parent.title('Facturas - Ventana Principal')
        self.grid(padx=20, pady=20)

        self.initTXT()

    def initTXT(self):
        self.lbl_todo = tkinter.Label(self, text='¿Qué quieres hacer?', font=('TkHeadingFont', 16), height=2)
        self.lbl_todo.grid(row=0, column=1)

        self.btn_ver_factura = tkinter.Button(self, text='Ver Facturas', bg='white')
        self.btn_ver_factura.grid(row=1, column=1)

        self.btn_crear_factura = tkinter.Button(self, text='Crear Factura', bg='white')
        self.btn_crear_factura.grid(row=2, column=0)

        self.btn_agregar_cliente = tkinter.Button(self, text='Agregar Cliente', bg='white')
        self.btn_agregar_cliente.grid(row=2, column=1)

        self.btn_agregar_cliente = tkinter.Button(self, text='Agregar Producto', bg='white')
        self.btn_agregar_cliente.grid(row=2, column=2)

    def callback(self, event):
        self.focus_set()


def main():
    root = tkinter.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
