import unittest
from Domain.Tema import Tema

class testTema(unittest.TestCase):
    def setUp(self):
        self.__tema = Tema(10, "Alex", "Rezolvare a s d f")

    def test_get(self):
        self.assertEqual(self.__tema.getID, 10)
        self.assertEqual(self.__tema.getNumeStudent, "Alex")
        self.assertEqual(self.__tema.getRezolvare, "Rezolvare a s d f")

    def test_set(self):
        self.__tema.setNumeStudent("Ion V.")
        self.assertEqual(self.__tema.getNumeStudent, "Ion V.")
        self.__tema.setRezolvare("Rez a a a a")
        self.assertEqual(self.__tema.getRezolvare, "Rez a a a a")

    def tearDown(self):
        del self.__tema


if __name__ == '__main__':
    unittest.main()
