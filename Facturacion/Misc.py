from Facturacion.Collections import Items as i, Bills as b, Clients as c


class Config:
    database = 'faturacion.db'


class Collection:
    items = i.Items()
    bills = b.Bills()
    clients = c.Clients()
