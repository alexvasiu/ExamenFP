"""
    UI Layer
"""
class UI:
    """
        clasa de UI
    """
    def __init__(self, controller):
        """
            initializare cu controller
        """
        self.__controller = controller

    def showMenu(self):
        """
            afisare meniu, citire date, afirare rapoarte
        """
        while True:
            self.__Menu()
            cmd = input("Optiune = ")
            if cmd == '0': break
            elif cmd == '1':
                id = input("ID Tema : ")
                nume_student = input("Nume Student : ")
                rezolvare = input("Rezolvare Tema : ")
                try:
                    self.__controller.createTema(id, nume_student, rezolvare)
                    print("Tema a fost adaugata cu succes")
                except ValueError as e:
                    print(e)
            elif cmd == '2':
                raport = self.__controller.temeOrdDesc()
                for tema in raport:
                    print(tema)
            elif cmd == '3':
                plagiate = self.__controller.plagiat()
                if len(plagiate) == 0: print("Nu exista plagiat")
                else:
                    for plagiat in plagiate:
                        print(plagiat)
            else:
                print("Comanda Invalida")


    def __Menu(self):
        """
            afisare optiuni
        """
        print("1 - Adaugare tema")
        print("2 - Vizualizare tema")
        print("3 - Determinare plagiat")
        print("0 - Exit")