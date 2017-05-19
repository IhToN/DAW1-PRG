import tkinter
import tkinter.ttk as ttk


class BillsListWindow(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title('Facturas - Lista de Facturas')
        self.create_ui()

    def create_ui(self):
        tv = ttk.Treeview(self)
        tv['columns'] = ('vendedor', 'cliente', 'total', 'opciones')
        tv.heading("#0", text='Factura', anchor='w')
        tv.column("#0", anchor="w", width=100)
        tv.heading('vendedor', text='Vendedor')
        tv.column('vendedor', anchor='center', width=100)
        tv.heading('cliente', text='Cliente')
        tv.column('cliente', anchor='center', width=100)
        tv.heading('total', text='Precio Total')
        tv.column('total', anchor='center', width=100)
        tv.heading('opciones', text='Opciones')
        tv.column('opciones', anchor='center', width=100)
        tv.grid()

        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
