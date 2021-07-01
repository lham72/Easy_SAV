import unittest
from DataAccess.dbOp import DbOp


class MyTestCase(unittest.TestCase):
    def test_simple_select(self):
        cmd = """SELECT prenom FROM Technicien WHERE id_Tech = 3"""
        dbobj = DbOp()
        record = dbobj.get_from_db(cmd)
        dbobj.close
        for row in record:
            self.assertEqual("Lahcene", row[0])

    """Warning : change mychgvalue variable each time you
        execute this test"""
    def test_adding_intervention(self):
        mychgvalue = "Freezer Hors service4"
        cmd = """INSERT INTO Intervention(libelle, id_Client, id_Tech) VALUES (?, ?, ?)"""
        datas = (mychgvalue, 5, 3)
        dbobj = DbOp()
        count = dbobj.insert_into_db(cmd, datas)
        dbobj.commit()

        """Verification"""
        cmd = f"SELECT id_Tech FROM Intervention WHERE libelle = '{mychgvalue}'"
        dbobj = DbOp()
        record = dbobj.get_from_db(cmd)
        dbobj.close()
        for row in record:
            self.assertEqual(3, row[0])

    def test_get_inter_belongs_one_tech(self):
        dbobj = DbOp()
        records = dbobj.getAllInterOfTech("Lahcene")
        for row in records:
            print(row)


if __name__ == '__main__':
    unittest.main()
