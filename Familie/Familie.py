"""
Modul care contine toate funtiile necesare comenzilor :
    - adauga_cheltuiala
    - creeaza
si functii auxiliare :
    - get_index
"""

from copy import deepcopy
from Domain import *


def get_index(zi, tip, cheltuieli):
    """
    Funtia primeste ziua si tipul unei cheltuili si returneza pozitia unde se gaseste chetuiala in lista de cheltuieli
    Daca nu exita, functia va returna -1
    """
    if zi > 31 or zi < 1: raise ValueError("Zi Invalida")
    if tip not in ["mancare", "intretinere", "inbracaminte", "telefon", "altele"]: raise ValueError("Tip Invalid")
    found_index = -1
    for index in range(0, len(get_cheltuieli(cheltuieli))):
        cheltuiala = get_cheltuieli(cheltuieli)[index]
        if get_zi(cheltuiala) == zi and get_tip(cheltuiala) == tip:
            found_index = index
            break
    return found_index


def adauga_cheltuiala(zi, suma, tip, cheltuieli):
    """
    Funtia primeste ca parametri ziua, suma si tipul unei cheltuieli, precum si lista de cheltuieli
    Daca exista deja aceasta cheltuiala(aceeiasi zi si acelasi tip), suma va fi adaugata la cea existenta
    In caz contrar, se va adauga cheltuiala in lista
    Daca ziua nu e in intervalul [1, 31] se va arunca o eroare
    Daca suma nu este pozitiva, se va arunca o eroare
    Daca tip nu este unul dintre : ["mancare", "intretinere", "inbracaminte", "telefon", "altele"], se va arunca o eroare
    """
    try :
        zi = int(zi)
    except: raise ValueError("Zi Invalida")
    if zi > 31 or zi < 1: raise ValueError("Zi Invalida")
    try :
        suma = int(suma)
    except: raise ValueError("Suma Invalida")
    if suma <= 0 : raise ValueError("Suma Invalida")
    if tip not in ["mancare", "intretinere", "inbracaminte", "telefon", "altele"]: raise ValueError("Tip Invalid")
    get_undolist(cheltuieli).append(deepcopy(get_cheltuieli(cheltuieli)))
    found_index = get_index(zi, tip, cheltuieli)
    if found_index == -1:
        get_cheltuieli(cheltuieli).append(creeaza_cheltuiala(zi, suma, tip))
    else:
        get_cheltuieli(cheltuieli)[found_index][1] += suma


def sterge(tipOrStart, end, action, cheltuieli):
    """
    Funtia sterge cheltuieli din lista de cheltuieli
    Exista 3 tipuri de stergeri :
        - stergere pe o zi :
            Se sterg toate cheltuielile din ziua tipOrStart
            Daca tipOrStart nu e in intervalul [1, 31], se va arunca o eroare
            action = "Single"
            end = orice
        - stergere pe o perioada :
            Se sterg toate cheltuielile din perioada [tipOrStart, end]
            Daca tipOrStart nu e in intervalul [1, 31], se va arunca o eroare
            Daca end nu e in intervalul [1, 31], se va arunca o eroare
            action = "Interval"
        - stergere dupa tip :
            Se sterg toate cheltuielile care au tipul : tipOrStart
            Daca tipOrStart nu este unul dintre : ["mancare", "intretinere", "inbracaminte", "telefon", "altele"], se va arunca o eroare
            action = "Tip"
            end = orice
    """
    get_undolist(cheltuieli).append(deepcopy(get_cheltuieli(cheltuieli)))
    length = len(get_cheltuieli(cheltuieli))
    index = 0
    if action == "Single":
        tipOrStart = int(tipOrStart)
        if tipOrStart <= 0: raise ValueError("Suma Invalida")
        while index < length:
            cheltuiala = get_cheltuieli(cheltuieli)[index]
            if get_suma(cheltuiala) == tipOrStart:
                del get_cheltuieli(cheltuieli)[index]
                index -= 1
                length -= 1
            index += 1
    elif action == "Interval":
        tipOrStart = int(tipOrStart)
        end = int(end)
        if tipOrStart > 31 or tipOrStart < 1: raise ValueError("Zi Invalida")
        if end > 31 or end < 1: raise ValueError("Zi Invalida")
        if tipOrStart > end: raise ValueError("Zi final trebuie sa fie mai mare ca zi start")
        while index < length:
            cheltuiala = get_cheltuieli(cheltuieli)[index]
            if tipOrStart <= get_suma(cheltuiala) <= end:
                del get_cheltuieli(cheltuieli)[index]
                index -= 1
                length -= 1
            index += 1
    elif action == "Tip":
        if tipOrStart not in ["mancare", "intretinere", "inbracaminte", "telefon", "altele"]: raise ValueError("Tip Invalid")
        while index < length:
            cheltuiala = get_cheltuieli(cheltuieli)[index]
            if get_tip(cheltuiala) == tipOrStart:
                del get_cheltuieli(cheltuieli)[index]
                index -= 1
                length -= 1
            index += 1


def cautare(sumOrTip, zi, action, cheltuieli):
    """
    Funtia cauta in lista de cheltuieli
    Exista 3 tipuri de cautari :
        - cautare cu suma mai mare:
            Se returneaza toate cheltuielile cu suma mai mare ca sumOrTip
            Daca sumOrTip nu este pozitiva, se va arunca o eroare
            action = "Single"
            zi = orice
        - cautare cu suma mai mica si zi mai mica :
            Se returneaza toate cheltuielile cu suma mai mica ca sumOrTip si cu ziua mai mica ca zi
            Daca sumOrTip nu este pozitiva, se va arunca o eroare
            Daca zi nu este in intervalul [1, 31], se va arunca o eroare
            action = "Multiple"
        - cautare dupa tip :
            Se returneaza toate cheltuielile care au tipul : tipOrStart
            Daca sumOrTip nu este unul dintre : ["mancare", "intretinere", "inbracaminte", "telefon", "altele"], se va arunca o eroare
            action = "Tip"
            zi = orice
    """
    lista = []
    if action == "Single":
        sumOrTip = int(sumOrTip)
        if sumOrTip <= 0: raise ValueError("Suma Invalida")
        for cheltuiala in get_cheltuieli(cheltuieli):
            if get_suma(cheltuiala) > sumOrTip:
                lista.append(cheltuiala)
    elif action == "Multiple":
        sumOrTip = int(sumOrTip)
        zi = int(zi)
        if zi > 31 or zi < 1: raise ValueError("Zi Invalida")
        if sumOrTip <= 0: raise ValueError("Suma Invalida")
        for cheltuiala in get_cheltuieli(cheltuieli):
            if get_suma(cheltuiala) < sumOrTip and get_zi(cheltuiala) < zi:
                lista.append(cheltuiala)
    elif action == "Tip":
        if sumOrTip not in ["mancare", "intretinere", "inbracaminte", "telefon", "altele"]: raise ValueError("Tip Invalid")
        for cheltuiala in get_cheltuieli(cheltuieli):
            if get_tip(cheltuiala) == sumOrTip:
                lista.append(cheltuiala)
    return lista


def rapoarte(sumOrTip, action, cheltuieli):
    """
        Funtia ofera rapoarte despre lista de cheltuieli
        Exista 4 tipuri de rapoarte :
            - Suma totala pentru un anumit tip:
                Se returneaza suma totala a cheltuielilor cu tipul sumOrTip
                Daca sumOrTip nu este unul dintre : ["mancare", "intretinere", "inbracaminte", "telefon", "altele"], se va arunca o eroare
                action = "SumByTip"
            - Ziua cu cheltuiala maxima :
                Se returneaza prima zi cu cheltuiala maxima
                action = "Maxim"
                sumOrTip = orice
            - Toate cheltuielile cu o anumita suma :
                Se returneaza toate cheltuielile care au suma sumOrTip
                Daca sumOrTip nu e o valoare pozitiva, se va arunca o eroare
                action = "Sum"
            - Cheltuilile sortate dupa tip:
                Se returneaza o lista de cheltuieli grupate dupa sumOrTip
                Daca sumOrTip nu este unul dintre : ["mancare", "intretinere", "inbracaminte", "telefon", "altele"], se va arunca o eroare
                action = "Sort"
    """
    if action == "SumByTip":
        if sumOrTip not in ["mancare", "intretinere", "inbracaminte", "telefon", "altele"]: raise ValueError("Tip Invalid")
        sum = 0
        for cheltuiala in get_cheltuieli(cheltuieli):
            if get_tip(cheltuiala) == sumOrTip:
                sum += get_suma(cheltuiala)
        return sum
    elif action == "Maxim":
        zile = {}
        maxim = -1
        zi_maxima = -1
        for cheltuiala in get_cheltuieli(cheltuieli):
            if zile.__contains__(get_zi(cheltuiala)):
                zile[get_zi(cheltuiala)] += get_suma(cheltuiala)
            else:
                zile[get_zi(cheltuiala)] = get_suma(cheltuiala)
            if zile[get_zi(cheltuiala)] > maxim:
                maxim = zile[get_zi(cheltuiala)]
                zi_maxima = get_zi(cheltuiala)
        return zi_maxima
    elif action == "Sum":
        sumOrTip = int(sumOrTip)
        if sumOrTip <= 0: raise ValueError("Suma Invalida")
        lista = []
        for cheltuiala in get_cheltuieli(cheltuieli):
            if get_suma(cheltuiala) == sumOrTip:
                lista.append(cheltuiala)
        return lista
    elif action == "Sort":
        lista = {}
        for cheltuiala in get_cheltuieli(cheltuieli):
            if lista.__contains__(get_tip(cheltuiala)):
                lista[get_tip(cheltuiala)].append(cheltuiala)
            else:
                lista[get_tip(cheltuiala)] = [cheltuiala]
        return lista


def filtrare(sumOrTip, action, cheltuieli):
    """
        Funtia filtreaza(sterge) unele cheluieli din lista de cheltuieli
        Exista 2 tipuri de filtrari :
            - filtrare dupa tip:
                Se sterg toate cheltuielile cu tipul sumOrTip
                Daca sumOrTip nu este unul dintre : ["mancare", "intretinere", "inbracaminte", "telefon", "altele"], se va arunca o eroare
                action = "Tip"
           - filtrare dupa suma mai mica:
                Se sterg toate cheltuielile cu suma mai mica decat sumOrTip
                Daca sumOrTip nu e o valoare pozitiva, se va arunca o eroare
                action = "Sum"
    """
    get_undolist(cheltuieli).append(deepcopy(get_cheltuieli(cheltuieli)))
    index = 0
    length = len(get_cheltuieli(cheltuieli))
    if action == "Tip":
        if sumOrTip not in ["mancare", "intretinere", "inbracaminte", "telefon", "altele"]: raise ValueError("Tip Invalid")
        while index < length:
            cheltuiala = get_cheltuieli(cheltuieli)[index]
            if get_tip(cheltuiala) == sumOrTip:
                del get_cheltuieli(cheltuieli)[index]
                index -= 1
                length -= 1
            index += 1
    elif action == "Sum":
        sumOrTip = int(sumOrTip)
        if sumOrTip <= 0: raise ValueError("Suma Invalida")
        while index < length:
            cheltuiala = get_cheltuieli(cheltuieli)[index]
            if get_suma(cheltuiala) < sumOrTip:
                del get_cheltuieli(cheltuieli)[index]
                index -= 1
                length -= 1
            index += 1
    return get_cheltuieli(cheltuieli)


def undo(cheltuieli):
    """
    Revine la ultima lista de cheltuili avuta
    """
    if len(get_undolist(cheltuieli)) > 0:
        set_cheltuieli(cheltuieli, get_undolist(cheltuieli).pop())
    return get_cheltuieli(cheltuieli)
