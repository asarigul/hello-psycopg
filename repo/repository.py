from  dbmanager import DBManager

class Repository:

    def __init__(self, db_manager:DBManager):
        self._db_manager = db_manager

    def _connection(self):
        return self._db_manager.get_connection()