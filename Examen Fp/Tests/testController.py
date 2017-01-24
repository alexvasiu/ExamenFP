import unittest
from Controller.ControllerJucatori import ControllerJucator
from Repository.Repo import Repo
from Domain.Validator import Validator

class testController(unittest.TestCase):
    def setUp(self):
        self.__validator = Validator()
        self.__repo = Repo("tests")
        self.__controller = ControllerJucator(self.__validator, self.__repo)

    def test01(self):
        self.__controller.AdaugaJucator("Alex", "Vasiu", 210, "Fundas")
        self.assertEqual(len(self.__repo.getAll()), 1)
        with self.assertRaises(ValueError) as error:
            self.__controller.AdaugaJucator("Alex", "Vasiu", "abx", "Alergator")
        self.assertTrue(
            "['Inaltimea trebuie sa fie un numar pozitiv', 'Postul jucatorului poate fi Fundas, Pivot sau Extrema']" in str(
                error.exception))
        self.assertEqual(len(self.__repo.getAll()), 1)

    def test02(self):
        self.__controller.AdaugaJucator("Alex", "Vasiu", 210, "Fundas")
        with self.assertRaises(ValueError) as error:
            self.__controller.updateInaltime("alex", "Vasiu", 210)
        self.assertTrue("Nu exsita jucatorul introdus" in str(error.exception))
        self.__controller.updateInaltime("Alex", "Vasiu", 200)
        self.assertEqual(self.__repo.getAll()[0].getInaltime(), 200)

    def test03(self):
        self.__controller.AdaugaJucator("Alex", "Vasiu", 210, "Fundas")
        self.__controller.AdaugaJucator("Alex", "v", 202, "Fundas")
        self.__controller.AdaugaJucator("Alex", "va", 205, "Fundas")
        self.__controller.AdaugaJucator("dsada", "Vasiu", 188, "Extrema")
        self.__controller.AdaugaJucator("Alddddex", "Vasiu", 215, "Extrema")
        with self.assertRaises(ValueError) as error:
            self.__controller.getTeam()
        self.assertTrue("Nu sunt destui jucatori pentru a forma o echipa" in str(error.exception))
        self.__controller.AdaugaJucator("pop", "Vasiu", 210, "Pivot")
        print(self.__controller.getTeam())
        self.assertEqual(self.__controller.getTeam(), ['va Alex Fundas 205', 'Vasiu Alex Fundas 210', 'Vasiu pop Pivot 210', 'Vasiu dsada Extrema 188', 'Vasiu Alddddex Extrema 215'])

    def tearDown(self):
        with open("tests", "w") as f:
            f.close()
if __name__ == '__main__':
    unittest.main()