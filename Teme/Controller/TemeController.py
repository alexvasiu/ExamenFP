"""
    Controller Layer
"""
from Domain.Tema import Tema


class TemeController:
    """
        Clasa teme controller
    """
    def __init__(self, repo, validator):
        """
             initializare cu repository si validator
        """
        self.__repo = repo
        self.__validator = validator

    def createTema(self, ID, Nume_Student, Rezolvare):
        """
            creeare si stoare tema in repository
            aruncare de exceptie in caz ca id-ul nu e unic
            sau id nu numar pozitiv sau numele nu contine minim 3 litere sau rezolvarea nu contine minim 5 cuvinte
        """
        tema = Tema(int(ID), Nume_Student, Rezolvare)
        if tema in self.__repo.getAll: raise ValueError("Person already exists")
        try:
            self.__validator.validateTema(tema)
            self.__repo.store(tema)
        except ValueError as e:
            raise e

    def temeOrdDesc(self):
        """
            returneaza temele in sortate descrescator dupa numarul de cuvinte din rezolvare
        """
        return list(map(str,reversed(sorted(self.__repo.getAll, key = lambda tema: len(tema.getRezolvare.split(' '))))))

    def plagiat(self):
        """
            returneaza perechi de teme care se considera a fi palgiat (15% din nr total de cuv sunt comune) si procentajul copierii
        """
        plagiate = []
        numar_teme = len(self.__repo.getAll)
        for i in range(0, numar_teme):
            for j in range(i + 1, numar_teme):
                numar_comune = 0
                tema1 = self.__repo.getAll[i]
                tema2 = self.__repo.getAll[j]
                cuvinte_rez1 = tema1.getRezolvare.split(' ')
                cuvinte_rez2 = tema2.getRezolvare.split(' ')
                numar_total_cuvinte = len(cuvinte_rez1) + len(cuvinte_rez2)
                for cuvant in cuvinte_rez1:
                    if cuvant in cuvinte_rez2:
                        numar_comune += 1
                procentaj = 100 * numar_comune / numar_total_cuvinte
                if procentaj > 15.00:
                    plagiate.append((str(tema1), str(tema2), "%.2f " % procentaj + "%"))
        return plagiate