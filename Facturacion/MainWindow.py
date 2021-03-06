import tkinter
import Facturacion.TLWindows as tlw


class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.opened = None

        print("Iniciando ventana principal")
        self.init_ui()

        self.bind("<Button-1>", self.callback)

    def init_ui(self):
        '''Interfaz Gráfico'''
        self.parent.title('Facturas - Ventana Principal')
        self.grid(padx=20, pady=20)

        self.init_txt()

    def init_txt(self):
        self.lbl_todo = tkinter.Label(self, text='¿Qué quieres hacer?', font=('TkHeadingFont', 16), height=2)
        self.lbl_todo.grid(row=0, column=1)

        self.btn_add_bill = tkinter.Button(self, text='Crear Factura', bg='white',
                                           command=self.init_cbill_window)
        self.btn_add_bill.grid(row=1, column=0)
        self.btn_bills_list = tkinter.Button(self, text='Ver Facturas', bg='white',
                                             command=self.init_bills_window)
        self.btn_bills_list.grid(row=1, column=2)

        self.btn_add_client = tkinter.Button(self, text='Agregar Cliente', bg='white',
                                             command=self.init_cclient_window)
        self.btn_add_client.grid(row=2, column=0)
        self.btn_add_vendor = tkinter.Button(self, text='Agregar Vendedor', bg='white',
                                             command=self.init_cvendor_window)
        self.btn_add_vendor.grid(row=2, column=1)
        self.btn_add_item = tkinter.Button(self, text='Agregar Producto', bg='white',
                                           command=self.init_citem_window)
        self.btn_add_item.grid(row=2, column=2)

    def callback(self, event=None):
        self.focus_set()

    def close_tl_window(self):
        self.opened.destroy()
        self.opened = None
        self.callback()

    def init_bills_window(self):
        if not self.opened:
            self.opened = tlw.BillsListWindow(self)
            self.opened.protocol("WM_DELETE_WINDOW", self.close_tl_window)

    def init_cvendor_window(self):
        if not self.opened:
            self.opened = tlw.CreateVendorWindow(self)
            self.opened.protocol("WM_DELETE_WINDOW", self.close_tl_window)

    def init_cclient_window(self):
        if not self.opened:
            self.opened = tlw.CreateClientWindow(self)
            self.opened.protocol("WM_DELETE_WINDOW", self.close_tl_window)

    def init_citem_window(self):
        if not self.opened:
            self.opened = tlw.CreateItemWindow(self)
            self.opened.protocol("WM_DELETE_WINDOW", self.close_tl_window)

    def init_cbill_window(self):
        if not self.opened:
            self.opened = tlw.CreateBillWindow(self)
            self.opened.protocol("WM_DELETE_WINDOW", self.close_tl_window)


def main():
    root = tkinter.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
