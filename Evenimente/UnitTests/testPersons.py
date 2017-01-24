import unittest
from Domain.Persons import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p = Person(10, "Alex", "Strada Daliei nr.2")
        self.p1 = Person(10, "Alex", "Strada Daliei nr.2")

    def test_properties(self):
        self.assertEqual(self.p.Name, "Alex")
        self.assertEqual(self.p.PersonID, 10)
        self.assertEqual(self.p.Address, "Strada Daliei nr.2")

    def test_update(self):
        self.p.setAddress("A")
        self.assertEqual(self.p.Address, "A")
        self.p.setID(11)
        self.assertEqual(self.p.PersonID, 11)
        self.p.setName("ALEX")
        self.assertEqual(self.p.Name, "ALEX")

    def test_strAndequal(self):
        self.assertEqual(str(self.p), "10 Alex Strada Daliei nr.2")
        self.assertEqual(self.p, self.p1)

if __name__ == '__main__':
    unittest.main()