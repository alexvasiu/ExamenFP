"""
    Modulul cu clasa EventsController
"""

from Domain.Events import Event
from Domain.Exceptions import EventException


class EventsController:
    """
        clasa EventsController :
            + createEvent
            + delete
            + update
            - IndexOfEvent
            + AllEvents
            + searchByID
            + searchByTime
            + searchByDate
            + searchByDateTime
            + searchByDescription
            + getEventByID
    """
    def __init__(self, repository, validator):
        """
            constructor EventsController : se initializeaza cu validatorul si cu repository-*9ul
        """
        self.__repository = repository
        self.__validator = validator

    def createEvent(self, ID, Date, Time, Description):
        """
            adauga event daca se poate contruii un eveniment valid
            daca evenimentul exista deja, se va arunca EventException, "Event already exists"
        """
        event = Event(ID, Date, Time, Description)
        if self.__IndexOfEvent(ID) is not None:
            self.update(ID, Date, Time, Description)
        else:
            self.__validator.validateEvent(event)
            self.__repository.storeEvent(event)

    def delete(self, ID):
        """
            sterge evenimentul, daca exista evenimentul cu id-ul : ID
            daca evenimentul nu exista, se va arunca EventException, "Event not found"
        """
        index = self.__IndexOfEvent(ID)
        if index == None: raise EventException("Event not found")
        self.__repository.deleteEvent(index)

    def update(self, ID, Date, Time, Description):
        """
            editeaza evenimentul, daca exista evenimentul cu id-ul : ID, si il editeaza cu paramatri dati
            daca evenimentul nu exista, se va arunca EventException, "Event not found"
            daca un argument e vid atunci acesta nu va fi modificat
        """
        index = self.__IndexOfEvent(ID)
        if index == None: raise EventException("Event not found")
        if Date == "": Date = self.AllEvents[index].Date
        if Time == "": Time = self.AllEvents[index].Time
        if Description == "": Description = self.AllEvents[index].Description
        self.__validator.validateEvent(Event(ID, Date, Time, Description))
        self.__repository.updateEvent(index, Date, Time, Description)

    def __IndexOfEvent(self, ID):
        """
            :return : Returneaza index-ul evenimentului cu id-ul ID, se va returna None daca nu exista
        """
        index = 0
        for event in self.__repository.AllEvents:
            if int(event.EventID) == ID:
                return index
            index += 1
        return None

    @property
    def AllEvents(self):
        """
            getter pentru toate evenimentele
        """
        return self.__repository.AllEvents

    def searchByID(self, ID):
        """
            :retuneaza evenimentul sub forma de string, daca il va gasi duoa ID
            daca nu exita se va arunca EventException, "Event not found"
        """
        index = self.__IndexOfEvent(ID)
        if index == None: raise EventException("Event not found")
        return str(self.__repository.AllEvents[index])

    def searchByDate(self, Date):
        """
            :retuneaza evenimentele sub forma de string-uri, daca il va gasi dupa Data
            daca nu exita se va arunca EventException, "No event found"
        """
        index = 0
        searchResults = []
        for event in self.__repository.AllEvents:
            if str(event.Date) == Date:
                searchResults.append(str(self.__repository.AllEvents[index]))
            index += 1
        if searchResults == []:
            raise EventException("No event found")
        return searchResults

    def searchByTime(self, Time):
        """
            :retuneaza evenimentele sub forma de string-uri, daca il va gasi dupa Time
            daca nu exita se va arunca EventException, "No event found"
        """
        index = 0
        searchResults = []
        for event in self.__repository.AllEvents:
            if str(event.Time) == Time:
                searchResults.append(str(self.__repository.AllEvents[index]))
            index += 1
        if searchResults == []:
            raise EventException("No event found")
        return searchResults

    def searchByDateTime(self, Date, Time):
        """
            :retuneaza evenimentele sub forma de string-uri, daca il va gasi dupa Data si Time
            daca nu exita se va arunca EventException, "No event found"
        """
        index = 0
        searchResults = []
        for event in self.__repository.AllEvents:
            if str(event.Time) == Time and str(event.Date) == Date:
                searchResults.append(str(self.__repository.AllEvents[index]))
            index += 1
        if searchResults == []:
            raise EventException("No event found")
        return searchResults

    def searchByDescription(self, Description):
        """
            :retuneaza evenimentele sub forma de string-uri, daca il va gasi dupa Description
            daca nu exita se va arunca EventException, "No event found"
        """
        index = 0
        searchResults = []
        for event in self.__repository.AllEvents:
            if str(event.Description).lower().__contains__(Description.lower()):
                searchResults.append(str(self.__repository.AllEvents[index]))
            index += 1
        if searchResults == []:
            raise EventException("No event found")
        return searchResults

    def getEventByID(self, ID):
        """
            :retuneaza evenimentul sub forma de obiect Event, daca il va gasi dupa ID
            daca nu exita se va arunca EventException, "Event not found"
        """
        index = self.__IndexOfEvent(ID)
        if index == None: raise EventException("Event not found")
        return self.__repository.AllEvents[index]
