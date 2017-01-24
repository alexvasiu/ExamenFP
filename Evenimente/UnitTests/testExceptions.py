import unittest
from Domain.Exceptions import *

class testExceptions(unittest.TestCase):
    def testPersonException(self):
        with self.assertRaises(PersonException) as error:
            raise PersonException("Person exception")
        self.assertTrue("Person exception" in str(error.exception))

    def testEventException(self):
        with self.assertRaises(EventException) as error:
            raise EventException("Event exception")
        self.assertTrue("Event exception" in str(error.exception))

    def testDatabaseException(self):
        with self.assertRaises(DatabaseException) as error:
            raise DatabaseException("Database exception")
        self.assertTrue("Database exception" in str(error.exception))

if __name__ == '__main__':
    unittest.main()
