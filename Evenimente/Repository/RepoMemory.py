"""
    Modul pentru Repository cu memorie
"""

from Domain.Persons import Person
from Domain.Events import Event

class RepoMemory:
    """
        Clasa de Repo (memorie) :
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
    def __init__(self):
        """
            constructor : se initializeaza cu numele fisierului
            se apeleaza functia __load pentru a incarca in __persons si in __events
        """
        self.__persons = []
        self.__events = []

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


    def storePerson(self, person):
        """
            salveza persona
        """
        self.__persons.append(person)

    def storeEvent(self, event):
        """
            salvare Event
        """
        self.__events.append(event)


    def deleteEvent(self, index):
        """
            sterge eveniment din repo
        """
        for person in self.__persons:
            person.deleteEvent(self.__events[index])
        del self.__events[index]

    def deletePerson(self, index):
        """
            sterge persona din repo
        """
        del self.__persons[index]

    def updateEvent(self, index, Date, Time, Description):
        """
            update eveniment in repo
        """
        self.__events[index].setDate(Date)
        self.__events[index].setTime(Time)
        self.__events[index].setDescription(Description)

    def updatePerson(self, index, Name, Address):
        """
            update persoana in repo
        """
        self.__persons[index].setName(Name)
        self.__persons[index].setAddress(Address)

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

    def storeRegitered(self, PersonID, EventID):
        """
            sa functioneze si pentru celelate Repo-uri
        """
        pass

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