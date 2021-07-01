from typing import List
from Domain.intervention import Intervention
from DataAccess.dbOp import DbOp

class Technicien:
    def __init__(self, prenom):
        self.prenom = prenom
        self.interventions: List[Intervention] = list()

    def getAllInter(self):
        dbobj = DbOp()
        records = dbobj.getAllInterOfTech(self.prenom)
        for row in records:
            my_inter = Intervention()
            my_inter.createFromRecord(row[1], row[5])
            self.interventions.append(my_inter)
