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

def do_func1_tests(str_list, expected):
    res = program.func1(str_list)
    if res is None:
        raise testlib.NotImplemented()
    testlib.checkList(res, expected)
    return 2

def test_func1_1():
    str_list = ["python", "chat", "code", "ai"]
    expected = [0, 2, 3, 5]
    return do_func1_tests(str_list, expected)

def test_func1_2():
    str_list = ["aeiou", "bcd", "hello world"]
    expected = [0, 3, 7]
    return do_func1_tests(str_list, expected)

def test_func1_3():
    str_list = []
    expected = []
    return do_func1_tests(str_list, expected)

def test_func1_4():
    # caratteri non alfabetici ignorati, stringa vuota, 'y' è una consonante,
    # input non ordinato
    str_list = ["rhythm & fly!", "123", "", "zzz", "queue", "xyz y"]
    expected = [0, 0, 1, 3, 4, 9]
    return do_func1_tests(str_list, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 2 TESTS (8 punti: 4 test x 2) -----------------------------------------
###########################################################################################################################

def do_func2_tests(text, expected):
    res = program.func2(text)
    if res is None:
        raise testlib.NotImplemented()
    if res != expected:
        hint = ""
        if isinstance(res, list) and any(isinstance(el, tuple) for el in res):
            hint = "\nSuggerimento: ogni elemento deve essere una LISTA [vocale, frequenza], non una tupla."
        my_print(f"{'*'*50}\n[ERROR] La lista ritornata è sbagliata!\nReturned={res}, expected={expected}.{hint}\n{'*'*50}")
        return 0
    return 2

def test_func2_1():
    text = "an apple a day keeps the doctor away!"
    expected = [['a', 6], ['e', 4], ['i', 0], ['o', 2], ['u', 0]]
    return do_func2_tests(text, expected)

def test_func2_2():
    text = "banana e kiwi"
    expected = [['a', 3], ['e', 1], ['i', 2], ['o', 0], ['u', 0]]
    return do_func2_tests(text, expected)

def test_func2_3():
    text = "aeiou aeiou"
    expected = [['a', 2], ['e', 2], ['i', 2], ['o', 2], ['u', 2]]
    return do_func2_tests(text, expected)

def test_func2_4():
    # nessuna vocale ('y' non è una vocale): tutte le frequenze a 0
    text = "rhythm & fly!"
    expected = [['a', 0], ['e', 0], ['i', 0], ['o', 0], ['u', 0]]
    return do_func2_tests(text, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 3 TESTS (16 punti: 4 test x 4) -----------------------------------------
###########################################################################################################################

def do_func3_tests(list1, list2, expected):
    res = program.func3(list1, list2)
    if res is None:
        raise testlib.NotImplemented()
    testlib.checkList(res, expected)
    return 4

def test_func3_1():
    list1 = ["a123", "b12", "c12", "test", "a123", "no_digits"]
    list2 = ["test", "other"]
    expected = ['a123', 'b12', 'c12', 'no_digits']
    return do_func3_tests(list1, list2, expected)

def test_func3_2():
    # input non ordinato, duplicati in list1, ordinamento alfabetico
    list1 = ["x1", "y22", "z333", "w", "x1"]
    list2 = ["y22"]
    expected = ['w', 'x1', 'z333']
    return do_func3_tests(list1, list2, expected)

def test_func3_3():
    list1 = ["apple", "banana"]
    list2 = ["apple", "banana"]
    expected = []
    return do_func3_tests(list1, list2, expected)

def test_func3_4():
    # list2 vuota: solo rimozione dei duplicati e ordinamento
    list1 = ["ghi99", "abc9", "def8", "abc9"]
    list2 = []
    expected = ['abc9', 'def8', 'ghi99']
    return do_func3_tests(list1, list2, expected)

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
