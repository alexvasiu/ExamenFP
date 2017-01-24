import unittest
from Domain.Events import Event
from Domain.Persons import Person
from Domain.Validator import Validator
from Domain.Exceptions import PersonException, EventException



class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()
        self.person = Person(-10, "", "")
        self.person1 = Person("dsd", "dsa", "dsada")
        self.event = Event(10, '2/02/2012', '2242', '')
        self.event1 = Event(-10, '2/24/2012', '22:42', 'dasd')

    def testValidatePerson1(self):
        with self.assertRaises(PersonException) as error:
            self.validator.validatePerson(self.person)
        self.assertTrue(str(["ID cannot be negative", "Name cannot be empty", "Address cannot be empty"]) in str(error.exception))

    def testValidatePerson2(self):
        with self.assertRaises(PersonException) as error:
            self.validator.validatePerson(self.person1)
        self.assertTrue(str(["ID should be a number"]) in str(error.exception))

    def testValidateEvent1(self):
        with self.assertRaises(EventException) as error:
            self.validator.validateEvent(self.event)
        self.assertTrue(str(["Invalid time format", "Description cannot be empty"]) in str(error.exception))

    def testValidateEvent2(self):
        with self.assertRaises(EventException) as error:
            self.validator.validateEvent(self.event1)
        self.assertTrue(str(["ID cannot be negative", "Invalid date format"]) in str(error.exception))

if __name__ == '__main__':
    unittest.main()
