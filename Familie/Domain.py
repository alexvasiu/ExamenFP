"""
Domanin Module :
 - creare cheltuieli
 - get chetuieli
 - set cheltuieli
"""
def creeaza():
    """
    Functia creeaza o lista ce contine 2 liste principale :
        - cea de cheltuieli
        - cea necesare pentru UNDO (cheltuielile trecute)
    """
    return [[],[]]

def creeaza_cheltuiala(zi, suma, tip):
    """
    Creeaza o cheltuiala
    """
    return [zi, suma, tip]

def get_zi(cheltuiala):
    return cheltuiala[0]

def get_suma(cheltuiala):
    return cheltuiala[1]

def get_tip(cheltuiala):
    return cheltuiala[2]

def get_cheltuieli(cheltuieli):
    return cheltuieli[0]

def get_undolist(cheltuieli):
    return cheltuieli[1]

def set_cheltuieli(cheltuieli, value):
    cheltuieli[0] = value
    return cheltuieli

