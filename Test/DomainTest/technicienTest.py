import unittest
from Domain.technicien import Technicien



class MyTestCase(unittest.TestCase):
    def test_get_all_inter(self):
        mytech = Technicien("Lahcene")
        mytech.getAllInter()
        print(len(mytech.interventions))



if __name__ == '__main__':
    unittest.main()
