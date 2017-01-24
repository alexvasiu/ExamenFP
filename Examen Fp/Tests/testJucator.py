import unittest
from Domain.Jucator import Jucator


class test_Jucator(unittest.TestCase):
    def setUp(self):
       self.__jucator = Jucator("Vasiu", "Alex", 192, "Fundas")

    def test_atributte(self):
        self.assertEqual(self.__jucator.getNume(), "Vasiu")
        self.assertEqual(self.__jucator.getPrenume(), "Alex")
        self.assertEqual(self.__jucator.getInaltime(), 192)
        self.assertEqual(self.__jucator.getPost(), "Fundas")

    def test_setteri(self):
        self.__jucator.setInaltime(195)
        self.assertEqual(self.__jucator.getInaltime(), 195)
        self.__jucator.setPost("Extrema")
        self.assertEqual(self.__jucator.getPost(), "Extrema")

    def test_equ_str(self):
        self.assertEqual(str(self.__jucator), "Vasiu~Alex~192~Fundas\n")
        self.assertEqual(self.__jucator.getFullPlayer(), "Alex Vasiu Fundas 192")
        juc = Jucator("Vasiu", "Alex", 887, "Fundas")
        self.assertEqual(juc, self.__jucator)


if __name__ == '__main__':
    unittest.main()
