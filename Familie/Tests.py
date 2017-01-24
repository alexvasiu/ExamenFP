"""
Modul ce contine toate testele
"""

from Familie import adauga_cheltuiala, get_index, sterge, cautare, rapoarte, filtrare, undo
from Domain import *


def test_adauga_cheltuiala():
    """
    Testeaza functionalitatea functiei adauga_cheltuiala
    """
    cheltuieli = creeaza()
    try:
        adauga_cheltuiala(0, 20, "", cheltuieli)
        assert False
    except ValueError:
        assert True
    try:
        adauga_cheltuiala(10, -20, "", cheltuieli)
        assert False
    except ValueError:
        assert True
    try:
        adauga_cheltuiala(10, 20, "ceva", cheltuieli)
        assert False
    except ValueError:
        assert True
    adauga_cheltuiala(10, 20, "mancare", cheltuieli)
    assert cheltuieli[0][0] == [10, 20, "mancare"]
    adauga_cheltuiala(10, 10, "mancare", cheltuieli)
    assert cheltuieli[0][0] == [10, 30, "mancare"]
    adauga_cheltuiala(10, 10, "altele", cheltuieli)
    assert cheltuieli[0][1] == [10, 10, "altele"]
    adauga_cheltuiala(20, 20, "altele", cheltuieli)
    assert cheltuieli[0][2] == [20, 20, "altele"]


def test_get_index():
    """
    Testeaza functionalitatea functiei get_index
    """
    try:
        get_index(10, "", [[], []])
        assert False
    except ValueError:
        assert True
    try:
        get_index(310, "mancare", [[], []])
        assert False
    except ValueError:
        assert True
    assert get_index(10, "altele", [[[3, 10, "altele"]], []]) == -1
    assert get_index(10, "altele", [[[10, 10, "altele"]], []]) == 0
    assert get_index(10, "altele", [[[10, 10, "mancare"], [10, 33, "altele"]], []]) == 1
    assert get_index(10, "altele", [[], []]) == -1
    assert get_index(10, "mancare", [[[10, 10, "altele"], [4, 10, "mancare"]], []]) == -1


def test_stergere():
    """
    Testeaza functia sterge
    """
    cheltuieli = creeaza()
    adauga_cheltuiala(10, 10, "mancare", cheltuieli)
    adauga_cheltuiala(10, 20, "altele", cheltuieli)
    adauga_cheltuiala(11, 10, "mancare", cheltuieli)
    try:
        sterge(-10, -1, "Single", cheltuieli)
        assert False
    except ValueError:
        assert True
    try:
        sterge("ceva", -1, "Tip", cheltuieli)
        assert False
    except ValueError:
        assert True
    sterge(10, -1, "Single", cheltuieli)
    assert get_cheltuieli(cheltuieli) == [[10, 20, "altele"]]
    adauga_cheltuiala(10, 10, "mancare", cheltuieli)
    sterge(10, 20, "Interval", cheltuieli)
    assert cheltuieli[0] == []
    adauga_cheltuiala(10, 20, "mancare", cheltuieli)
    adauga_cheltuiala(9, 10, "mancare", cheltuieli)
    adauga_cheltuiala(10, 1, "altele", cheltuieli)
    adauga_cheltuiala(10, 2, "mancare", cheltuieli)
    sterge("mancare", -1, "Tip", cheltuieli)
    assert cheltuieli[0] == [[10, 1, "altele"]]


def test_cautare():
    """
    Testeaza funtia de cautare
    """
    try:
        cautare(-10, -1, "Single", [[], []])
        assert False
    except ValueError:
        assert True
    try:
        cautare(100, -10, "Multiple", [[], []])
        assert False
    except ValueError:
        assert True
    assert cautare(10, -1, "Single", [[], []]) == []
    assert cautare(10, -1, "Single", [[[11, 55, "altele"], [11, 10, "mancare"], [19, 3, "mancare"]], []]) == [
        [11, 55, "altele"]]
    assert cautare(1000, -1, "Single", [[[99, -1, "mancare"]], []]) == []
    assert cautare(100, 10, "Multiple", [[[9, 101, "mancare"], [11, 10, "altele"], [5, 10, "telefon"]], []]) == [
        [5, 10, "telefon"]]
    assert cautare("mancare", -1, "Tip", [[[9, 101, "mancare"], [11, 10, "altele"], [5, 10, "mancare"]], []]) == [
        [9, 101, "mancare"], [5, 10, "mancare"]]


def test_rapoarte():
    """
    Testeaza functia de rapoarte
    """
    try:
        rapoarte("ceva", "SumByTip", [[[10, 10, "altele"]], []])
        assert False
    except ValueError:
        assert True
    try:
        rapoarte(0, "Sum", [[[10, 10, "mancare"]], []])
        assert False
    except ValueError:
        assert True
    assert rapoarte("mancare", "SumByTip", [[[10, 10, "altele"]], []]) == 0
    assert rapoarte("altele", "SumByTip", [[[10, 10, "altele"]], []]) == 10
    assert rapoarte("mancare", "SumByTip", [[[10, 10, "altele"], [20, 5, "mancare"], [10, 13, "mancare"]], []]) == 18
    assert rapoarte(-1, "Maxim", [[[10, 20, "mancare"]], []]) == 10
    assert rapoarte(-1, "Maxim", [[], []]) == -1
    assert rapoarte(-1, "Maxim", [[[10, 20, "mancare"], [10, 10, "altele"], [11, 150, "telefon"]], []]) == 11
    assert rapoarte(10, "Sum", [[[10, 10, "mancare"]], []]) == [[10, 10, "mancare"]]
    assert rapoarte(100, "Sum", [[[10, 10, "mancare"]], []]) == []
    assert rapoarte(100, "Sum",
                    [[[10, 10, "mancare"], [1, 100, "telefon"], [2, 1, "imbracaminte"], [3, 100, "altele"]], []]) == [
               [1, 100, "telefon"], [3, 100, "altele"]]
    assert rapoarte(-1, "Sort", [[], []]) == {}
    assert rapoarte(-1, "Sort", [[[1, 2, "mancare"], [3, 10, "altele"], [4, 100, "mancare"]], []]) == {
        'mancare': [[1, 2, "mancare"], [4, 100, "mancare"]], 'altele': [[3, 10, "altele"]]}
    assert rapoarte(-1, "Sort", [[[1, 2, "altele"]], []]) == {'altele': [[1, 2, "altele"]]}


def test_filtrare():
    """
    Testeaza functia de filtrare
    """
    cheltuieli = creeaza()
    adauga_cheltuiala(10, 20, "mancare", cheltuieli)
    adauga_cheltuiala(11, 14, "mancare", cheltuieli)
    adauga_cheltuiala(4, 10, "altele", cheltuieli)
    try:
        filtrare("ce", "Tip", cheltuieli)
        assert False
    except ValueError:
        assert True
    try:
        filtrare(-32, "Sum", cheltuieli)
        assert False
    except ValueError:
        assert True
    assert filtrare("mancare", "Tip", cheltuieli) == [[4, 10, "altele"]]
    assert filtrare(100, "Sum", cheltuieli) == []
    assert filtrare("altele", "Tip", cheltuieli) == []


def test_undo():
    """
    Testeaza functia de undo
    """
    cheltuieli = creeaza()
    adauga_cheltuiala(10, 20, "mancare", cheltuieli)
    adauga_cheltuiala(11, 14, "mancare", cheltuieli)
    adauga_cheltuiala(4, 10, "altele", cheltuieli)
    undo(cheltuieli)
    assert undo(cheltuieli) == [[10, 20, "mancare"]]
    assert undo(cheltuieli) == []
    assert undo(cheltuieli) == []
    adauga_cheltuiala(10, 20, "mancare", cheltuieli)
    filtrare("mancare", "Tip", cheltuieli)
    assert undo(cheltuieli) == [[10, 20, "mancare"]]
    filtrare(22, "Sum", cheltuieli)
    assert undo(cheltuieli) == [[10, 20, "mancare"]]
    sterge(10, 20, "Interval", cheltuieli)
    assert undo(cheltuieli) == [[10, 20, "mancare"]]
