# -*- coding: utf-8 -*-
import testlib
from testlib import my_print, COL

import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
# %% ---------------------- DEBUG VARIABLE -------------------
DEBUG = False   # set to True for full tracebacks

#############################################################################
# %% ---------------------- TEST SECTION -------------------
#############################################################################

def test_personal_data_entry():
    assert program.nome      != 'NOME',      f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
    assert program.cognome   != 'COGNOME',   f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
    assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 1e-9

###########################################################################################################################
# ----------------------------------------- FUNC 1 TESTS (8 punti: 4 test x 2) -----------------------------------------
###########################################################################################################################

def do_func1_tests(vector, word, expected):
    res = program.func1(vector, word)
    if res is None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f"{'*'*50}\n[ERROR] Il numero TOTALE di stringhe contate atteso è {expected} e non {res}.\n{'*'*50}")
        return 0
    return 2

def test_func1_1():
    vector = ["Apple", "Banana", "Axe", "Avocado", "Ant", "Air", "Berry"]
    word = "Arc"
    expected = 3
    return do_func1_tests(vector, word, expected)

def test_func1_2():
    # stesso primo carattere ma lunghezze diverse ("c", "cats") vanno escluse
    vector = ["cat", "dog", "cow", "car", "cut", "cup", "c", "cats"]
    word = "cap"
    expected = 5
    return do_func1_tests(vector, word, expected)

def test_func1_3():
    # case-sensitive: "HELLO" e "Hello" iniziano con 'H', non con 'h'
    vector = ["HELLO", "World", "house", "Home", "Hello", "hello"]
    word = "heavy"
    expected = 2
    return do_func1_tests(vector, word, expected)

def test_func1_4():
    # nessuna stringa soddisfa entrambe le condizioni
    vector = ["a", "bb", "ccc", "Xyz", "xy", "xyzw"]
    word = "xyz"
    expected = 0
    return do_func1_tests(vector, word, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 2 TESTS (8 punti: 4 test x 2) -----------------------------------------
###########################################################################################################################

def do_func2_tests(data, expected):
    res = program.func2(data)
    if res is None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f"{'*'*50}\n[ERROR] La lista ritornata è sbagliata!\nReturned={res}, expected={expected}.\n{'*'*50}")
        return 0
    return 2

def test_func2_1():
    data = [(3, "cat"), (5, "giraffa"), (4, "cat"), (6, "snake"), (5, "zebra")]
    expected = ['giraffa']
    return do_func2_tests(data, expected)

def test_func2_2():
    data = [(2, "code"), (3, "data"), (4, "py"), (1, "x"), (3, "java"), (5, "rust")]
    expected = ['code', 'data', 'java']
    return do_func2_tests(data, expected)

def test_func2_3():
    # k = 0, lunghezza uguale a k esclusa, duplicati mantenuti
    data = [(0, "a"), (1, "bb"), (2, "ccc"), (3, "ddd"), (0, ""), (1, "bb")]
    expected = ['a', 'bb', 'ccc', 'bb']
    return do_func2_tests(data, expected)

def test_func2_4():
    data = []
    expected = []
    return do_func2_tests(data, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 3 TESTS (16 punti: 4 test x 4) -----------------------------------------
###########################################################################################################################

def do_func3_tests(points, expected):
    res = program.func3(points)
    if res is None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f"{'*'*50}\n[ERROR] La tupla ritornata è sbagliata!\nReturned={res}, expected={expected}.\n{'*'*50}")
        return 0
    return 4

def test_func3_1():
    # N dispari
    points = [(10, 5), (2, 8), (2, 4), (5, 12), (1, 6)]
    expected = (4.0, 6.0)
    return do_func3_tests(points, expected)

def test_func3_2():
    # N pari: mediana = media dei due valori centrali
    points = [(0, 10), (0, 20), (0, 30), (5, 5)]
    expected = (1.25, 15.0)
    return do_func3_tests(points, expected)

def test_func3_3():
    # arrotondamento a 2 cifre di Mx (7/3), coordinate Y non ordinate
    points = [(1, 1), (3, 3), (3, 2)]
    expected = (2.33, 2.0)
    return do_func3_tests(points, expected)

def test_func3_4():
    # float, valori negativi, N pari
    points = [(-5.5, 10.0), (-2.0, 4.0), (-5.5, 2.0), (10.0, 0.0)]
    expected = (-0.75, 3.0)
    return do_func3_tests(points, expected)

###########################################################################################################################

tests = [
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,  # 8 pt
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,  # 8 pt
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,  # 16 pt
    test_personal_data_entry,
]

if __name__ == '__main__':
    test_personal_data_entry()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
