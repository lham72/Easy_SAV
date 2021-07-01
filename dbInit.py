import sqlite3
import os


# Initialise database
class DbInit:
    def __init__(self, dbname):
        self.dbName = dbname

    def connect(self):
        try:
            os.remove(self.dbName)
            connexion = sqlite3.connect(self.dbName)
            return connexion

        except Exception as exc:
            print(exc)
