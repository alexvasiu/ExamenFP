"""
    Controller MODULE - Controller Jucatori
"""

from Domain.Jucator import Jucator
import random


class ControllerJucator:
    """
        Controller Class
    """
    def __init__(self, validator, repo):
        """
        Contructor controller
        :param validator: Validatorul pentru jucatori
        :param repo: Repository-ul pentru salvarea datelor
        """
        self.__validator = validator
        self.__repo = repo

    def AdaugaJucator(self, nume, prenume, inaltime, post):
        """
        Adauga un jucator
        Daca nu este valid, atunci va arunca exceptiile venite de la validator
        :param nume: Nume Jucator
        :param prenume: Prenume Jucator
        :param inaltime: Inaltime Jucator
        :param post: Post Jucator
        :return: None
        """
        player = Jucator(nume, prenume, inaltime, post)
        self.__validator.validateJucator(player)
        self.__repo.storePlayer(player)

    def updateInaltime(self, nume, prenume, inaltime):
        """
        Face update la inaltime unui jucator
        Daca jucatorul la care se doreste update nu exista, se va arunca exceptie
        :param nume: Nume Jucator
        :param prenume: Prenume Jucator
        :param inaltime: Inaltime Noua Jucator
        :return: None
        """
        player = None
        jucatorNou = Jucator(nume, prenume, inaltime, "")
        self.__validator.validateJucator(Jucator("Alex", "Alex", inaltime, "Fundas"))
        for jucator in self.__repo.getAll():
            if jucatorNou == jucator:
                player = jucator
                break
        if not player: raise ValueError("Nu exsita jucatorul introdus")
        self.__repo.updateInaltime(player, inaltime)

    def getTeam(self):
        """
        Compune o echipa de baschet formata din 2 fundasi, 1 pivot si 2 extreme,
        echipa cu media de inaltime cea mai mare. Daca nu se poate forma o echipa
        se va arunca o exceptie.
        :return: Lista cu membrii echipei
        """
        fundasi = [x for x in self.__repo.getAll() if x.getPost() == "Fundas"]
        pivoti = [x for x in self.__repo.getAll() if x.getPost() == "Pivot" ]
        extrema = [x for x in self.__repo.getAll() if x.getPost() == "Extrema"]
        echipa = []
        if len(fundasi) < 2 or len(pivoti) < 1 or len(extrema) < 2:
            raise ValueError("Nu sunt destui jucatori pentru a forma o echipa")
        fundasi = sorted(fundasi, key=lambda x:int(x.getInaltime()))
        pivoti = sorted(pivoti, key=lambda x:int(x.getInaltime()))
        extrema = sorted(extrema, key=lambda x:int(x.getInaltime()))
        echipa.append(fundasi[-2].getFullPlayer())
        echipa.append(fundasi[-1].getFullPlayer())
        echipa.append(pivoti[-1].getFullPlayer())
        echipa.append(extrema[-2].getFullPlayer())
        echipa.append(extrema[-1].getFullPlayer())
        return echipa

    def importFromFile(self, filename):
        """
        Face import de nume, prenume dintr-un fisier si asigneaza inaltimea si postul random
        In caz ca fiserul nu exista se va arunca exceptia venit din Repo
        :param filename: numele fisierului
        :return: numarul de playeri importati
        """
        nr = 0
        posturi = ["Fundas", "Pivot", "Extrema"]
        players = self.__repo.getFromFile(filename)
        for player in players:
            player.setInaltime(random.randint(160, 225))
            player.setPost(posturi[random.randint(0, 2)])
            if player not in self.__repo.getAll():
                nr += 1
                self.__repo.storePlayer(player)
        return nr