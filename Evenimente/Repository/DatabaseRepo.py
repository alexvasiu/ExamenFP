"""
    Modulul pentru repository cu baza de date
"""

import sqlite3

from Domain.Events import Event
from Domain.Exceptions import DatabaseException
from Domain.Persons import Person


class RepoDB:
    """
        Clasa RepoDB(cu baza de date) :
            + AllPersons
            + AllEvents
            - loadDatabase
            - saveDatabase
            + storePerson
            + storeEvent
            + deleteEvent
            + deletePerson
            + updateEvent
            + updatePerson
            + storeRegitered
            - getEventByID
            - getPersonByID
            - IndexOfPersons
            - IndexOfEvent
    """
    def __init__(self, datebase):
        """
            constructor : se initializeaza cu baza de date
            se apeleaza __loadDatabase
        """
        self.__persons = []
        self.__events = []
        self.__database = datebase
        self.__loadDatabase()

    def __loadDatabase(self):
        """
            citeste si incarca datele din baza de date
        """
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                cmd = cursor.execute("SELECT * FROM Persons")
                while True:
                    line = cmd.fetchone()
                    if line is None: break
                    person = Person(line[0], line[1], line[2])
                    self.__persons.append(person)
                cmd = cursor.execute("SELECT * FROM Events")
                while True:
                    line = cmd.fetchone()
                    if line is None: break
                    event = Event(line[0], line[1], line[2], line[3])
                    self.__events.append(event)
                cmd = cursor.execute("SELECT * FROM Regitered")
                while True:
                    line = cmd.fetchone()
                    if line is None: break
                    event = self.__getEventByID(line[1])
                    person = self.__getPersonByID(line[0])
                    if event is not None and person is not None:
                        person.registerForEvent(event)
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")

    def __saveDatabase(self):
        """
            salveaza toate datele in baza de date
        """
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                for person in self.__persons:
                    ID = (person.PersonID,)
                    params = (person.PersonID, person.Name, person.Address)
                    cmd = cursor.execute("SELECT * FROM Persons WHERE PersonID=?", ID)
                    if cmd.fetchone() != params:
                        cursor.execute("INSERT INTO Persons VALUES(?, ?, ?)", params)
                for event in self.__events:
                    ID = (event.EventID,)
                    params = (event.EventID, event.Date, event.Time, event.Description)
                    cmd = cursor.execute("SELECT * FROM Events WHERE EventID=?", ID)
                    if cmd.fetchone() != params:
                        cursor.execute("INSERT INTO Events VALUES(?, ?, ?, ?)", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")

    def storePerson(self, person):
        """
            salveaza persoana in repo
        """
        self.__persons.append(person)
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                params = (person.PersonID, person.Name, person.Address)
                cursor.execute("INSERT INTO Persons VALUES(?, ?, ?)", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")

    def storeEvent(self, event):
        """
            salveaza event in repo
        """
        self.__events.append(event)
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                params = (event.EventID, event.Date, event.Time, event.Description)
                cursor.execute("INSERT INTO Events VALUES(?, ?, ?, ?)", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")

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

    def deleteEvent(self, index):
        """
            sterge eveniment si legaturile acestuia cu persoanele inregistrale la el
        """
        for person in self.__persons:
            person.deleteEvent(self.__events[index])
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                params = (self.__events[index].EventID,)
                cursor.execute("DELETE FROM Events WHERE EventID=?", params)
                cursor.execute("DELETE FROM Regitered WHERE EventID=?", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")
        del self.__events[index]

    def deletePerson(self, index):
        """
             sterge persona din repo si legaturile acestuia cu evenimentele
        """
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                params = (self.__persons[index].PersonID, )
                cursor.execute("DELETE FROM Persons WHERE PersonID=?", params)
                cursor.execute("DELETE FROM Regitered WHERE PersonID=?", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")
        del self.__persons[index]

    def updateEvent(self, index, Date, Time, Description):
        """
            update evenimentului de la pozitia index din AllEvents cu parametrii dati
        """
        self.__events[index].setDate(Date)
        self.__events[index].setTime(Time)
        self.__events[index].setDescription(Description)
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                params = (Date, Time, Description, self.__events[index].EventID)
                cursor.execute("UPDATE Events SET Date = ?, Time = ?, Description = ? WHERE EventID=?", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")

    def updatePerson(self, index, Name, Address):
        """
            update persoanei de la pozitia index din AllEvents cu parametrii dati
        """
        self.__persons[index].setName(Name)
        self.__persons[index].setAddress(Address)
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                params = (Name, Address, self.__persons[index].PersonID)
                cursor.execute("UPDATE Persons SET Name = ?, Address = ? WHERE PersonID=?", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")

    def storeRegitered(self, PersonID, EventID):
        """
            inregistreaza legatura persoana-event in baza de date
        """
        try:
            if self.__database is not None:
                con = sqlite3.connect(self.__database)
                cursor = con.cursor()
                params = (PersonID, EventID)
                cursor.execute("INSERT INTO Regitered VALUES(?, ?)", params)
                con.commit()
                cursor.close()
                con.close()
        except:
            raise DatabaseException("Database error")

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