import tkinter
import tkinter.ttk as ttk
from Facturacion.Collections.Vendors import Vendors
from Facturacion.Collections.Clients import Clients
from Facturacion.Collections.Bills import Bills
from Facturacion.Collections.Items import Items


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
        tv.grid(padx=20, pady=20)

        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def load_list(self):
        for bill in Bills.facturas:
            self.treeview.insert('', 'end', text=bill.cod_factura, values=(bill.vendedor,
                                                                           bill.cliente, bill.total, '--'))


class CreateVendorWindow(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title('Facturas - Agregar Vendedor')
        self.frame = tkinter.Frame(self)
        self.frame.grid(padx=20, pady=20)

        # cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad
        self.vc_cif = tkinter.StringVar()
        self.vc_name = tkinter.StringVar()
        self.vc_sn1 = tkinter.StringVar()
        self.vc_sn2 = tkinter.StringVar()
        self.vc_adr = tkinter.StringVar()
        self.vc_zip = tkinter.IntVar()
        self.vc_cty = tkinter.StringVar()

        self.create_ui()

    def create_ui(self):
        self.lbl_head = tkinter.Label(self.frame, text='Datos del nuevo vendedor', font=('TkHeadingFont', 12), height=2)
        self.lbl_head.grid(row=0, columnspan=2)

        self.lbl_cif = tkinter.Label(self.frame, text='CIF')
        self.lbl_cif.grid(row=1, column=0, sticky=tkinter.W)
        self.etr_cif = tkinter.Entry(self.frame, textvariable=self.vc_cif)
        self.etr_cif.grid(row=1, column=1)

        self.lbl_name = tkinter.Label(self.frame, text='Nombre')
        self.lbl_name.grid(row=2, column=0, sticky=tkinter.W)
        self.etr_name = tkinter.Entry(self.frame, textvariable=self.vc_name)
        self.etr_name.grid(row=2, column=1)

        self.lbl_sn1 = tkinter.Label(self.frame, text='1º Apellido')
        self.lbl_sn1.grid(row=3, column=0, sticky=tkinter.W)
        self.etr_sn1 = tkinter.Entry(self.frame, textvariable=self.vc_sn1)
        self.etr_sn1.grid(row=3, column=1)

        self.lbl_sn2 = tkinter.Label(self.frame, text='2º Apellido')
        self.lbl_sn2.grid(row=4, column=0, sticky=tkinter.W)
        self.etr_sn2 = tkinter.Entry(self.frame, textvariable=self.vc_sn2)
        self.etr_sn2.grid(row=4, column=1)

        self.lbl_adr = tkinter.Label(self.frame, text='Dirección')
        self.lbl_adr.grid(row=5, column=0, sticky=tkinter.W)
        self.etr_adr = tkinter.Entry(self.frame, textvariable=self.vc_adr)
        self.etr_adr.grid(row=5, column=1)

        self.lbl_zip = tkinter.Label(self.frame, text='Cód. Postal')
        self.lbl_zip.grid(row=6, column=0, sticky=tkinter.W)
        self.etr_zip = tkinter.Entry(self.frame, textvariable=self.vc_zip)
        self.etr_zip.grid(row=6, column=1)

        self.lbl_cty = tkinter.Label(self.frame, text='Ciudad')
        self.lbl_cty.grid(row=7, column=0, sticky=tkinter.W)
        self.etr_cty = tkinter.Entry(self.frame, textvariable=self.vc_cty)
        self.etr_cty.grid(row=7, column=1)

        self.btn_yes = tkinter.Button(self.frame, text='Guardar Nuevo Vendedor', command=self.save_vendor)
        self.btn_yes.grid(row=8, columnspan=2)

    def save_vendor(self):
        ven_data = self.vc_cif.get(), self.vc_name.get(), self.vc_sn1.get(), self.vc_sn2.get(), \
                   self.vc_adr.get(), self.vc_zip.get(), self.vc_cty.get()
        print('Guardando un vendedor con los siguientes datos: {}'.format(ven_data))
        Vendors.add_vendor(*ven_data)


class CreateClientWindow(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title('Facturas - Agregar Cliente')
        self.frame = tkinter.Frame(self)
        self.frame.grid(padx=20, pady=20)

        # cif, nombre, apellido1, apellido2, direccion, cod_postal, ciudad
        self.vc_cif = tkinter.StringVar()
        self.vc_name = tkinter.StringVar()
        self.vc_sn1 = tkinter.StringVar()
        self.vc_sn2 = tkinter.StringVar()
        self.vc_adr = tkinter.StringVar()
        self.vc_zip = tkinter.IntVar()
        self.vc_cty = tkinter.StringVar()

        self.create_ui()

    def create_ui(self):
        self.lbl_head = tkinter.Label(self.frame, text='Datos del nuevo cliente', font=('TkHeadingFont', 12), height=2)
        self.lbl_head.grid(row=0, columnspan=2)

        self.lbl_cif = tkinter.Label(self.frame, text='CIF')
        self.lbl_cif.grid(row=1, column=0, sticky=tkinter.W)
        self.etr_cif = tkinter.Entry(self.frame, textvariable=self.vc_cif)
        self.etr_cif.grid(row=1, column=1)

        self.lbl_name = tkinter.Label(self.frame, text='Nombre')
        self.lbl_name.grid(row=2, column=0, sticky=tkinter.W)
        self.etr_name = tkinter.Entry(self.frame, textvariable=self.vc_name)
        self.etr_name.grid(row=2, column=1)

        self.lbl_sn1 = tkinter.Label(self.frame, text='1º Apellido')
        self.lbl_sn1.grid(row=3, column=0, sticky=tkinter.W)
        self.etr_sn1 = tkinter.Entry(self.frame, textvariable=self.vc_sn1)
        self.etr_sn1.grid(row=3, column=1)

        self.lbl_sn2 = tkinter.Label(self.frame, text='2º Apellido')
        self.lbl_sn2.grid(row=4, column=0, sticky=tkinter.W)
        self.etr_sn2 = tkinter.Entry(self.frame, textvariable=self.vc_sn2)
        self.etr_sn2.grid(row=4, column=1)

        self.lbl_adr = tkinter.Label(self.frame, text='Dirección')
        self.lbl_adr.grid(row=5, column=0, sticky=tkinter.W)
        self.etr_adr = tkinter.Entry(self.frame, textvariable=self.vc_adr)
        self.etr_adr.grid(row=5, column=1)

        self.lbl_zip = tkinter.Label(self.frame, text='Cód. Postal')
        self.lbl_zip.grid(row=6, column=0, sticky=tkinter.W)
        self.etr_zip = tkinter.Entry(self.frame, textvariable=self.vc_zip)
        self.etr_zip.grid(row=6, column=1)

        self.lbl_cty = tkinter.Label(self.frame, text='Ciudad')
        self.lbl_cty.grid(row=7, column=0, sticky=tkinter.W)
        self.etr_cty = tkinter.Entry(self.frame, textvariable=self.vc_cty)
        self.etr_cty.grid(row=7, column=1)

        self.btn_yes = tkinter.Button(self.frame, text='Guardar Nuevo Cliente', command=self.save_client)
        self.btn_yes.grid(row=8, columnspan=2)

    def save_client(self):
        cli_data = self.vc_cif.get(), self.vc_name.get(), self.vc_sn1.get(), self.vc_sn2.get(), \
                   self.vc_adr.get(), self.vc_zip.get(), self.vc_cty.get()
        print('Guardando un cliente con los siguientes datos: {}'.format(cli_data))
        Clients.add_client(*cli_data)


class CreateItemWindow(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title('Facturas - Agregar Artículo')
        self.frame = tkinter.Frame(self)
        self.frame.grid(padx=20, pady=20)

        # cod_articulo, nombre, precio
        self.vc_cod = tkinter.IntVar()
        self.vc_name = tkinter.StringVar()
        self.vc_prc = tkinter.DoubleVar()

        self.vc_cod.set(Items.get_max_code())

        self.create_ui()

    def create_ui(self):
        self.lbl_head = tkinter.Label(self.frame, text='Datos del nuevo artículo', font=('TkHeadingFont', 12), height=2)
        self.lbl_head.grid(row=0, columnspan=2)

        self.lbl_cod = tkinter.Label(self.frame, text='Cód. Artículo')
        self.lbl_cod.grid(row=1, column=0, sticky=tkinter.W)
        self.etr_cod = tkinter.Entry(self.frame, textvariable=self.vc_cod)
        self.etr_cod.grid(row=1, column=1)

        self.lbl_name = tkinter.Label(self.frame, text='Nombre')
        self.lbl_name.grid(row=2, column=0, sticky=tkinter.W)
        self.etr_name = tkinter.Entry(self.frame, textvariable=self.vc_name)
        self.etr_name.grid(row=2, column=1)

        self.lbl_prc = tkinter.Label(self.frame, text='Precio')
        self.lbl_prc.grid(row=7, column=0, sticky=tkinter.W)
        self.etr_prc = tkinter.Entry(self.frame, textvariable=self.vc_prc)
        self.etr_prc.grid(row=7, column=1)

        self.btn_yes = tkinter.Button(self.frame, text='Guardar Nuevo Artículo', command=self.save_item)
        self.btn_yes.grid(row=8, columnspan=2)

    def save_item(self):
        itm_data = self.vc_cod.get(), self.vc_name.get(), self.vc_prc.get()
        print('Guardando un producto con los siguientes datos: {}'.format(itm_data))
        Items.add_item(*itm_data)


class CreateBillWindow(tkinter.Toplevel):
    def __init__(self):
        tkinter.Toplevel.__init__(self)
        self.title('Facturas - Crear Factura')
        self.frame = tkinter.Frame(self)
        self.frame.grid(padx=20, pady=20)

        # cod_factura, vendedor, cliente
        self.vc_cod = tkinter.IntVar()
        self.vc_vnd = tkinter.StringVar()
        self.vc_cln = tkinter.StringVar()

        self.vc_cod.set(Items.get_max_code())

        self.create_ui()

    def create_ui(self):
        self.lbl_head = tkinter.Label(self.frame, text='Datos del nuevo artículo', font=('TkHeadingFont', 12), height=2)
        self.lbl_head.grid(row=0, columnspan=2)

        self.lbl_cod = tkinter.Label(self.frame, text='Cód. Artículo')
        self.lbl_cod.grid(row=1, column=0, sticky=tkinter.W)
        self.etr_cod = tkinter.Entry(self.frame, textvariable=self.vc_cod)
        self.etr_cod.grid(row=1, column=1)

        self.lbl_vnd = tkinter.Label(self.frame, text='Vendedor')
        self.lbl_vnd.grid(row=2, column=0, sticky=tkinter.W)
        self.cb_vnd = ttk.Combobox(self.frame, textvariable=self.vc_vnd, state="readonly")
        self.cb_vnd.grid(row=2, column=1)
        self.vnd_vals = self.cb_load_options(Vendors.vendedores.values(), self.cb_vnd, "cif",
                                             next(iter(Vendors.vendedores.values())), self.vc_vnd)

        self.lbl_cln = tkinter.Label(self.frame, text='Cliente')
        self.lbl_cln.grid(row=3, column=0, sticky=tkinter.W)
        self.cb_cln = ttk.Combobox(self.frame, textvariable=self.vc_cln, state="readonly")
        self.cb_cln.grid(row=3, column=1)
        self.cln_vals = self.cb_load_options(Clients.clientes.values(), self.cb_cln, "cif",
                                             next(iter(Clients.clientes.values())), self.vc_cln)

        self.btn_yes = tkinter.Button(self.frame, text='Guardar Nuevo Artículo', command=self.save_item)
        self.btn_yes.grid(row=8, columnspan=2)

    def cb_load_options(self, coleccion, objeto, campoid, val2select, variable):
        keys, values = [], []

        for obj in coleccion:
            values.append(str(obj))
            keys.append(getattr(obj, campoid))
        objeto['values'] = values
        return dict(zip(values, keys))

    def save_item(self):
        vendor = Vendors.vendedores[self.vnd_vals[self.vc_vnd.get()]]
        client = Clients.clientes[self.cln_vals[self.vc_cln.get()]]
        itm_data = self.vc_cod.get(), vendor, client
        print('Guardando un producto con los siguientes datos: {}'.format(itm_data))
        print('Tipo del vendedor', type(vendor))
        # Items.add_item(*itm_data)
