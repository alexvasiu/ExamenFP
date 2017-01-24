"""
    Modulul pentru clasa Validator
"""

import datetime

from Domain.Exceptions import *

class Validator:
    """
        clasa Validator :
            + validatePerson
            + validate Event
            - canConvertToInt
            - canBeDate
    """

    def validatePerson(self, person):
        """
            Validare persona :
                - ID numar pozitiv
                - Nume nevid
                - Adresa nevida
        """
        errors = []
        if not self.__canConvertToInt(person.PersonID) or type(person.PersonID) == str:
            errors.append("ID should be a number")
        elif person.PersonID < 0: errors.append("ID cannot be negative")
        if person.Name == "": errors.append("Name cannot be empty")
        if person.Address == "": errors.append("Address cannot be empty")
        if len(errors):
            raise PersonException(errors)

    def validateEvent(self, event):
        """
            Validare Eveniment :
                - ID numar pozitiv
                - Data de forma 'dd/mm/yyyy'
                - Timp de forma 'hh:mm'
                - Descriere nevida
        """
        errors = []
        if not self.__canConvertToInt(event.EventID) or type(event.EventID) == str: errors.append("ID should be a number")
        elif event.EventID < 0: errors.append("ID cannot be negative")
        if event.Date == "": errors.append("Date cannot be empty")
        if event.Time == "": errors.append("Time cannot be empty")
        DateParts = event.Date.split('/')
        if not (len(DateParts) is 3 and len(DateParts[0]) <= 2 and len(DateParts[1]) <= 2 and len(DateParts[2]) == 4 and
                self.__canConvertToInt(DateParts[0]) and self.__canConvertToInt(DateParts[1]) and
                self.__canConvertToInt(DateParts[2]) and
                self.__canBeDate(int(DateParts[2]), int(DateParts[1]), int(DateParts[0]), 0, 0)):
            errors.append("Invalid date format")
        TimeParts = event.Time.split(':')
        if not (len(TimeParts) is 2 and len(TimeParts[0]) == 2 and len(TimeParts[1]) == 2 and
                self.__canConvertToInt(TimeParts[0]) and self.__canConvertToInt(TimeParts[1]) and
                self.__canBeDate(2016, 1, 1, int(TimeParts[0]), int(TimeParts[1]))):
            errors.append("Invalid time format")
        if event.Description == "": errors.append("Description cannot be empty")
        if len(errors):
            raise EventException(errors)

    def __canConvertToInt(self, value):
        """
            returneaza True daca value poate fi numar intreg, altfel False
        """
        try:
            value = int(value)
            return True
        except ValueError:
            return False

    def __canBeDate(self, year, month, day, hours, minutes):
        """
            returneaza True daca  parametri pot constituii o data valida, altfel False
        """
        try:
            date = datetime.datetime(year, month, day, hours, minutes, 0)
            return True
        except ValueError:
            return False