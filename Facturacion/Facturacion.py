import os
import tkinter

from Facturacion import GenerateDB
from Facturacion.Collections.Bills import Bills
from Facturacion.Collections.Clients import Clients
from Facturacion.Collections.Items import Items
from Facturacion.Collections.Vendors import Vendors
from Facturacion import MainWindow
from Facturacion.Misc import Config


def init_collections():
    Vendors.load_vendors()
    print("Vendedores cargados:", Vendors.vendedores.values())
    Clients.load_clients()
    print("Clientes cargados:", Clients.clientes.values())
    Items.load_items()
    print("Artículos cargados:", Items.articulos.values())
    Bills.load_bills()
    print("Facturas cargadas:", Bills.facturas.values())


def main():
    if not (os.path.isfile(Config.database)):
        GenerateDB.generateDB(False)

    init_collections()

    MainWindow.main()


if __name__ == '__main__':
    main()
