class Loggable():
    def __init__(self):
        self.title = ''

    def log(self):
        print('Load message from ' + self.title)


class Connection():
    def __init__(self):
        self.server = ''

    def connect(self):
        print('Connecting to database on ' + self.server)


class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.title = 'Sql Connection Demo of Madoka'
        self.server = 'Madoka server'


def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()


sql_connection = SqlDatabase()
framework(sql_connection)
