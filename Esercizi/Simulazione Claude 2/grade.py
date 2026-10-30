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
# DEBUG = True    # with    stack trace of errors
DEBUG = False   # without stack trace of errors

#############################################################################
# %% ---------------------- TEST SECTION -------------------
#############################################################################

def test_personal_data_entry():
    assert program.nome      != 'NOME',      f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
    assert program.cognome   != 'COGNOME',   f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
    assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 1e-9

###########################################################################################################################
# ----------------------------------------- FUNC 1 TESTS -----------------------------------------
###########################################################################################################################

def do_func1_tests(a_dict, char, a_dict_exp, expected):
    res = program.func1(a_dict, char)
    if res == None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il numero TOTALE di elementi rimossi atteso è {expected} e non {res}. / Total elements removed should be {expected}, but {res} were returned.\n {'*'*50}''')
        return 0
    testlib.checkDict(a_dict, a_dict_exp)
    return 1

def test_func1_1():
    a_dict = {'x': ['banana', 'Anna', 'kiwi'], 'y': ['casa', 'alba']}
    char = 'a'
    a_dict_exp = {'x': ['kiwi']}
    expected = 4
    return do_func1_tests(a_dict, char, a_dict_exp, expected)

def test_func1_2():
    a_dict = {'p': ['Eden', 'eke', 'ape', 'Bee', 'tree'], 'q': ['sole', 'mare']}
    char = 'E'
    a_dict_exp = {'p': ['ape'], 'q': ['sole', 'mare']}
    expected = 4
    return do_func1_tests(a_dict, char, a_dict_exp, expected)

def test_func1_3():
    a_dict = {'a': ['ciao', 'mondo'], 'b': ['python']}
    char = 'z'
    a_dict_exp = {'a': ['ciao', 'mondo'], 'b': ['python']}
    expected = 0
    return do_func1_tests(a_dict, char, a_dict_exp, expected)

def test_func1_4():
    a_dict = {'k1': ['ll', 'Lilla'], 'k2': ['ballo', 'LOL', 'pollo'], 'k3': ['nulla', 'sole']}
    char = 'l'
    a_dict_exp = {'k3': ['sole']}
    expected = 6
    return do_func1_tests(a_dict, char, a_dict_exp, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 2 TESTS -----------------------------------------
###########################################################################################################################

def do_func2_tests(dictionary, soglia, expected):
    res = program.func2(dictionary, soglia)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] La lista ritornata è sbagliata! / The returned list is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func2_1():
    dictionary = {'anna': [7, 8, 9], 'bruno': [10, 10], 'carla': [5, 5, 5, 5], 'dario': [3]}
    expected = ['anna', 'bruno', 'carla']
    return do_func2_tests(dictionary, 19, expected)

def test_func2_2():
    dictionary = {'zeta': [5, 5], 'alfa': [10], 'beta': [1, 2, 3, 4, 1], 'gamma': []}
    expected = ['beta', 'alfa', 'zeta']
    return do_func2_tests(dictionary, 0, expected)

def test_func2_3():
    dictionary = {'a': [-5, 2], 'b': [-1], 'c': [0, 0], 'd': [-10, 20]}
    expected = ['d', 'c', 'b']
    return do_func2_tests(dictionary, -2, expected)

def test_func2_4():
    dictionary = {}
    expected = []
    return do_func2_tests(dictionary, 5, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 3 TESTS -----------------------------------------
###########################################################################################################################

def do_func3_tests(a_list, expected):
    res = program.func3(a_list)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}\nexpected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func3_1():
    a_list = ["a1b2", "33", "abc", "9"]
    expected = [0, 1, 2]
    return do_func3_tests(a_list, expected)

def test_func3_2():
    a_list = ["2026", "ottobre", "17", "10", "x"]
    expected = [0, 2, 4]
    return do_func3_tests(a_list, expected)

def test_func3_3():
    a_list = []
    expected = []
    return do_func3_tests(a_list, expected)

def test_func3_4():
    a_list = ["", "1a2b3c", "abc123", "999"]
    expected = [0, 3]
    return do_func3_tests(a_list, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 4 TESTS -----------------------------------------
###########################################################################################################################

def do_func4_tests(string_list1, string_list2, expected):
    res = program.func4(string_list1, string_list2)
    testlib.checkList(res, expected)
    return 1.5

def test_func4_1():
    string_list1 = ['mela', 'kiwi', 'banana', 'uva', 'kiwi']
    string_list2 = ['uva', 'kiwi', 'pera', 'banana']
    expected = ['banana', 'kiwi', 'uva']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_2():
    string_list1 = ['Alba', 'eco', 'eco', 'tre', 'Idea']
    string_list2 = ['eco', 'Idea', 'eco', 'Alba', 'sei']
    expected = ['Idea', 'Alba', 'eco']
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_3():
    string_list1 = ['sole', 'mare']
    string_list2 = ['luna', 'Sole']
    expected = []
    return do_func4_tests(string_list1, string_list2, expected)

def test_func4_4():
    string_list1 = ['brr', 'psst', 'ok', 'zz', 'ai']
    string_list2 = ['zz', 'ai', 'ok', 'brr', 'psst', 'xx']
    expected = ['ai', 'ok', 'brr', 'psst', 'zz']
    return do_func4_tests(string_list1, string_list2, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 5 TESTS -----------------------------------------
###########################################################################################################################
def do_func5(points, expected):
    points_copy = points[:]
    res = program.func5(points)
    if res != expected:
        my_print(f'''{'*' * 50}\n[ERROR] La tupla ritornata è sbagliata! / The returned tuple is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{'*' * 50}''')
        return 0
    if points != points_copy:
        my_print(f'''{'*' * 50}\n[ERROR] La lista points è stata modificata! / The input list has been modified!''')
        my_print(f'''Now={points}, before={points_copy}.\n{'*' * 50}''')
        return 0
    return 2

def test_func5_1():
    points = [(4, 1), (1, 2), (3, 5), (1, 7), (6, 0)]
    expected = (1.67, 4.67)
    return do_func5(points, expected)

def test_func5_2():
    points = [(2, 9), (0, 3), (2, 1), (0, 0), (2, 4), (5, 5)]
    expected = (0.67, 4.0)
    return do_func5(points, expected)

def test_func5_3():
    points = [(-3, 4), (5, -2), (0, 1)]
    expected = (0.67, 1.0)
    return do_func5(points, expected)

def test_func5_4():
    points = [(10 - x, x * x) for x in range(6)]
    expected = (6.0, 16.67)
    return do_func5(points, expected)

###########################################################################################################################
# ----------------------------------------- FUNC 6 TESTS -----------------------------------------
###########################################################################################################################

def do_func6_tests(text, expected):
    res = program.func6(text)

    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}, expected={expected}.\n{'*'*50}''')
        return 0
    return 1

def test_func6_1():
    text = 'Il gatto e il cane e il Gatto'
    expected = {2: ['il'], 5: ['gatto'], 1: ['e'], 4: ['cane']}
    return do_func6_tests(text, expected)

def test_func6_2():
    text = ''
    expected = {}
    return do_func6_tests(text, expected)

def test_func6_3():
    text = '  tanti   spazi  tra   le parole '
    expected = {5: ['tanti', 'spazi'], 3: ['tra'], 2: ['le'], 6: ['parole']}
    return do_func6_tests(text, expected)

def test_func6_4():
    text = 'Ciao CIAO ciao Mondo mondo MONDI'
    expected = {4: ['ciao'], 5: ['mondo', 'mondi']}
    return do_func6_tests(text, expected)

###########################################################################################################################

tests = [
    # TO DISABLE SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4, # OK 4
    test_func2_1, test_func2_2, test_func2_3, test_func2_4, # OK 4
    test_func3_1, test_func3_2, test_func3_3, test_func3_4, # OK 4
    test_func4_1, test_func4_2, test_func4_3, test_func4_4, # OK 6
    test_func5_1, test_func5_2, test_func5_3, test_func5_4, # OK 8
    test_func6_1, test_func6_2, test_func6_3, test_func6_4, # OK 4
    test_personal_data_entry,
]

if __name__ == '__main__':
    test_personal_data_entry()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################