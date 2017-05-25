import Facturacion.Controllers.DBCreator as dbc


def generateDB(is_test=True):
    creator = dbc.Creator()
    creator.create_db(is_test)


if __name__ == '__main__':
    generateDB()
