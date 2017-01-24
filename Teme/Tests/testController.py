import unittest
from Controller.TemeController import TemeController
from Domain.Validator import Validator
from Repository.Repo import Repo

class testController(unittest.TestCase):
    def setUp(self):
        self.__repo = Repo("tests")
        self.__validator = Validator()
        self.__controller = TemeController(self.__repo, self.__validator)

    def test_create(self):
        self.__controller.createTema(10, "Alex", "A b c d e")
        self.assertEqual(len(self.__repo.getAll), 1)
        with self.assertRaises(ValueError) as error:
            self.__controller.createTema(10, "Ion", "A b c d e")
        self.assertTrue("Person already exists" in str(error.exception))
        self.assertEqual(len(self.__repo.getAll), 1)

    def test_Order(self):
        self.__controller.createTema(10, "Alex", "A b c d e")
        self.__controller.createTema(11, "Alex1", "A b c d e f r")
        self.__controller.createTema(12, "Alex2", "A b c d e g")
        self.assertEqual(self.__controller.temeOrdDesc(), ['11,Alex1,A b c d e f r', '12,Alex2,A b c d e g', '10,Alex,A b c d e'])

    def test_plagiat(self):
        self.__controller.createTema(10, "Alex", "A b c d e")
        self.__controller.createTema(11, "Alex1", "A b c d e f r")
        self.__controller.createTema(12, "Alex2", "ana are mere pere etc")
        self.assertEqual(self.__controller.plagiat(), [('10,Alex,A b c d e', '11,Alex1,A b c d e f r', '41.67 %')])

    def tearDown(self):
        with open("tests", 'w') as file:
            file.write('')
        del self.__repo
        del self.__validator
        del self.__controller

if __name__ == '__main__':
    unittest.main()
