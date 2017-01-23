import unittest
from Controller.ControllerJucatori import ControllerJucator
from Repository.Repo import Repo
from Domain.Validator import Validator
from Domain.Jucator import Jucator

class testRepo(unittest.TestCase):
    def setUp(self):
        self.__validator = Validator()
        self.__repo = Repo("tests")
        self.__controller = ControllerJucator(self.__validator, self.__repo)

    def test01(self):
        self.assertEqual(self.__repo.getAll(), [])
        self.__controller.AdaugaJucator("Alex", "Vasiu", 199, "Fundas")
        self.assertEqual(len(self.__repo.getAll()), 1)
        self.__repo.storePlayer(Jucator("Alex", "Vasiu", 199, "Fundas"))
        self.assertEqual(len(self.__repo.getAll()), 1)
        self.__repo.updateInaltime(Jucator("Alex", "Vasiu", 199, "Fundas"), 200)
        self.assertEqual(self.__repo.getAll()[0].getInaltime(), 200)
        self.assertEqual(len(self.__repo.getFromFile("test1.txt")), 2)

    def tearDown(self):
        with open("tests", "w") as f:
            f.close()
if __name__ == '__main__':
    unittest.main()
