"""
    Modulul pentru clasa persoana
"""

import datetime
from Utils import Sort
from Domain.Exceptions import PersonException


class Person:
    """
        Clasa Person :
            + Name
            + PersonID
            + Address
            + setAddress
            + setName
            + setID
            + registerForEvent
            + AllRegisteredEvents
            + deleteEvent
            + RegisteredEventsByDescription
            + RegisteredEventsByDateTime
            - str
            - eq
    """
    def __init__(self, personID, name, address):
        """
            Initializare persoana cu ID, nume, adresa
        """
        self.__address = address
        self.__personID = personID
        self.__name = name
        self.__events = []

    @property
    def Name(self):
        """
            getter pentru Nume
        """
        return self.__name

    @property
    def PersonID(self):
        """
            getter pentru ID
        """
        return self.__personID

    @property
    def Address(self):
        """
            getter pentru adresa
        """
        return self.__address

    def setAddress(self, address):
        """
            setter pentru adresa
        """
        self.__address = address

    def setName(self, name):
        """
            setter pentru nume
        """
        self.__name = name

    def setID(self, ID):
        """
            setter pentru ID
        """
        self.__personID = ID

    def registerForEvent(self, Event):
        """
              inregistrare persoana la event
        """
        if self.__events.__contains__(Event): raise PersonException("Already regiterd for this event")
        self.__events.append(Event)

    @property
    def AllRegisteredEvents(self):
        """
            getter pentru evenimentele inregisrate
        """
        return self.__events

    def deleteEvent(self, Event):
        """
            delete un eveniment la care e inregistrat
        """
        if self.__events.__contains__(Event):
            self.__events.remove(Event)

    @property
    def RegisteredEventsByDescription(self):
        """
            getter pentru evenimentele inregisrate sortate dupa descriere
        """
        return list(map(str, Sort.QuickSort(self.__events, key=lambda event: event.Description.lower())))


    @property
    def RegisteredEventsByDateTime(self):
        """
             getter pentru evenimentele inregisrate dupa Data
        """
        return list(map(str, Sort.GnomeSort(self.__events, key=lambda event: datetime.datetime.strptime(event.Date, "%d/%m/%Y"))))

    def __str__(self):
        """
            override functia str, str(Persoana) = ID + " " + NUME + " " + Adresa
        """
        return "{0} {1} {2}".format(self.__personID, self.__name, self.__address)

    def __eq__(self, other):
        """
            override =, 2 persoane sunt egale daca au acelasi ID
        """
        return isinstance(other, Person) and self.__personID == other.__personID
