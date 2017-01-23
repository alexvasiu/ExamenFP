"""
    Domain Moudule - Validator
"""

class Validator:
    """
        Validator Class
    """
    def validateJucator(self, player):
        """
        Valideaza un jucator astfel :
            - numele si prenumele sa nu fie vide
            - inaltimea sa fie un numar pozitiv
            - postul sa fie unul din urmatoarele : Fundas, Pivot, Extrema
        Daca exista exceptii se vor arunca
        :param player:
        :return: None
        """
        errors = []
        if len(player.getNume()) == 0: errors.append("Numele nu poate fi vid")
        if len(player.getPrenume()) == 0: errors.append("Prenumele nu poate fi vid")
        if self.__isInt(player.getInaltime()):
            if int(player.getInaltime()) <= 0:
                errors.append("Inaltimea trebuie sa fie un numar pozitiv")
        else:
            errors.append("Inaltimea trebuie sa fie un numar pozitiv")
        if player.getPost() not in ["Fundas", "Pivot", "Extrema"]:
            errors.append("Postul jucatorului poate fi Fundas, Pivot sau Extrema")
        if len(errors):
            raise ValueError(errors)

    def __isInt(self, nr):
        """
        Testeaza un string daca e int
        :param nr: stringul de testat
        :return: True daca e numar si False, atfel
        """
        try:
            t = int(nr)
            return True
        except:
            return False