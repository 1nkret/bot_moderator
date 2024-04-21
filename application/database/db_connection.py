from sqlite3 import connect


class DbConnection:
    """
    Class to connect to db
    """
    def __init__(self):
        self.connection = connect('database.db')

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()