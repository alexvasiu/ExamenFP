import unittest
from Domain.Events import Event
from Domain.Persons import Person
from Repository.RepoMemory import RepoMemory


class testMemoryRepo(unittest.TestCase):
    def setUp(self):
        self.repo = RepoMemory()

    def test_store(self):
        self.assertEqual(len(self.repo.AllEvents), 0)
        self.assertEqual(len(self.repo.AllPersons), 0)
        self.repo.storeEvent(Event(1, '22/12/2015', '22:22', 'dsadsadsadsa'))
        self.assertEqual(len(self.repo.AllEvents), 1)
        self.assertEqual(len(self.repo.AllPersons), 0)
        self.repo.storePerson(Person(1, '22/12/2015', '22:22'))
        self.assertEqual(len(self.repo.AllPersons), 1)
        self.assertEqual(len(self.repo.AllEvents), 1)

    def test_delete(self):
        event = Event(1, '22/12/2015', '22:22', 'dsadsadsadsa')
        self.repo.storeEvent(event)
        self.repo.deleteEvent(0)
        self.assertEqual(len(self.repo.AllEvents), 0)

if __name__ == '__main__':
    unittest.main()
