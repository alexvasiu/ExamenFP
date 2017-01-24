from Concurs import adauga_scor_persoana
from Concurs import creeaza
from Concurs import undo

def print_menu():
    print("1 - Adauga Scor La Participant")
    print("6 - Undo")
    print("0 - Exit")

def UI():
    participanti = creeaza()
    while True:
        print_menu()
        print(participanti)
        comanda = input("Algeti o comanda : ")
        if comanda == '0': break
        elif comanda == '1':
            while True:
                try:
                    id = int(input("Id Concurent = "))
                    break
                except:
                    print("Numar Invalid")
            scoruri = []
            for i in range(1, 11):
                while True:
                    try:
                        scor = int(input("Scor proba {0} = ".format(i)))
                        scoruri.append(scor)
                        break
                    except:
                        print("Numar Invalid")
            adauga_scor_persoana(id,scoruri, participanti)
            print("Concurent adaugat cu succes\n")
        elif comanda == '6':
            undo(participanti)
        else: print("Comanda Invalida")
# tema 3 - Cheltuieli de familie