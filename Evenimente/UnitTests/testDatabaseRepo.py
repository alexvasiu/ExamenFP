import unittest
from Domain.Events import Event
from Domain.Exceptions import *
from Domain.Persons import Person
from Repository.DatabaseRepo import RepoDB

class testDatabaseRepo(unittest.TestCase):
    def setUp(self):
        self.repo = RepoDB("TestRepo.sqlite")

    def test_read(self):
        self.assertEqual(len(self.repo.AllEvents), 1)
        self.assertEqual(len(self.repo.AllPersons), 2)
        self.assertEqual(len(self.repo.AllPersons[1].AllRegisteredEvents), 1)
        self.assertEqual(len(self.repo.AllPersons[0].AllRegisteredEvents), 0)

    def test_alreadyRegitered(self):
        with self.assertRaises(PersonException) as error:
            self.repo.AllPersons[1].registerForEvent(self.repo.AllEvents[0])
        self.assertTrue("Already regiterd for this event" in str(error.exception))

    def test_StoreDeleteUpdate(self):
        event = Event(123, '22/12/2016', '22:22', 'Dsdadd dksldklsa')
        person = Person(144, "Alex", "CLUJ")
        self.repo.storeEvent(event)
        self.repo.storePerson(person)
        self.repo.AllPersons[2].registerForEvent(self.repo.AllEvents[1])
        self.assertEqual(len(self.repo.AllEvents), 2)
        self.assertEqual(len(self.repo.AllPersons), 3)
        self.assertEqual(len(self.repo.AllPersons[0].AllRegisteredEvents), 0)
        self.assertEqual(len(self.repo.AllPersons[1].AllRegisteredEvents), 1)
        self.assertEqual(len(self.repo.AllPersons[2].AllRegisteredEvents), 1)
        self.repo.updatePerson(2, "Alex Vasiu", "Cluj")
        self.repo = RepoDB("TestRepo.sqlite")
        self.assertEqual(self.repo.AllPersons[2].Name, "Alex Vasiu")
        self.assertEqual(self.repo.AllPersons[2].Address, "Cluj")
        self.repo.deleteEvent(1)
        self.assertEqual(len(self.repo.AllEvents), 1)
        self.assertEqual(len(self.repo.AllPersons), 3)
        self.assertEqual(len(self.repo.AllPersons[0].AllRegisteredEvents), 0)
        self.assertEqual(len(self.repo.AllPersons[1].AllRegisteredEvents), 1)
        self.assertEqual(len(self.repo.AllPersons[2].AllRegisteredEvents), 0)
        self.repo.deletePerson(2)


if __name__ == '__main__':
    unittest.main()
