"""
    Modulul cu clasa Eveniment
"""

class Event:
    """
     clasa Event :
        + EventID
        + Date
        - eq
        + Date
        + Time
        + Description
        + setDate
        + setTime
        + setDescription
        + setID
        - str
    """
    def __init__(self, eventID, date, time, description):
        """
            Initializare Event cu ID, data, timp si descriere
        """
        self.__eventID = eventID
        self.__date = date
        self.__time = time
        self.__description = description

    @property
    def EventID(self):
        """
            getter pentru ID
        """
        return self.__eventID

    def __eq__(self, other):
        """
            override = , doua evenimente sunt egale daca au acelasi ID
        """
        return isinstance(other, Event) and self.__eventID == other.__eventID

    @property
    def Date(self):
        """
            getter pentru Data
        """
        return self.__date

    @property
    def Time(self):
        """
            getter pentru Timp
        """
        return self.__time

    @property
    def Description(self):
        """
            getter pentru descriere
        """
        return self.__description

    def setDate(self, date):
        """
            setter pentru data
        """
        self.__date = date

    def setTime(self, time):
        """
            setter pentru Timp
        """
        self.__time = time

    def setDescription(self, description):
        """
            setter pentru Descriere
        """
        self.__description = description

    def setID(self, ID):
        """
            setter pentru ID
        """
        self.__eventID = ID

    def __str__(self):
        """
            override functia str, str(event) = ID + " " + data + " " + timp + " " + descriere
        """
        return "{0} {1} {2} {3}".format(self.__eventID, self.__date, self.__time, self.__description)