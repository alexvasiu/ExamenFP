"""
    Moudul de teste
"""
from Controller.EventsController import EventsController
from Controller.PersonsController import PersonsController
from Domain.Events import Event
from Domain.Exceptions import *
from Domain.Persons import Person
from Domain.Validator import Validator
from Repository.DatabaseRepo import RepoDB
from Repository.Repo import Repo
from Repository.RepoMemory import RepoMemory


class Tests:
    def run_all(self):
        """
        Se ruleaza toate testele
        """
        self.__testPersons()
        self.__testEvents()
        self.__testValidator()
        self.__testExpections()
        self.__testEventsController()
        self.__testPersonsController()
        self.__testRepo()
        self.__testRepoDB()
        self.__testRepoMemory()

    def __testPersons(self):
        """
            Se testeaza functionalitatea clasei Person
        """
        p = Person(10, "Alex", "Strada Daliei nr.2")
        assert p.Name == "Alex"
        assert p.PersonID == 10
        assert p.Address == "Strada Daliei nr.2"
        assert p.AllRegisteredEvents == []
        p.setAddress("A")
        assert p.Address == "A"
        p.setID(11)
        assert p.PersonID == 11
        p.setName("ALEX")
        assert p.Name == "ALEX"
        p = Person(10, "Alex", "Strada Daliei nr.2")
        assert str(p) == "10 Alex Strada Daliei nr.2"
        p1 = Person(10, "Aledsdsx", "Strada Daliei nr.2")
        assert p == p1

    def __testEvents(self):
        """
            Se testeaza functionalitatea clasei Event
        """
        e = Event(10, "22/12/2016", "22:42", "Limit 1")
        assert e.EventID == 10
        assert e.Date == "22/12/2016"
        assert e.Description == "Limit 1"
        assert e.Time == "22:42"
        e.setID(11)
        e.setDate("23/12/2016")
        e.setTime("23:42")
        e.setDescription("Limit 2")
        assert e.EventID == 11
        assert e.Date == "23/12/2016"
        assert e.Description == "Limit 2"
        assert e.Time == "23:42"
        assert str(e) == "11 23/12/2016 23:42 Limit 2"
        e1 = Event(11, "", "", "")
        assert e == e1

    def __testValidator(self):
        """
            Se testeaza functionalitatea clasei Validator
        """
        person = Person(-10, "", "")
        validator = Validator()
        try:
            validator.validatePerson(person)
            assert False
        except PersonException as e:
            assert e.errors == ["ID cannot be negative", "Name cannot be empty", "Address cannot be empty"]
        person = Person("dsd", "dsa", "dsada")
        try:
            validator.validatePerson(person)
            assert False
        except PersonException as e:
            assert e.errors == ["ID should be a number"]
        event = Event(10, '22/12/2012', '22:42', 'DSADSAA')
        try:
            validator.validateEvent(event)
            assert True
        except EventException:
            assert False
        event = Event(10, '2/02/2012', '2242', '')
        try:
            validator.validateEvent(event)
            assert False
        except EventException as e:
            assert e.errors == ["Invalid time format", "Description cannot be empty"]
        event = Event(-10, '2/24/2012', '22:42', 'dasd')
        try:
            validator.validateEvent(event)
            assert False
        except EventException as e:
            assert e.errors == ["ID cannot be negative", "Invalid date format"]

    def __testExpections(self):
        """
            Se testeaza functionalitatea Exceptiilor
        """
        try:
            raise PersonException("Person exception")
        except (PersonException, EventException, DatabaseException) as e:
            assert e.errors == "Person exception"
            assert type(e) == PersonException
        try:
            raise EventException("Event exception")
        except (PersonException, EventException, DatabaseException) as e:
            assert e.errors == "Event exception"
            assert type(e) == EventException
        try:
            raise DatabaseException("Database error")
        except (PersonException, EventException, DatabaseException) as e:
            assert e.errors == "Database error"
            assert type(e) == DatabaseException

    def __testEventsController(self):
        """
            Se testeaza functionalitatea clasei EventsController
        """
        repo = Repo(["Tests/persons", "Tests/events", "Tests/register"])
        validator = Validator()
        controller = EventsController(repo, validator)
        event = Event(1000427, '22/10/2015', '22:23', "dsada")
        controller.createEvent(1000427, '22/10/2015', '22:23', "dsada")
        assert controller.AllEvents.__contains__(event)
        controller.update(1000427, '22/10/2016', '22:23', "dddd")
        assert controller.getEventByID(1000427).Date == '22/10/2016'
        assert controller.getEventByID(1000427).Description == 'dddd'
        assert controller.getEventByID(1000427).Time == '22:23'
        assert controller.AllEvents == repo.AllEvents
        assert controller.searchByID(1000427) == "1000427 22/10/2016 22:23 dddd"
        try:
            controller.searchByDate('323232')
            assert False
        except EventException as e:
            assert e.errors == "No event found"
        assert controller.searchByDescription("dddd").__contains__(str(controller.getEventByID(1000427)))
        assert controller.searchByTime("22:23").__contains__(str(controller.getEventByID(1000427)))
        controller.update(1000427, '22/10/2015', '22:23', "dsada")
        assert controller.getEventByID(1000427) == event
        controller.delete(1000427)
        assert not controller.AllEvents.__contains__(event)
        try:
            controller.createEvent("10", "dsdsadas","22:32", "dd")
            assert False
        except (PersonException, EventException) as e:
            assert type(e) == EventException

    def __testPersonsController(self):
        """
            Se testeaza functionalitatea clasei PersonsController
        """
        repo = Repo(["Tests/persons", "Tests/events", "Tests/register"])
        validator = Validator()
        controller = PersonsController(repo, validator)
        controller_events = EventsController(repo, validator)
        person = Person(9991119, "Alex", "Daliei nr.2")
        controller.createPerson(9991119, "Alex", "Daliei nr.2")
        assert person == controller.getPersonByID(9991119)
        controller.update(9991119, "Alex", "Cluj")
        assert controller.getPersonByID(9991119).Name == "Alex"
        assert controller.getPersonByID(9991119).Address == "Cluj"
        assert controller.AllPersons == repo.AllPersons
        try:
            controller.searchByID(321803821038210381203812903812330213099)
            assert False
        except (EventException,PersonException) as e:
            assert e.errors == "Person not found"
            assert type(e) == PersonException
        controller.update(9991119, "Alex", "Daliei nr.2")
        assert controller.searchByName("Alex").__contains__(str(person))
        assert controller.searchByAddress("Daliei").__contains__(str(person))
        for i in range(999999999899, 999999999999):
            controller_events.createEvent(i, "22/12/2016", '22:22', "dsadaa")
            controller.getPersonByID(9991119).registerForEvent(controller_events.getEventByID(i))
        l = []
        l.append(str(controller.searchByID(9991119)))
        assert controller.maxEvents() == l
        for i in range(999999999899, 999999999999):
            controller_events.delete(i)
        controller_events.createEvent(999999999999, "21/12/2013", '22:22', "dasdsad")
        controller.getPersonByID(9991119).registerForEvent(controller_events.getEventByID(999999999999))
        controller_events.createEvent(999999999998, "22/12/2013", '22:22', "aasdsad")
        controller.getPersonByID(9991119).registerForEvent(controller_events.getEventByID(999999999998))
        assert controller.personEventsOrderByDescription(9991119) == ['999999999998 22/12/2013 22:22 aasdsad',
                                                             '999999999999 21/12/2013 22:22 dasdsad']
        assert controller.personEventsOrderByDateTime(9991119) ==  ['999999999999 21/12/2013 22:22 dasdsad',
                                                                     '999999999998 22/12/2013 22:22 aasdsad']
        controller_events.delete(999999999999)
        controller_events.delete(999999999998)
        controller.delete(9991119)
        assert not controller.AllPersons.__contains__(person)

    def __testRepo(self):
        """
            Se testeaza functionalitatea clasei Repo (cu fisiere)
        """
        repo = Repo(["Tests/persons", "Tests/events", "Tests/register"])
        assert len(repo.AllEvents) == 2
        assert len(repo.AllPersons) == 2
        person = repo.AllPersons[0]
        try:
            person.registerForEvent(repo.AllEvents[1])
            assert False
        except (PersonException,DatabaseException, EventException) as e:
            assert e.errors == "Already regiterd for this event"
            assert type(e) == PersonException
        assert person.Address == "Strada Daliei nr.2"
        assert int(person.PersonID) == 1
        assert person.Name == "Alex"
        event = repo.AllEvents[1]
        assert int(event.EventID) == 2
        assert event.Date == '04/08/2016'
        assert event.Time == "00:00"
        assert event.Description == "Untold Festival 2016"
        event = Event(3, '22/12/2016', '22:42', "42")
        repo.storeEvent(event)
        assert len(repo.AllEvents) == 3
        repo.updateEvent(2, '22/12/2016', '23:42', "42.sh")
        event = repo.AllEvents[2]
        assert event.Date == '22/12/2016'
        assert event.Time == '23:42'
        assert event.Description == '42.sh'
        person = Person(22, "Raul", "Sibiu")
        repo.storePerson(person)
        assert len(repo.AllPersons) == 3
        repo.updatePerson(2, "Raul", "Cluj Napoca")
        person = repo.AllPersons[2]
        assert person.Address == "Cluj Napoca"
        assert person.Name == "Raul"
        repo.deletePerson(2)
        assert len(repo.AllPersons) == 2
        repo.deleteEvent(2)
        assert len(repo.AllEvents) == 2

    def __testRepoDB(self):
        """
            Se testeaza functionalitatea clasei RepoDB (cu baza de date)
        """
        repo = RepoDB("Tests/TestRepo.sqlite")
        assert len(repo.AllEvents) == 1
        assert len(repo.AllPersons) == 2
        assert len(repo.AllPersons[1].AllRegisteredEvents) == 1
        assert len(repo.AllPersons[0].AllRegisteredEvents) == 0
        try:
            repo.AllPersons[1].registerForEvent(repo.AllEvents[0])
            assert False
        except (PersonException, DatabaseException, EventException) as e:
            assert type(e) == PersonException
            assert e.errors == "Already regiterd for this event"
        event = Event(123, '22/12/2016', '22:22', 'Dsdadd dksldklsa')
        person = Person(144, "Alex", "CLUJ")
        repo.storeEvent(event)
        repo.storePerson(person)
        repo.AllPersons[2].registerForEvent(repo.AllEvents[1])
        assert len(repo.AllEvents) == 2
        assert len(repo.AllPersons) == 3
        assert len(repo.AllPersons[0].AllRegisteredEvents) == 0
        assert len(repo.AllPersons[1].AllRegisteredEvents) == 1
        assert len(repo.AllPersons[2].AllRegisteredEvents) == 1
        repo.updatePerson(2, "Alex Vasiu", "Cluj")
        repo = RepoDB("Tests/TestRepo.sqlite")
        assert repo.AllPersons[2].Name == "Alex Vasiu"
        assert repo.AllPersons[2].Address == "Cluj"
        repo.deleteEvent(1)
        assert len(repo.AllEvents) == 1
        assert len(repo.AllPersons) == 3
        assert len(repo.AllPersons[0].AllRegisteredEvents) == 0
        assert len(repo.AllPersons[1].AllRegisteredEvents) == 1
        assert len(repo.AllPersons[2].AllRegisteredEvents) == 0
        repo.deletePerson(2)

    def __testRepoMemory(self):
        """
            Se testeaza functionalitatea clasei RepoMemory (in memorie)
        """
        repo = RepoMemory()
        assert len(repo.AllEvents) == 0
        assert len(repo.AllPersons) == 0
        repo.storeEvent(Event(1, '22/12/2015', '22:22', 'dsadsadsadsa'))
        assert len(repo.AllEvents) == 1
        assert len(repo.AllPersons) == 0
        repo.storePerson(Person(1, '22/12/2015', '22:22'))
        assert len(repo.AllPersons) == 1
        assert len(repo.AllEvents) == 1