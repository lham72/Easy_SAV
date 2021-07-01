import sqlite3
from globalVar import GlobalVar


"""class allowing to make operation on database
    as connection, execute query, commit changes and close connection"""
class DbOp:
    DB_LOCATION = GlobalVar.DB_PATH

    def __init__(self):
        self.connection = sqlite3.connect(DbOp.DB_LOCATION)
        self.cursor = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def get_from_db(self, req):
        """execute a row of data to current cursor"""
        list = self.cursor.execute(req).fetchall()
        return list

    def insert_into_db(self, req, datas):
        self.cursor.execute(req, datas)

    def getAllInterOfTech(self, prenom):
        cmd = f"SELECT * FROM Intervention " \
              f"INNER JOIN Technicien " \
              f"USING(id_Tech) " \
              f"WHERE Technicien.prenom = '{prenom}'"
        list = self.get_from_db(cmd)
        return list

    def commit(self):
        """commit changes to database"""
        self.connection.commit()
