"""
    Domain Layer : Tema
"""
class Tema:
    """
        Clasa Tema
    """
    def __init__(self, id, nume, rezolvare):
        """
             initalizare cu id, nume student si rezolvare
        """
        self.__ID = id
        self.__nume_student = nume
        self.__rezolvare = rezolvare

    @property
    def getID(self):
        """
            getter pentru ID
        """
        return self.__ID

    @property
    def getNumeStudent(self):
        """
           getter pentru nume student
        """
        return self.__nume_student

    @property
    def getRezolvare(self):
        """
            getter pentru rezolvare
        """
        return self.__rezolvare

    def setID(self, ID):
        """
            setter pentru ID
        """
        self.__ID = ID

    def setNumeStudent(self, nume):
        """
            setter pentru nume student
        """
        self.__nume_student = nume

    def setRezolvare(self, rezolvare):
        """
             setter pentru Rezolvare
        """
        self.__rezolvare = rezolvare

    def __str__(self):
        """
            override functie de str
        """
        return str(self.__ID) + "," + self.__nume_student + "," + self.__rezolvare

    def __eq__(self, other):
        """
            override functie de =
        """
        return self.getID == other.getID