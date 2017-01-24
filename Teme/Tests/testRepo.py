import unittest
from Repository.Repo import Repo
from Domain.Tema import Tema


class testRepo(unittest.TestCase):
    def setUp(self):
        self.__repo = Repo("tests")
        self.__tema = Tema(10, "Alex", "a b c d e")

    def test_store(self):
        self.__repo.store(self.__tema)
        self.assertEqual(str(self.__repo.getAll), str([self.__tema]))
        self.assertEqual(len(self.__repo.getAll), 1)

    def tearDown(self):
        with open("tests", 'w') as file:
            file.write('')
        del self.__repo
        del self.__tema

if __name__ == '__main__':
    unittest.main()
