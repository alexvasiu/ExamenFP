"""
    Modul pentru Repository cu fisiere
"""

from Domain.Persons import Person
from Domain.Events import Event

class Repo:
    """
        Clasa de Repo (cu fisiere) :
            - load
            + Persons
            + Events
            + save
            + storeRegitered
            + storePerson
            + storeEvent
            - appendLine
            + deleteEvent
            + deletePerson
            + updateEvent
            + updatePerson
            + AllPersons
            + AllEvents
            - getEventByID
            - getPersonByID
            - IndexOfPersons
            - IndexOfEvent
    """
    def __init__(self, filenames):
        """
            constructor : se initializeaza cu numele fisierului
            se apeleaza functia __load pentru a incarca in __persons si in __events
        """
        self.__filenames = filenames
        self.__persons = []
        self.__events = []
        self.__load()

    def __load(self):
        """
            Incarca datele din fisiere
        """
        try:
            file_persons = open(self.__filenames[0])
            file_events = open(self.__filenames[1])
            file_regiter = open(self.__filenames[2])
            lines = file_persons.read().split('\n')
            for line in lines:
                if line.strip() == '':
                    continue
                args = line.split()
                if len(args) >= 3:
                    self.__persons.append(Person(args[0], args[1], " ".join(args[2:])))
            file_persons.close()
            lines = file_events.read().split('\n')
            for line in lines:
                if line.strip() == '':
                    continue
                args = line.split()
                if len(args) >= 4:
                    self.__events.append(Event(args[0], args[1], args[2], " ".join(args[3:])))
            file_events.close()
            lines = file_regiter.read().split('\n')
            for line in lines:
                if line.strip() == '':
                    continue
                args = line.split()
                if len(args) == 2:
                    try:
                        args[0], args[1] = int(args[0]), int(args[1])
                        event = self.__getEventByID(args[1])
                        person = self.__getPersonByID(args[0])
                        if event is not None and person is not None:
                            person.registerForEvent(event)
                    except:
                        pass
            file_regiter.close()
        except:
            raise ValueError("Cannot load file")

    @property
    def Persons(self):
        """
            getter pentru Persons
        """
        return self.__persons

    @property
    def Events(self):
        """
            getter pentru Events
        """
        return self.__events

    def save(self):
        """
            salveaza datele in fisier
        """
        try:
            file_persons = open(self.__filenames[0], 'w')
            file_events = open(self.__filenames[1], 'w')
            file_regiter = open(self.__filenames[2], 'w')
            for person in self.__persons:
                file_persons.write(str(person) + "\n")
                for event in person.AllRegisteredEvents:
                    file_regiter.write("{0} {1}\n".format(person.PersonID, event.EventID))
            for event in self.__events:
                file_events.write(str(event) + "\n")
            file_persons.close()
            file_events.close()
            file_regiter.close()
        except:
            raise ValueError("Cannot save")

    def storeRegitered(self, PersonID, EventID):
        """
            resalvarea datelor pentru ca o persoana a fost inregistrata
        """
        self.save()

    def storePerson(self, person):
        """
            salveza persona
        """
        self.__persons.append(person)
        self.__appendLine("{0}\n".format(str(person)), self.__filenames[0])

    def storeEvent(self, event):
        """
            salvare Event
        """
        self.__events.append(event)
        self.__appendLine("{0}\n".format(str(event)), self.__filenames[1])

    def __appendLine(self, line, filename):
        """
            adauga o linie in fisier
        """
        with open(filename, "a") as myfile:
            myfile.write(line)

    def deleteEvent(self, index):
        """
            sterge eveniment din repo
        """
        for person in self.__persons:
            person.deleteEvent(self.__events[index])
        del self.__events[index]
        self.save()

    def deletePerson(self, index):
        """
            sterge persona din repo
        """
        del self.__persons[index]
        self.save()

    def updateEvent(self, index, Date, Time, Description):
        """
            update eveniment in repo
        """
        self.__events[index].setDate(Date)
        self.__events[index].setTime(Time)
        self.__events[index].setDescription(Description)
        self.save()

    def updatePerson(self, index, Name, Address):
        """
            update persoana in repo
        """
        self.__persons[index].setName(Name)
        self.__persons[index].setAddress(Address)
        self.save()

    @property
    def AllPersons(self):
        """
            getter AllPersons
        """
        return self.__persons

    @property
    def AllEvents(self):
        """
            getter AllEvents
        """
        return self.__events

    def __getEventByID(self, ID):
        """
            :retuneaza evenimentul sub forma de obiect Event, daca il va gasi dupa ID
            daca nu exita se va returna None
        """
        index = self.__IndexOfEvent(ID)
        if index == None: return None
        return self.AllEvents[index]

    def __IndexOfEvent(self, ID):
        """
            :return : Returneaza index-ul evenimentului cu id-ul ID, se va returna None daca nu exista
        """
        index = 0
        for event in self.__events:
            if int(event.EventID) == ID:
                return index
            index += 1
        return None

    def __getPersonByID(self, ID):
        """
            :retuneaza persoana sub forma de obiect Person, daca il va gasi dupa ID
            daca nu exita se va returna None
        """
        index = self.__IndexOfPersons(ID)
        if index == None: return None
        return self.AllPersons[index]

    def __IndexOfPersons(self, ID):
        """
            :return : Returneaza index-ul persoanei cu id-ul ID, se va returna None daca nu exista
        """
        index = 0
        for person in self.__persons:
            if int(person.PersonID) == ID:
                return index
            index += 1
        return None