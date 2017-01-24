"""
    Modul pentru exceptii
"""

class EventException(Exception):
    """
        Exceptii pentru Events
    """
    def __init__(self, errors):
        """
            constructor
        """
        self.errors = errors

    def getErrors(self):
        """
            getter pentru errori
        """
        return self.errors

class PersonException(Exception):
    """
        Exceptii pentru Persons
    """
    def __init__(self, errors):
        """
            constructor
        """
        self.errors = errors

    def getErrors(self):
        """
            getter pentru errori
        """
        return self.errors

class DatabaseException(Exception):
    """
        Exceptii pentru baza de date
    """
    def __init__(self, errors):
        """
            constructor
        """
        self.errors = errors

    def getErrors(self):
        """
            getter pentru errori
        """
        return self.errors