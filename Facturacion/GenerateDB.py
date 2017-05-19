import Facturacion.Controllers.DBCreator as dbc

if __name__ == '__main__':
    creator = dbc.Creator()
    creator.create_db(False)
