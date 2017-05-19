import tkinter
import tkinter.ttk as ttk
from Facturacion.Collections.Vendors import Vendors

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
        vendors = Vendors()
        ven_data = self.vc_cif.get(), self.vc_name.get(), self.vc_sn1.get(), self.vc_sn2.get(), \
                   self.vc_adr.get(), self.vc_zip.get(), self.vc_cty.get()
        print('Guardando un vendedor con los siguientes datos: {}'.format(ven_data))
        vendors.add_vendor(*ven_data)
