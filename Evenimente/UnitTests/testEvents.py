import unittest
from Domain.Events import Event


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.e = Event(10, "22/12/2016", "22:42", "Limit 1")
        self.e1 = Event(10, "22/12/2016", "22:42", "Limit 3")

    def test_properties(self):
        self.assertEqual(self.e.EventID, 10)
        self.assertEqual(self.e.Description, "Limit 1")
        self.assertEqual(self.e.Date, '22/12/2016')
        self.assertEqual(self.e.Time, "22:42")

    def test_update(self):
        self.e.setID(11)
        self.e.setDate("23/12/2016")
        self.e.setTime("23:42")
        self.e.setDescription("Limit 2")
        self.assertEqual(self.e.EventID, 11)
        self.assertEqual(self.e.Description, "Limit 2")
        self.assertEqual(self.e.Date, '23/12/2016')
        self.assertEqual(self.e.Time, "23:42")

    def test_strAndequal(self):
        self.assertEqual(str(self.e1), "10 22/12/2016 22:42 Limit 3")
        self.assertEqual(self.e, self.e1)


if __name__ == '__main__':
    unittest.main()
