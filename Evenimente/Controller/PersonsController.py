"""
    Modulul cu clasa PersonsController
"""

from  Domain.Exceptions import PersonException
from Domain.Persons import Person
import random

class PersonsController:
    """
        Clasa PersonsController :
            + createPerson
            + delete
            + update
            - IndexOfPersons
            + AllPersons
            + searchByID
            + searchByName
            + searchByAddress
            + maxEvents
            + PersonsToEvents
            + personEventsOrderByDescription
            + personEventsOrderByDateTime
            + RegisterToEvent
            + getPersonByID

    """
    def __init__(self, repository, validator):
        """
            Constructor, adauga repository si validator
        """
        self.__repository = repository
        self.__validator = validator

    def createPerson(self, ID, Name, Address):
        """
            adauga persoana daca se poate contruii o persoana valida
            daca persoana exista deja, se va arunca PersonException, "Person already exists"
        """
        person = Person(ID, Name, Address)
        if self.__IndexOfPersons(ID) is not None:
            self.update(ID, Name, Address)
        else:
            self.__validator.validatePerson(person)
            self.__repository.storePerson(person)

    def delete(self, ID):
        """
           sterge persoana, daca exista persoana cu id-ul : ID
           daca persoana nu exista, se va arunca PersonException, "Person not found"
        """
        index = self.__IndexOfPersons(ID)
        if index == None: raise PersonException("Person not found")
        self.__repository.deletePerson(index)

    def update(self, ID, Name, Address):
        """
            editeaza persona, daca exista persona cu id-ul : ID, si se editeaza cu paramatri dati
            daca persona nu exista, se va arunca PersonException, "Person not found"
            daca un argument e vid atunci acesta nu va fi modificat
        """
        index = self.__IndexOfPersons(ID)
        if index == None: raise PersonException("Person not found")
        if Name == "": Name = self.AllPersons[index].Name
        if Address == "": Address = self.AllPersons[index].Address
        self.__validator.validatePerson(Person(ID, Name, Address))
        self.__repository.updatePerson(index, Name, Address)

    ############ recursive function ################
    def __IndexOfPersons(self, ID, index = 0):
        """
            :return : Returneaza index-ul persoanei cu id-ul ID, se va returna None daca nu exista
        """
        if index < len(self.__repository.AllPersons):
            if int(self.__repository.AllPersons[index].PersonID) == ID:
                return index
            else:
                return self.__IndexOfPersons(ID, index + 1)
        else:
            return None

    @property
    def AllPersons(self):
        """
            getter pentru AllPersons
        """
        return self.__repository.AllPersons

    def searchByID(self, ID):
        """
            :retuneaza persoana sub forma de string, daca o va gasi duoa ID
            daca nu exita se va arunca PersonException, "Person not found"
        """
        index = self.__IndexOfPersons(ID)
        if index == None: raise PersonException("Person not found")
        return str(self.__repository.AllPersons[index])

    def searchByName(self, Name):
        """
            :retuneaza persoanele sub forma de string-uri, daca il va gasi dupa Nume
            daca nu exita se va arunca PersonException, "No person found"
        """
        index = 0
        searchResults = []
        for person in self.__repository.AllPersons:
            if str(person.Name).lower().__contains__(Name.lower()):
                searchResults.append(str(self.__repository.AllPersons[index]))
            index += 1
        if searchResults == []:
            raise PersonException("No person found")
        return searchResults

    def searchByAddress(self, Address):
        """
            :retuneaza persoanele sub forma de string-uri, daca il va gasi dupa adresa
            daca nu exita se va arunca PersonException, "No person found"
        """
        '''
            # Complexity
                a. Time :
                    O(n) - where n is number of persons
                    iterate through all list of person and try to find persons with almost same address
                    Possible better implementation : Binary Search - O(LOG2 N)
                b. Space
                    O(m) - where m will be the length of list result
                    This is the best complexity for space
                    Best case : O(1)
        '''
        index = 0
        searchResults = []
        for person in self.__repository.AllPersons:
            if str(person.Address).lower().__contains__(Address.lower()):
                searchResults.append(str(self.__repository.AllPersons[index]))
            index += 1
        if searchResults == []:
            raise PersonException("No person found")
        return searchResults

    def maxEvents(self):
        """
            Returneaza persoanele participante la cele mai multe evenimente
            Daca nu exita, se va arunca PersonException "No persons to events"
        """
        persons = []
        maxEvents = -1
        for person in self.AllPersons:
            if len(person.AllRegisteredEvents) > maxEvents:
                persons = [str(person)]
            elif len(person.AllRegisteredEvents) == maxEvents:
                persons.append(str(person))
        if persons == []: raise PersonException("No persons to events")
        return persons

    def PersonsToEvents(self):
        """
            Primele 20% evenimente cu cei mai multi participanti
            Daca nu exista se va arunca PersonException "No persons to events"
        """
        events = {}
        for person in self.AllPersons:
            for event in person.AllRegisteredEvents:
                if events.__contains__(int(event.EventID)):
                    events[int(event.EventID)][0] += 1
                else:
                    events[int(event.EventID)] = [1, event.Description]
        result = []
        nr = len(events) // 5
        for event in reversed(sorted(events)):
            if nr == 0: break
            result.append(events[event])
            nr -= 1
        if result == []: raise PersonException("No persons to events")
        return result

    def personEventsOrderByDescription(self, ID):
        """
            Returneaza lista de evenimente la care participa o persoana data de ID
            ordonat alfabetic dupa descriere
            Daca persona nu exista, se va arunca PersonException "Person not found"
            Daca nu este inregistrat la niciun eveniment, se va arunca PersonException "No registered event"
        """
        index = self.__IndexOfPersons(ID)
        if index == None: raise PersonException("Person not found")
        result = self.__repository.AllPersons[index].RegisteredEventsByDescription
        if len(result) == 0: raise PersonException("No registered event")
        return result

    def personEventsOrderByDateTime(self, ID):
        """
            Returneaza lista de evenimente la care participa o persoana data de ID
            ordonat dupa DataTime
            Daca persona nu exista, se va arunca PersonException "Person not found"
            Daca nu este inregistrat la niciun eveniment, se va arunca PersonException "No registered event"
        """
        index = self.__IndexOfPersons(ID)
        if index == None: raise PersonException("Person not found")
        result = self.__repository.AllPersons[index].RegisteredEventsByDateTime
        if len(result) == 0: raise PersonException("No registered event")
        return result

    def RegisterToEvent(self, IDPers, Event):
        """
            Inregistreaza persoana cu id-ul, IDPers la Event-ul dat
            Daca persoana nu exista, se va arunca PersonException "Person not found"
        """
        index = self.__IndexOfPersons(IDPers)
        if index == None: raise PersonException("Person not found")
        self.__repository.AllPersons[index].registerForEvent(Event)
        self.__repository.storeRegitered(IDPers, Event.EventID)

    def getPersonByID(self, ID):
        """
            :retuneaza persoana sub forma de obiect Person, daca il va gasi dupa ID
            daca nu exita se va arunca PersonException, "Person not found"
        """
        index = self.__IndexOfPersons(ID)
        if index == None: raise PersonException("Person not found")
        return self.__repository.AllPersons[index]

    def populate(self, n):
        """
            Populare repository cu Persoane random
        """

        alphabet = "abcdefghijklmnopqrstuvxyz"
        while n > 0:
            self.createPerson(random.randrange(100, 20000000),
            ''.join(random.choice(alphabet + alphabet.upper()) for _ in range(random.randrange(5, 30))),
            ''.join(random.choice(alphabet + alphabet.upper() + "0123456789. ") for _ in range(random.randrange(20, 80))))
            n -= 1

    ############ recursive function ################
    def eventsOrderedbypersons(self, index=0, dic={}):
        """
            Returneaza of lista cu datale ordonate descrescator dupa numarul de participanti in aceea zi
        """
        if index < len(self.__repository.AllPersons):
            for event in self.__repository.AllPersons[index].AllRegisteredEvents:
                if dic.__contains__(event.Date):
                    dic[event.Date] += 1
                else:
                    dic[event.Date] = 1
            return self.eventsOrderedbypersons(index + 1, dic)
        else:
            return list(reversed(sorted(dic, key=dic.__getitem__)))
