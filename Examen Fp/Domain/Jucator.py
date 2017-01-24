"""
    Domain Moudule - Jucator Class
"""


class Jucator:
    """
        Clasa Jucator
    """
    def __init__(self, nume, prenume, inaltime, post):
        """
        Constructor Jucator
        :param nume: Nume Jucator
        :param prenume: Prenume Jucator
        :param inaltime: Inaltime Jucator
        :param post: Post Jucator
        """
        self.__nume = nume
        self.__prenume = prenume
        self.__inaltime = inaltime
        self.__post = post

    def getNume(self):
        """
        Getter pentru Nume
        :return: Numele Jucatorului
        """
        return self.__nume

    def getPrenume(self):
        """
        Getter pentru Prenume
        :return: Prenumele Jucatorului
        """
        return self.__prenume

    def getInaltime(self):
        """
        Getter pentru Inaltime
        :return: Inaltimea Jucatorului
        """
        return self.__inaltime

    def getPost(self):
        """
        Getter pentru Post
        :return: Postul Jucatorului
        """
        return self.__post

    def setInaltime(self, inaltime):
        """
        Setter pentru inaltime
        :param inaltime: Postul Jucatorului
        :return: None
        """
        self.__inaltime = inaltime

    def setPost(self, post):
        """
            Setter pentru post
            :param post: Postul Jucatorului
            :return: None
        """
        self.__post = post

    def __eq__(self, other):
        """
        Testeaza 2 jucatori daca au acelasi nume si prenume
        :param other: Alt Jucator
        :return: True, daca e aceeasi persoana, False altfel
        """
        return self.__nume == other.__nume and self.__prenume == other.__prenume

    def __str__(self):
        """
        :return: Returneaza un string atributele jucatorui concatenate cu ~ si cu un endline
        """
        return self.__nume + "~" + self.__prenume + "~" + str(self.__inaltime) + "~" + self.__post + "\n"

    def getFullPlayer(self):
        """
        :return: Returneaza un string atributele jucatorui concatenate cu space
        """
        return self.__prenume + " " + self.__nume + " " + self.__post + " " + str(self.__inaltime)
