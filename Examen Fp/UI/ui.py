"""
    UI MODULE - ui class
"""

class UI:
    """
        UI Class
    """
    def __init__(self, controller):
        self.__controller = controller

    def showUI(self):
        """
        Afiseaza meniul si citeste optiunea utilizatorului
        in functie de optiune printeaza ceea ce i s-a cerut
        Prinde toate exceptiile
        :return: None
        """
        while True:
            self.__printMenu()
            commad = input('Optiune = ')
            if commad == '1':
                nume = input("Nume = ")
                prenume = input("Prenume = ")
                inaltime = input("Inaltime = ")
                post = input("Post = ")
                try:
                    self.__controller.AdaugaJucator(nume, prenume, inaltime, post)
                    print("Jucator adaugat cu succes")
                except ValueError as e:
                    print(e)
            elif commad == '2':
                nume = input("Nume = ")
                prenume = input("Prenume = ")
                inaltime = input("Inaltime = ")
                try:
                    self.__controller.updateInaltime(nume, prenume, inaltime)
                    print("Inaltimea a fost modificata cu succes")
                except ValueError as e:
                    print(e)
            elif commad == '3':
                try:
                    team = self.__controller.getTeam()
                    for player in team:
                        print(player)
                except ValueError as e:
                    print(e)
            elif commad == '4':
                try:
                    filename = input("Nume Fisier = ")
                    nr = self.__controller.importFromFile(filename)
                    print("Au fost importati %d jucatori" % nr)
                except ValueError as e:
                    print(e)
            elif commad == '0':
                break
            else:
                print("Comanda Invalida")

    def __printMenu(self):
        """
        Afiseza mesajele pentru meniu
        :return: None
        """
        print("1 - Adauga Jucator")
        print("2 - Update Jucator")
        print("3 - Get Team")
        print("4 - Import")
        print("0 - Exit")