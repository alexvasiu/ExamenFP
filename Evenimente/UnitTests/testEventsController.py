import unittest
from Controller.EventsController import EventsController
from Domain.Validator import Validator
from Domain.Events import Event
from Repository.RepoMemory import RepoMemory
from Domain.Exceptions import EventException

class testEventsController(unittest.TestCase):
    def setUp(self):
        self.repo = RepoMemory()
        self.validator = Validator()
        self.controller = EventsController(self.repo, self.validator)
        self.event = Event(1000427, '22/10/2015', '22:23', "dsada")

    def test_update(self):
        self.controller.createEvent(1000427, '22/10/2015', '22:23', "dsada")
        self.assertTrue(self.controller.AllEvents.__contains__(self.event))
        self.controller.update(1000427, '22/10/2016', '22:23', "dddd")
        self.assertEqual(self.controller.getEventByID(1000427).Date , '22/10/2016')
        self.assertEqual(self.controller.getEventByID(1000427).Description, 'dddd')
        self.assertEqual(self.controller.getEventByID(1000427).Time, '22:23')
        self.assertEqual(self.controller.AllEvents, self.repo.AllEvents)
        self.assertEqual(self.controller.searchByID(1000427), "1000427 22/10/2016 22:23 dddd")

    def test_NotExist(self):
        with self.assertRaises(EventException) as error:
            self.controller.searchByDate('323232')
        self.assertTrue("No event found" in str(error.exception))

    def test_create(self):
        with self.assertRaises(EventException) as error:
            self.controller.createEvent("10", "dsdsadas", "22:32", "dd")
        self.assertTrue(str(['ID should be a number', 'Invalid date format']) in str(error.exception))

if __name__ == '__main__':
    unittest.main()
