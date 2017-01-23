"""
    Repository MODULE
"""

from Domain.Jucator import Jucator

class Repo:
    """
        Repo Class
    """
    def __init__(self, filename):
        """
        Constructor Repository ... initializeaza cu numele fisierului si incarca datele din fisier
        :param filename: numele fisierului
        """
        self.__filename = filename
        self.__players = []
        self.__load()

    def __load(self):
        """
        Incarca din fiser jucatorii care au atributele despartite de ~
        :return: None
        """
        try:
            file = open(self.__filename, "r")
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                args = line.split('~')
                if line != "" and len(args) == 4:
                    player = Jucator(args[0], args[1], int(args[2]), args[3])
                    self.__addPlayer(player)
            file.close()
        except IOError:
            raise ValueError("Eroare Fisier")

    def __save(self):
        """
        Salveaza in fisier jucatorii prin suprascriere
        :return: None
        """
        try:
            file = open(self.__filename, "w")
            for player in self.__players:
                file.write(str(player))
            file.close()
        except IOError:
            raise ValueError("Eroare Fisier")

    def __addPlayer(self, player):
        """
        Adauga un player in lista de jucatori doar daca nu mai exista deja
        :param player: jucatorul care trebuie sa fie adaugat
        :return: True daca nu mai exista si False, altfel
        """
        if player not in self.__players:
            self.__players.append(player)
            return True
        return False

    def storePlayer(self, player):
        """
        Salveaza un player in fisier si in lista de jucatori
        :param player: Playerul sa fie adaugat
        :return: None
        """
        if self.__addPlayer(player):
            file = open(self.__filename, "a")
            file.write(str(player))
            file.close()

    def getAll(self):
        """
        Getter pentru lista de jucatori
        :return: Lista de jucatori
        """
        return self.__players

    def updateInaltime(self, player, inaltimeNoua):
        """
        Face update la inaltime la un jucator dat in lista de jucatori si in fisier
        :param player: Jucatorul care trebuie modificat
        :param inaltimeNoua: inaltimea noua a jucatorului
        :return: None
        """
        i = 0
        while i < len(self.__players):
            if player == self.__players[i]:
                self.__players[i].setInaltime(inaltimeNoua)
                break
            i += 1
        self.__save()

    def getFromFile(self, filename):
        """
        Citeste din nume, prenume si retuneaza o lista jucatori cu numele, prenumele, 199, "" (ulterior
        vor fi modificate postul si inaltimea)
        Arunca exceptie daca da eroare la fisier
        :param filename: Numele fisierului
        :return: Lista de jucatori
        """
        players = []
        try:
            file = open(filename, "r")
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                args = line.split(' ')
                if line != "" and len(args) == 2:
                    player = Jucator(args[0], args[1], 199, "")
                    players.append(player)
            file.close()
        except IOError:
            raise ValueError("Eroare Fisier")
        return players