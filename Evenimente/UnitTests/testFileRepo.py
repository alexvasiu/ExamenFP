import unittest
from Domain.Events import Event
from Domain.Exceptions import PersonException
from Domain.Persons import Person
from Repository.Repo import Repo


class testFileRepo(unittest.TestCase):
    def setUp(self):
        self.repo = Repo(["persons", "events", "register"])

    def test_read(self):
        self.assertEqual(len(self.repo.AllEvents), 2)
        self.assertEqual(len(self.repo.AllPersons), 2)

    def test_alreadyRegistered(self):
        person = self.repo.AllPersons[0]
        with self.assertRaises(PersonException) as error:
            person.registerForEvent(self.repo.AllEvents[1])
        self.assertTrue("Already regiterd for this event" in str(error.exception))

    def test_properties(self):
        person = self.repo.AllPersons[0]
        self.assertEqual(person.Address, "Strada Daliei nr.2")
        self.assertEqual(int(person.PersonID), 1)
        self.assertEqual(person.Name, "Alex")
        event = self.repo.AllEvents[1]
        self.assertEqual(int(event.EventID), 2)
        self.assertEqual(event.Date, '04/08/2016')
        self.assertEqual(event.Time, "00:00")
        self.assertEqual(event.Description, "Untold Festival 2016")

    def test_StoreDeleteUpdate(self):
        event = Event(3, '22/12/2016', '22:42', "42")
        self.repo.storeEvent(event)
        self.assertEqual(len(self.repo.AllEvents), 3)
        self.repo.updateEvent(2, '22/12/2016', '23:42', "42.sh")
        event = self.repo.AllEvents[2]
        self.assertEqual(event.Date, '22/12/2016')
        self.assertEqual(event.Time, '23:42')
        self.assertEqual(event.Description, '42.sh')
        person = Person(22, "Raul", "Sibiu")
        self.repo.storePerson(person)
        self.assertEqual(len(self.repo.AllPersons), 3)
        self.repo.updatePerson(2, "Raul", "Cluj Napoca")
        person = self.repo.AllPersons[2]
        self.assertEqual(person.Address, "Cluj Napoca")
        self.assertEqual(person.Name, "Raul")
        self.repo.deletePerson(2)
        self.assertEqual(len(self.repo.AllPersons), 2)
        self.repo.deleteEvent(2)
        self.assertEqual(len(self.repo.AllEvents), 2)

if __name__ == '__main__':
    unittest.main()
