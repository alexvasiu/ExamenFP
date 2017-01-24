"""
    Modulul de UI
"""

from Domain.Exceptions import *

class UI:
    """
        Clasa UI - se folosete pentru printare/citire date
    """
    def __init__(self, Persons, Events):
        """
            Constructor UI Class
                - se initializeaza cu Persons (PersonsController)
                - se initializeaza cu Events (EventsController)
        """
        self.__persons = Persons
        self.__events = Events

    def show(self):
        """
            Coordoneaza tot UI-ul
        """
        comands = {
            '1': self.__actionAdd,
            '2': self.__actionDelete,
            '3': self.__actionUpdate,
            '4': self.__actionSearch,
            '5': self.__actionRegister,
            '6': self.__actionReport,
            '7': self.__actionPopulate,
            '8': self.__actionLab9
        }
        self.__info()
        while True:
            self.__showMenu()
            cmd = input("Choose command : ")
            if cmd == '0':
                break
            elif '1' <= cmd <= '8':
                try :
                    comands[cmd]()
                except KeyError:
                    print("Invalid Command")
            else:
                args = cmd.split()
                if len(args) == 1 and args[0].lower() == 'exit':
                    break
                else:
                    print("Invalid Command")

    def __info(self):
        """
            Print Informations about program
        """
        print("Event Manager v1.0.0")
        print("")

    def __showMenu(self):
        """
            Print Menu
        """
        print("1 - Add")
        print("2 - Delete")
        print("3 - Update")
        print("4 - Search")
        print("5 - Register")
        print("6 - Reports")
        print("7 - Populate Persons")
        #print("8 - Lab9")
        print("0 - Exit")

    def __submenuChoose(self):
        """
            Print Submenu for Add, Delete, Update, Search
        """
        print("1 - Person")
        print("2 - Event")
        print("0 - Cancel")

    def __submenuSearchPerson(self):
        """
            Print Submenu for Search Person
        """
        print("1 - Seach By ID")
        print("2 - Seach By Name")
        print("3 - Seach By Address")
        print("0 - Cancel")

    def __submenuSearchEvent(self):
        """
            Print Submenu for Search Time
        """
        print("1 - Seach By ID")
        print("2 - Seach By Date")
        print("3 - Seach By Time")
        print("4 - Seach By DateTime")
        print("5 - Seach By Description")
        print("0 - Cancel")

    def __submenuRaports(self):
        """
            Afiseaza submeniu pentru rapoarte
        """
        print("1 - List of registered events of a person")
        print("2 - Person registered in most events")
        print("3 - First 20% events with most persons")
        print("0 - Cancel")

    def __eventsReportsSubmenu(self):
        """
            Afiseaza submeniu pentru rapoarte optiunea 1
        """
        print("1 - Order by Description")
        print("2 - Order by DateTime")
        print("0 - Cancel")

    def __readInt(self, PrintMsg, ErrorMsg):
        """
            Reads until the input is an integer and return it
        """
        while True:
            try:
                var = int(input(PrintMsg))
                break
            except ValueError:
                print(ErrorMsg)
        return var

    def __actionAdd(self):
        """
            Coordoneaza comanda add
        """
        self.__submenuChoose()
        option = input("Choose command : ")
        if option == '0':
            pass
        elif option == '1':
            ID = self.__readInt("Person ID : ", "Invalid ID")
            Name = input("Person Name : ")
            Address = input("Person Address : ")
            try:
                self.__persons.createPerson(ID, Name, Address)
                print("Person successfully added !")
            except PersonException as e:
                print(e)
        elif option == '2':
            ID = self.__readInt("Event ID : ", "Invalid ID")
            Date = input("Event Date (dd/mm/yyyy) : ")
            Time = input("Event Time (hh:mm) : ")
            Description = input("Event Description : ")
            try:
                self.__events.createEvent(ID, Date, Time, Description)
                print("Event successfully added !")
            except EventException as e:
                print(e)
        else:
            print("Invalid Command")

    def __actionDelete(self):
        """
             Coordoneaza comanda delete
        """
        self.__submenuChoose()
        option = input("Choose command : ")
        if option == '0':
            pass
        elif option == '1':
            ID = self.__readInt("Person ID : ", "Invalid ID")
            try:
                self.__persons.delete(ID)
                print("Person successfully deleted !")
            except PersonException as e:
                print(e)
        elif option == '2':
            ID = self.__readInt("Event ID : ", "Invalid ID")
            try:
                self.__events.delete(ID)
                print("Event successfully deleted !")
            except EventException as e:
                print(e)
        else:
            print("Invalid Command")

    def __actionUpdate(self):
        """
            Coordoneaza comanda update
        """
        self.__submenuChoose()
        option = input("Choose command : ")
        if option == '0':
            pass
        elif option == '1':
            ID = self.__readInt("Person ID : ", "Invalid ID")
            Name = input("Person Name : ")
            Address = input("Person Address : ")
            try:
                self.__persons.update(ID, Name, Address)
                print("Person successfully updated !")
            except PersonException as e:
                print(e)
        elif option == '2':
            ID = self.__readInt("Event ID : ", "Invalid ID")
            Date = input("Event Date (dd/mm/yyyy) : ")
            Time = input("Event Time (hh:mm) : ")
            Description = input("Event Description : ")
            try:
                self.__events.update(ID, Date, Time, Description)
                print("Event successfully updated !")
            except EventException as e:
                print(e)
        else:
            print("Invalid Command")

    def __actionSearch(self):
        """
            Coordoneaza comanda search
        """
        self.__submenuChoose()
        option = input("Choose command : ")
        if option == '0':
            pass
        elif option == '1':
            self.__submenuSearchPerson()
            opt = input("Choose command : ")
            if opt == '0':
                pass
            elif opt == '1':
                ID = self.__readInt("Person ID : ", "Invalid ID")
                try:
                    print(self.__persons.searchByID(ID))
                except PersonException as e:
                    print(e)
            elif opt == '2':
                Name = input("Person Name : ")
                try:
                    print(self.__persons.searchByName(Name))
                except PersonException as e:
                    print(e)
            elif opt == '3':
                Address = input("Person Address : ")
                try:
                    print(self.__persons.searchByAddress(Address))
                except PersonException as e:
                    print(e)
            else:
                print("Invalid Command")
        elif option == '2':
            self.__submenuSearchEvent()
            opt = input("Choose command : ")
            if opt == '0':
                pass
            elif opt == '1':
                ID = self.__readInt("Event ID : ", "Invalid ID")
                try:
                    print(self.__events.searchByID(ID))
                except EventException as e:
                    print(e)
            elif opt == '2':
                Date = input("Event Date (dd/mm/yyyy) : ")
                try:
                    print(self.__events.searchByDate(Date))
                except EventException as e:
                    print(e)
            elif opt == '3':
                Time = input("Event Time (hh:mm) : ")
                try:
                    print(self.__events.searchByTime(Time))
                except EventException as e:
                    print(e)
            elif opt == '4':
                Date = input("Event Date (dd/mm/yyyy) : ")
                Time = input("Event Time (hh:mm) : ")
                try:
                    print(self.__events.searchByDateTime(Date, Time))
                except EventException as e:
                    print(e)
            elif opt == '5':
                Description = input("Event Description : ")
                try:
                    print(self.__events.searchByDescription(Description))
                except EventException as e:
                    print(e)
            else:
                print("Invalid Command")
        else:
            print("Invalid Command")

    def __actionRegister(self):
        """
            Coordoneaza comanda register
        """
        IDpers = self.__readInt("Person ID : ", "Invalid ID")
        IDevent = self.__readInt("Event ID : ", "Invalid ID")
        try:
            self.__persons.RegisterToEvent(IDpers, self.__events.getEventByID(IDevent))
            print("Register successfully !")
        except (PersonException, EventException) as e:
            print(e)

    def __actionReport(self):
        """
            Coordoneaza comanda reports
        """
        self.__submenuRaports()
        optiune = input("Choose command : ")
        if optiune == '0':
            pass
        elif optiune == '1':
            self.__eventsReportsSubmenu()
            opt = input("Choose command : ")
            if opt == '0':
                pass
            elif opt == '1':
                ID = self.__readInt("Person ID : ", "Invalid ID")
                try:
                    print(self.__persons.personEventsOrderByDescription(ID))
                except PersonException as e:
                    print(e)
            elif opt == '2':
                ID = self.__readInt("Person ID : ", "Invalid ID")
                try:
                    print(self.__persons.personEventsOrderByDateTime(ID))
                except PersonException as e:
                    print(e)
            else:
                print("Invalid Command")
        elif optiune == '2':
            try:
                print(self.__persons.maxEvents())
            except PersonException as e:
                print(e)
        elif optiune == '3':
            try:
                print(self.__persons.PersonsToEvents())
            except PersonException as e:
                print(e)
        else:
            print("Invalid Command")

    def __actionPopulate(self):
        numar = self.__readInt("Numar entitati : ", "Invalid number")
        try:
            self.__persons.populate(numar)
            print("Populare a avut loc cu succes")
        except (PersonException, ValueError):
            print("Populare esuata")

    def __actionLab9(self):
        print(self.__persons.eventsOrderedbypersons())

