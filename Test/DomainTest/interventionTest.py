import unittest
from Domain.intervention import Intervention
from DataAccess.dbOp import DbOp
import json


class MyTestCase(unittest.TestCase):
    def test_create_object_from_json(self):
        """json object to convert"""
        x = '{"libelle": "Azerty", "id_Client": 18}'
        myjson = json.loads(x)
        myObj = Intervention()
        myObj.createFromJson(myjson)
        self.assertEqual('Azerty', myObj.libelle)

    def test_insert_obj_in_db(self):
        x = '{"libelle": "Azerty", "id_Client": 7}'
        myjson = json.loads(x)
        myObj = Intervention()
        myObj.createFromJson(myjson)
        ret = myObj.putInDb()
        self.assertEqual("ok", ret)

    def test_get_inter_from_db(self):
        cmd = f"SELECT * FROM Intervention WHERE Id_Intervention = 1"
        dbobj = DbOp()
        record = dbobj.get_from_db(cmd)
        my_inter = Intervention()
        my_inter.createFromRecord(record)
        self.assertEqual("Azerty", my_inter.libelle)


if __name__ == '__main__':
    unittest.main()
