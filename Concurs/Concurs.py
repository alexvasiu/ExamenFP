from copy import deepcopy

def creeaza():
    """
       functia creeaza o noua lista de participanti si scoruri asociate
    """
    return [[],[],[]]


def findList(lista, value):
    """
    Functia ia ca parametru o lista si un numar si returneza pe ce pozitie se afla acel numar in lista
    Daca lista nu contine acel numar, functia va returna -1.
    """
    for i in range(0, len(lista)):
        if lista[i] == value:
            return i
    return -1


def test_findList():
    """
       Functia testeaza functionalitatea functiei findList
       """
    assert findList([10, 20], 10) == 0
    assert findList([], 1) == -1
    assert findList([10, 1990, 14], 14) == 2
    assert findList([20, 0, -10, 32], -10) == 2

def adauga_scor_persoana(numar_partipant, scoruri, participanti):
    """
       Functia ia ca parametri : numarul de participantului scorurile acestuia si lista de participanti existenta
       Aceata insereaza un utilizator nou, daca nu exista sau actualizeaza scorurile daca exista
    """
    if len(participanti[1]):
        participanti[2].append(deepcopy(participanti[1]))
    index = findList(participanti[0], numar_partipant)
    if index == -1:
        participanti[0].append(numar_partipant)
        participanti[1].append(scoruri)
    else:
        participanti[1][index] = scoruri

def test_adauga_scor_porsoana():
    """
          Functia testeaza functionalitatea functiei adauga_scor_persoana
    """
    participanti = creeaza()
    adauga_scor_persoana(10, [10, 20], participanti)
    assert findList(participanti[0], 10) == 0
    assert participanti[1][0] == [10, 20]
    adauga_scor_persoana(10, [10], participanti)
    assert participanti[1][0] == [10]
    adauga_scor_persoana(1200, [30, 10, 20, 100], participanti)
    assert findList(participanti[0], 1200) == 1
    assert participanti[1][1] == [30, 10, 20, 100]

def undo(participanti):
    if len(participanti[2]):
        participanti[1] = participanti[2].pop()

test_findList()
test_adauga_scor_porsoana()