def citire(lista):
    """
    Citeste o lista si o returneaza prin parametrul lista
    """
    lista.clear()
    numar_elemente = int(input("Numar elemente lista = "))
    for i in range(1, numar_elemente + 1):
        nr = int(input("Numar {0} = ".format(i)))
        lista.append(nr)

def afisare_meniu():
    """
    Afisare comenzi meniu
    """
    print("Alege comanda :")
    print("1 - Citire Lista")
    print("2 - Subsecventa maxima cu suma elementelor 5")
    print("3 - Subsecventa maxima de tip munte")
    print("4 - Subsecventa maxima cu oricare doua elemente consecutive, relativ prime intre ele")
    print("5 - Subsecventa maxima cu oricare doua elemente consecutive, de semne contrare")
    print("0 - Exit")

#  13. suma elementelor este egal cu 5

def subsecventa_sumFive(lista):
    """
    Functia primeste prin parametru lista, o lista de numere intregi
    Functia returneaza subsecventa de lungime maxima unde suma elementelor este 5, sub forma unei liste
    Daca nu exita o astfel de subsecventa, functia va returna o lista vida
    Daca exista mai multe subsecvente de acest tip, functia o va returna pe prima gasita
    """
    length = len(lista)
    subMaxima = []
    for start in range(0,length):
        sfarsit = length - 1
        while sfarsit >= start:
            sum = 0
            index = start
            while index <= sfarsit:
                sum += lista[index]
                index += 1
            if sum == 5 and sfarsit - start + 1 > len(subMaxima):
                subMaxima = lista[start:sfarsit + 1]
            sfarsit -= 1
    return subMaxima

def test_subsecventa_sumFive():
    """
    Funtia testeza functionalitatea functiei subsecventa_sumFive
    """
    assert subsecventa_sumFive([1, 2, 3]) == [2, 3]
    assert subsecventa_sumFive([1, 1, 1, 0, 1, 1]) == [1, 1, 1, 0, 1, 1]
    assert subsecventa_sumFive([1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert subsecventa_sumFive([-1, 1, 5, -5, 5, 1, 2]) == [-1, 1, 5, -5, 5]
    assert subsecventa_sumFive([5, 0, 0, 0, 1, 0, 0, 1, -1]) == [5, 0, 0, 0]
    assert subsecventa_sumFive([1, 1, 1, 1]) == []
    assert subsecventa_sumFive([]) == []
    assert subsecventa_sumFive([5]) == [5]
    assert subsecventa_sumFive([5, -5]) == [5]
    assert subsecventa_sumFive([3, 2, 3]) == [3, 2]
    assert subsecventa_sumFive([100, -1000, 5, 6, 7, -6, 1000, -2, -5, 0, 5]) == [-1000, 5, 6, 7, -6, 1000, -2, -5, 0]

# end 13.

# 15. reprezinta o secventa sub forma de munte

def subsecventa_munte(lista):
    """
    Functia primeste prin parametru lista, o lista de numere intregi
    Functia returneaza subsecventa de lungime maxima unde subsecventa este de tip munte
    Daca nu exita o astfel de subsecventa, functia va returna o lista vida
    Daca exista mai multe subsecvente de acest tip, functia o va returna pe prima gasita
    """
    length = len(lista)
    subMaxima = []
    for start in range(0, length):
        sfarsit = length - 1
        while sfarsit > start:
            index = start
            goUp = False
            while index + 1 <= sfarsit and lista[index] < lista[index + 1]:
                index += 1
                goUp = True
            goDown = False
            while index + 1 <= sfarsit and lista[index] > lista[index + 1]:
                index += 1
                goDown = True
            if goDown and goUp and index == sfarsit and sfarsit - start + 1 > len(subMaxima):
                subMaxima = lista[start:sfarsit + 1]
            sfarsit -= 1
    return subMaxima

def test_subsecventa_munte():
    """
    Funtia testeaza functionalitatea functiei subsecventa_munte
    """
    assert subsecventa_munte([2, 3, 2, 1, 6]) == [2, 3, 2, 1]
    assert subsecventa_munte([]) == []
    assert subsecventa_munte([1]) == []
    assert subsecventa_munte([2, 3, 3]) == []
    assert subsecventa_munte([1, 2, 3, 4, 3, 1, -1, 2]) == [1, 2, 3, 4, 3, 1, -1]
    assert subsecventa_munte([1, 2, 1]) == [1, 2, 1]
    assert subsecventa_munte([1, 2, 2, 1]) == []

# end 15.

# 3. Oricare doua elemente consecutive sunt relativ prime intre ele

def cmmdc(a, b):
    """
    Functia returneaza pentru doua numere a si b, cel mai mic divizor comun al lor
    Daca unul din parametri e un numar negativ, functia va returna 0
    Daca unul din parametri e numar nenul funtia il va returna pe celalat (daca este pozitiv)
    """
    if a < 0 or b < 0:
        return 0
    while b:
        r = a % b
        a = b
        b = r
    return a

def test_cmmdc():
    """
    Functia testeaza functionalitatea functiei cmmdc
    """
    assert cmmdc(1, 2) == 1
    assert cmmdc(0, 2) == 2
    assert cmmdc(3, 0) == 3
    assert cmmdc(-10, 100) == 0
    assert cmmdc(-1, -2) == 0
    assert cmmdc(625, 25) == 25
    assert cmmdc(1024, 6) == 2
    assert cmmdc(3, 33) == 3
    assert cmmdc(11, 11) == 11
    assert cmmdc(11, 41) == 1

def subsecventa_relPrime(lista):
    """
    Functia primeste prin parametru lista, o lista de numere intregi
    Functia returneaza subsecventa de lungime maxima unde oricare doua elemente consecutive sunt relativ prime intre ele
    Daca nu exita o astfel de subsecventa cu minim 2 elemente, functia va returna o lista vida
    Daca exista mai multe subsecvente de acest tip, functia o va returna pe prima gasita
    """
    length = len(lista)
    subMaxima = []
    for start in range(0, length):
        sfarsit = length - 1
        while sfarsit > start:
            index = start
            verify = True
            while index < sfarsit and verify:
                if cmmdc(lista[index], lista[index + 1]) != 1:
                    verify = False
                index += 1
            if verify and sfarsit - start + 1> len(subMaxima):
                subMaxima = lista[start:sfarsit + 1]
            sfarsit -= 1
    return subMaxima

def test_subsecventa_relPrime():
    """
    Functia verifica functionalitatea functiei subsecventa_relPrime
    """
    assert subsecventa_relPrime([1, 2, 3]) == [1, 2, 3]
    assert subsecventa_relPrime([1, 5, 25]) == [1, 5]
    assert subsecventa_relPrime([]) == []
    assert subsecventa_relPrime([625, 5, 125]) == []
    assert subsecventa_relPrime([-1, 10, 22]) == []
    assert subsecventa_relPrime([100, 10, 20, 1, 2, 1, -3]) == [20, 1, 2, 1]

# end 3.

# 12. are oricare doua elemente consecutive sunt de semne contrare

def subsecventa_contrara(lista):
    """
    Functia primeste prin parametru lista, o lista de numere intregi
    Functia returneaza subsecventa maxima cu oricare doua elemente consecutive, de semne contrare
    Daca nu exita o astfel de subsecventa cu minim 2 elemente, functia va returna o lista vida
    Daca exista mai multe subsecvente de acest tip, functia o va returna pe prima gasita
    """
    length = len(lista)
    subMaxima = []
    for start in range(0, length):
        sfarsit = length - 1
        while sfarsit > start:
            index = start
            verify = True
            while index < sfarsit and verify:
                if lista[index] * lista[index + 1] >= 0:
                    verify = False
                index += 1
            if verify and sfarsit - start + 1 > len(subMaxima):
                subMaxima = lista[start:sfarsit + 1]
            sfarsit -= 1
    return subMaxima

def test_subsecventa_contrara():
    """
    Functia testeaza functionalitatea functiei subsecventa_contrara
    """
    assert subsecventa_contrara([]) == []
    assert subsecventa_contrara([1, 2, -1]) == [2, -1]
    assert subsecventa_contrara([1, 2, 3, 4]) == []
    assert subsecventa_contrara([-2, -10, 10, 100]) == [-10, 10]
    assert subsecventa_contrara([-2, 10, -10, 100]) == [-2, 10, -10, 100]
    assert subsecventa_contrara([0, 0, 10]) == []
    assert subsecventa_contrara([0, 10, -2, 1000000]) == [10, -2, 1000000]
    assert subsecventa_contrara([12345, 0, -10, 20]) == [-10, 20]

# end 12.

lista = []

# teste
test_subsecventa_sumFive()
test_subsecventa_munte()
test_cmmdc()
test_subsecventa_relPrime()
test_subsecventa_contrara()
# end teste

while True:
    afisare_meniu()
    comanda = input()
    if comanda == '1':
        citire(lista)
    elif comanda == '2':
        print(subsecventa_sumFive(lista))
    elif comanda == '3':
        print(subsecventa_munte(lista))
    elif comanda == '4':
        print(subsecventa_relPrime(lista))
    elif comanda == '5':
        print(subsecventa_contrara(lista))
    elif comanda == '0':
        break
    else:
        print("Comanda invalida")

## 3 si 12 - TEMA