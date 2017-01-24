"""
    Repository Layer
"""

from Domain.Tema import Tema


class Repo:
    """
        Repo Class
    """
    def __init__(self, filename):
        """
            initializare cu numle fisierului,
            initializare lista teme
            incarcare teme
        """
        self.__filename = filename
        self.__teme = []
        self.__load()

    def __load(self):
        """
            incarcare teme din fisier
        """
        try:
            with open(self.__filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    args = line.split(',')
                    if len(args) == 3:
                        tema = Tema(int(args[0]), args[1], args[2].split('\n')[0])
                        self.__teme.append(tema)
        except:
            raise ValueError("File error")


    def store(self, Tema):
        """
            salvare tema in lista si fisier
        """
        self.__teme.append(Tema)
        try:
            with open(self.__filename, 'a') as file:
                file.write(str(Tema) + "\n")
        except:
            raise ValueError("File error")

    @property
    def getAll(self):
        """
            getter pentru teme
        """
        return self.__teme