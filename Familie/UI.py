"""
Modul pentru UI:
    - afisare meniu
    - procesare comenzi
"""

from Familie import adauga_cheltuiala, creeaza, sterge, cautare, rapoarte, filtrare, undo


def read_int(inputTxt, error):
    """
    :param inputTxt: Textul afisat pe ecran la citire
    :param error: Mesajul afisat in caz de eroare
    Functia citeste si returneza o valoare de tip integer
    """
    while True:
        try:
            var = int(input(inputTxt))
            break
        except ValueError:
            print(error)
    return var


def read_tip():
    """
    Functia citeste si returneza un string (tipul cheltuielii) care trebuie sa fie unul dintre :
        - mancare
        - intretinere
        - inbracaminte
        - telefon
        - altele
    In caz ca utilizatorul introduce un tip invalid se va afisa pe ecran "Tip Invalid"
    """
    while True:
        tip = (input("Tip (mancare/intretinere/inbracaminte/telefon/altele) : "))
        if tip in ["mancare", "intretinere", "inbracaminte", "telefon", "altele"]:
            break
        else:
            print("Tip Invalid")
    return tip


def print_menu():
    """
    Afiseaza meniul pe ecran
    """
    print("1 - Adauga Cheltuiala")
    print("2 - Sterge")
    print("3 - Cauta")
    print("4 - Rapoarte")
    print("5 - Filtrare")
    print("6 - Undo")
    print("0 - Exit")


def print_menu_stergere():
    """
    Afiseaza meniul pentru stergere
    """
    print("1 - Sterge cheltuieli pentru o zi data")
    print("2 - Sterge cheltuieli pentru o perioada de mai multe zile")
    print("3 - Sterge cheltuielile de un anumit tip")
    print("0 - Cancel")


def print_menu_cautare():
    """
    Afiseaza meniul pentru cautare
    """
    print("1 - Cheltuieli mai mari decat o suma")
    print("2 - Cheltuieli efectuate inainte de o zi data și mai mici decat o suma data")
    print("3 - Cheltuielile de un anumit tip")
    print("0 - Cancel")


def print_meniu_rapoarte():
    """
    Afiseaza meniul pentru rapoarte
    """
    print("1 - Suma totala pentru un anumit tip")
    print("2 - Ziua cu suma maxima")
    print("3 - Toate cheltuielile cu o anumita suma")
    print("4 - Cheltuielile sortate dupa tip")
    print("0 - Cancel")


def print_menu_filtrare():
    """
        Afiseaza meniul pentru filtrare
    """
    print("1 - Elimina cheltuielile cu un anumit tip")
    print("2 - Elimina cheltuielile mai mici decat o suma data")
    print("0 - Cancel")


def action_adaugare(cheltuieli):
    """
    Se executa pentru comada de adaugare
    Citeste datele si le trimite la procesat
    """
    ziua = read_int("Zi : ", "Zi Invalida")
    suma = read_int("Suma : ", "Suma Invalida")
    tip = read_tip()
    adauga_cheltuiala(ziua, suma, tip, cheltuieli)


def action_stergere(cheltuieli):
    """
    Se executa pentru comanda de stergere
    Citeste datele si le trimite la procesat
    """
    print_menu_stergere()
    try:
        delete_commad = int(input("Algeti comanda : "))
        if delete_commad == 0:
            pass
        elif delete_commad == 1:
            zi = read_int("Zi : ", "Zi Invalida")
            sterge(zi, -1, "Single", cheltuieli)
        elif delete_commad == 2:
            zi1 = read_int("Ziua 1 : ", "Zi Invalida")
            zi2 = read_int("Ziua 2 : ", "Zi Invalida")
            sterge(zi1, zi2, "Interval", cheltuieli)
        elif delete_commad == 3:
            tip = read_tip()
            sterge(tip, -1, "Tip", cheltuieli)
        else:
            print("Comanda Invalida")
    except:
        print("Comanda Invalida")


def action_cautare(cheltuieli):
    """
    Se executa pentru comanda de cautare
    Citeste datele si le trimite la procesat
    """
    print_menu_cautare()
    try:
        comanda_cautare = int(input("Alegeti comanda : "))
        if comanda_cautare == 0:
            pass
        elif comanda_cautare == 1:
            suma = read_int("Suma : ", "Suma Invalida")
            print(cautare(suma, -1, "Single", cheltuieli))
        elif comanda_cautare == 2:
            suma = read_int("Suma : ", "Suma Invalida")
            zi = read_int("Zi : ", "Zi Invalida")
            print(cautare(suma, zi, "Multiple", cheltuieli))
        elif comanda_cautare == 3:
            tip = read_tip()
            print(cautare(tip, -1, "Tip", cheltuieli))
    except:
        print("Comanda Invalida")


def action_rapoarte(cheltuieli):
    """
        Se executa pentru comanda de rapoarte
        Citeste datele si le trimite la procesat
    """
    print_meniu_rapoarte()
    try:
        comanda_rapoarte = int(input("Alegeti comanda : "))
        if comanda_rapoarte == 0:
            pass
        elif comanda_rapoarte == 1:
            tip = read_tip()
            print(rapoarte(tip, "SumByTip", cheltuieli))
        elif comanda_rapoarte == 2:
            print(rapoarte(-1, "Maxim", cheltuieli))
        elif comanda_rapoarte == 3:
            sum = read_int("Suma : ", "Suma Invalida")
            print(rapoarte(sum, "Sum", cheltuieli))
        elif comanda_rapoarte == 4:
            print(rapoarte(-1, "Sort", cheltuieli))
        else:
            print("Comanda Invalida")
    except:
        print("Comanda Invalida")


def action_filtrare(cheltuieli):
    """
    Se executa pentru comanda de filtrare
    Citeste datele si le trimite la procesat
    """
    print_menu_filtrare()
    try:
        comanda_filtrare = int(input("Alegeti comanda : "))
        if comanda_filtrare == 0:
            pass
        elif comanda_filtrare == 1:
            tip = read_tip()
            filtrare(tip, "Tip", cheltuieli)
        elif comanda_filtrare == 2:
            sum = read_int("Suma : ", "Suma Invalida")
            filtrare(sum, "Sum", cheltuieli)
        else:
            print("Comanda invalida")
    except:
        print("Comanda Invalida")


def UI():
    """
    Citeste si proceseaza comenzile primite de la utilizator
    """
    cheltuieli = creeaza()
    while True:
        print_menu()
        #comanda = read_int("Alegeti comanda : ", "Comanda Invalida")
        comanda = input("Dati Comanda : ")
        if comanda == '0':
            break
        elif comanda == '1':
            try:
                action_adaugare(cheltuieli)
            except ValueError as e:
                print(e)
        elif comanda == '2':
            try:
                action_stergere(cheltuieli)
            except ValueError as e:
                print(e)
        elif comanda == '3':
            try:
                action_cautare(cheltuieli)
            except ValueError as e:
                print(e)
        elif comanda == '4':
            try:
                action_rapoarte(cheltuieli)
            except ValueError as e:
                print(e)
        elif comanda == '5':
            try:
                action_filtrare(cheltuieli)
            except ValueError as e:
                print(e)
        elif comanda == '6':
            undo(cheltuieli)
        else:
            args = comanda.split()
            if args[0] == 'add' and len(args) == 4: # adaugare cheltuiala
                try:
                    adauga_cheltuiala(args[1], args[2], args[3], cheltuieli)
                except ValueError as e: print(e)
            elif args[0] == 'remove' and len(args) == 3: # sterge cheltuieli dintre 2 zile date
                try:
                    sterge(args[1], args[2], "Interval", cheltuieli)
                except ValueError as e: print(e)
            elif args[0] == 'undo' and len(args) == 1:  # undo
                try:
                   undo(cheltuieli)
                except ValueError as e: print(e)
            elif args[0] == 'filter' and args[1] == 'all' and len(args) == 2:  # afisare cheltuieli sortate dupa tip
                try:
                   print(rapoarte(-1, "Sort", cheltuieli))
                except ValueError as e: print(e)
            elif args[0] == 'search' and len(args) == 2: # afisare cheltuieli mai mari ca o suma data
                try:
                   print(cautare(args[1], -1, "Single", cheltuieli))
                except ValueError as e: print(e)
            else:
                print("Comanda Invalida")