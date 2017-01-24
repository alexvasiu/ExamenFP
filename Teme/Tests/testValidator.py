import unittest
from Domain.Validator import Validator
from Domain.Tema import Tema

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.__validator = Validator()
        self.__tema1 = Tema(-10, "", "Ana are me re a")
        self.__tema2 = Tema(10, "dsdasa", "me re a")

    def test_validator1(self):
        with self.assertRaises(ValueError) as error:
            self.__validator.validateTema(self.__tema1)
        self.assertTrue("['ID is not a positive integer', 'Name should have minimum 3 letters']" in str(error.exception))

    def test_validator2(self):
        with self.assertRaises(ValueError) as error:
            self.__validator.validateTema(self.__tema2)
        self.assertTrue("['Solution should have minimum 5 words']" in str(error.exception))

    def tearDown(self):
        del self.__tema1
        del self.__tema2
        del self.__validator


if __name__ == '__main__':
    unittest.main()
