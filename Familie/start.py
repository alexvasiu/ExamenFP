"""
Program principal :
    - se ruleza toate testele
    - se porneste interfata
"""

from UI import UI
from Tests import *

if __name__ == "__main__":
    test_get_index()
    test_adauga_cheltuiala()
    test_stergere()
    test_cautare()
    test_rapoarte()
    test_filtrare()
    test_undo()
    UI()