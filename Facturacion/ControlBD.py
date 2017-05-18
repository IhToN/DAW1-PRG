import sqlite3


class DB(object):
    """Inicializador y gestor de bases de datos SQLite. Funciona como un gestor de contexto."""

    def __init__(self, database='database.db', queries=None):
        """Crea o se conecta a una base de datos.

        Permite ejecutar una lista de querys.
        """

        self.database = database
        self.query = ''
        self.display = False

        if queries is not None:
            self.connect()
            self.execute(queries)
            self.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        """Conectarse a la base de datos SQLite."""

        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.connected = True
        self.query = ''

    def close(self):
        """Cierra la base de datos SQLite."""

        self.connection.commit()
        self.connection.close()
        self.connected = False

    def incomplete(self, statement):
        """Concatena sentencias hasta que se completa una query."""

        self.query += statement
        if self.query.count(';') > 1:
            self.query = ''
            raise ValueError('Ha ocurrido un error: No intentes ejecutar mas de una query a la vez.' +
                             '\nEl fallo ha sido en la query: {}'.format(self.query))

        return not sqlite3.complete_statement(self.query)

    def execute(self, queries=None):
        """Ejecuta una lista de Querys.

        Las sentencias incompletas se concatenarán en self.query hasta dar con una compelta (terminando en ;).

        La ejecución devolverá una lista con los resultados a tratar. Ejemplo de uso: 

        for resultado in db.execute(queries):
            for fila in resultado:
                print(fila)
        """
        if queries is None:
            return

        res_data = []
        close = False
        if not self.connected:
            self.connect()
            close = True

        if type(queries) == str:
            queries = [queries]
        for query in queries:
            if self.incomplete(query):
                continue
            try:
                query = self.query.strip()
                self.query = ''
                self.cursor.execute(query)

                for data in self.cursor:
                    if query.upper().startswith('SELECT'):
                        res_data.append(data)

            except sqlite3.Error as error:
                print('Ha ocurrido el siguiente error: {}'.format(error.args[0]))
                print('Para la query: {}'.format(query))

        if close:
            self.close()
        return res_data


if __name__ == '__main__':
    statement = 'CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, texto TEXT);'
    tables = ['tabla1', 'tabla2']

    database = 'test.db'
    queries = [statement.format(table) for table in tables]

    with DB(database, queries) as db:
        db.execute(["INSERT INTO tabla1 (id, texto) VALUES (8, 'reference.txt');"])

        db.execute(["INSERT INTO tabla2 (id, texto) VALUES (8, 'one.txt');",
                    "INSERT INTO tabla2 (id, texto) VALUES (9, 'two.txt');"])

        db.execute(["INSERT INTO tabla2 (id, texto) VALUES (10, 'three.txt');"])

        selects = ['SELECT * FROM tabla1;', 'SELECT * FROM tabla2;']

        for result in db.execute(selects):
            print(result)
