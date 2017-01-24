import unittest
from Controller.EventsController import EventsController
from Controller.PersonsController import PersonsController
from Domain.Validator import Validator
from Domain.Persons import Person
from Repository.RepoMemory import RepoMemory
from Domain.Exceptions import PersonException

class testPersonController(unittest.TestCase):
    def setUp(self):
        self.repo = RepoMemory()
        self.validator = Validator()
        self.controller = PersonsController(self.repo, self.validator)
        self.person = Person(9991119, "Alex", "Daliei nr.2")
        self.controller_events = EventsController(self.repo, self.validator)

    def test_update(self):
        self.controller.createPerson(9991119, "Alex", "Daliei nr.2")
        self.assertEqual(self.person, self.controller.getPersonByID(9991119))
        self.controller.update(9991119, "Alex", "Cluj")
        self.assertEqual(self.controller.getPersonByID(9991119).Name, "Alex")
        self.assertEqual(self.controller.getPersonByID(9991119).Address, "Cluj")
        self.assertEqual(self.controller.AllPersons, self.repo.AllPersons)

    def test_NotExist(self):
        with self.assertRaises(PersonException) as error:
            self.controller.searchByID(321803821038210381203812903812330213099)
        self.assertTrue("Person not found" in str(error.exception))

    def test_maxEventsAndPersonToEvents(self):
        self.controller.createPerson(9991119, "Alex", "Daliei nr.2")
        for i in range(999999999899, 999999999999):
            self.controller_events.createEvent(i, "22/12/2016", '22:22', "dsadaa")
            self.controller.getPersonByID(9991119).registerForEvent(self.controller_events.getEventByID(i))
        l = []
        l.append(str(self.controller.searchByID(9991119)))
        for i in range(999999999899, 999999999999):
            self.controller_events.delete(i)
        self.assertEqual(self.controller.maxEvents(), l)
        self.controller_events.createEvent(999999999999, "21/12/2013", '22:22', "dasdsad")
        self.controller.getPersonByID(9991119).registerForEvent(self.controller_events.getEventByID(999999999999))
        self.controller_events.createEvent(999999999998, "22/12/2013", '22:22', "aasdsad")
        self.controller.getPersonByID(9991119).registerForEvent(self.controller_events.getEventByID(999999999998))
        self.assertEqual(self.controller.personEventsOrderByDescription(9991119), ['999999999998 22/12/2013 22:22 aasdsad',
                                                                      '999999999999 21/12/2013 22:22 dasdsad'])
        self.assertEqual(self.controller.personEventsOrderByDateTime(9991119), ['999999999999 21/12/2013 22:22 dasdsad',
                                                                   '999999999998 22/12/2013 22:22 aasdsad'])

    def test_create(self):
        with self.assertRaises(PersonException) as error:
            self.controller.createPerson("-10", "dsdsadas", "")
        self.assertTrue(str(['ID should be a number', 'Address cannot be empty']) in str(error.exception))

    def test_alreadyRegitered(self):
        self.controller.createPerson(9991119, "Alex", "Daliei nr.2")
        self.controller_events.createEvent(999999999999, "21/12/2013", '22:22', "dasdsad")
        self.controller.getPersonByID(9991119).registerForEvent(self.controller_events.getEventByID(999999999999))
        with self.assertRaises(PersonException) as error:
            self.controller.getPersonByID(9991119).registerForEvent(self.controller_events.getEventByID(999999999999))
        self.assertTrue("Already regiterd for this event" in str(error.exception))


if __name__ == '__main__':
    unittest.main()
