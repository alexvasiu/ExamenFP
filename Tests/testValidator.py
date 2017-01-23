import unittest
from Domain.Jucator import Jucator
from Domain.Validator import Validator

class testValidator(unittest.TestCase):
    def setUp(self):
        self.__validator = Validator()

    def testOK(self):
        juc1 = Jucator("Alex", "Vasiu", 192, "Fundas")
        self.__validator.validateJucator(juc1)

    def testFail1(self):
        juc1 = Jucator("Alex", "Vasiu", "abx", "Alergator")
        with self.assertRaises(ValueError) as error:
            self.__validator.validateJucator(juc1)
        self.assertTrue("['Inaltimea trebuie sa fie un numar pozitiv', 'Postul jucatorului poate fi Fundas, Pivot sau Extrema']" in str(error.exception))

    def testFail2(self):
        juc1 = Jucator("", "Vasiu", 192, "Fundas")
        with self.assertRaises(ValueError) as error:
            self.__validator.validateJucator(juc1)
        self.assertTrue("['Numele nu poate fi vid']" in str(error.exception))

if __name__ == '__main__':
    unittest.main()
