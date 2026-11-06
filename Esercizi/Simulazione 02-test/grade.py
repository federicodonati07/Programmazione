# -*- coding: utf-8 -*-
import testlib, os
from testlib import my_print, COL, test_personal_data_entry

# Import the student's code
import program

###############################################################################
#### Mettete DEBUG=True per fare debug delle funzioni più facilmente attivando
#### la stack trace degli errori (più verbosa)
DEBUG = True
# DEBUG = False
###############################################################################

SEP = '*' * 50

################################################################################
################################################################################
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################
################################################################################

################################################################################
# %% ---------------------- TEST SECTION -------------------
################################################################################

# ----------------------------------- Func.1 ----------------------------------- #

def do_func1_tests(ID, expected):
    f1 = f'func1/input_{ID}_a.txt'
    f2 = f'func1/input_{ID}_b.txt'
    res = program.func1(f1, f2)
    if res is None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f"[ERROR] Wrong return value! Returned={res}, expected={expected}")
        return 0
    return 2

def test_func1_1():
    '''
    file_input_a = 'func1/input_0_a.txt'
    file_input_b = 'func1/input_0_b.txt'
    '''
    expected = {'x': '0/1', 'y': '2/7'}
    return do_func1_tests('0', expected)

def test_func1_2():
    '''
    file_input_a = 'func1/input_1_a.txt'
    file_input_b = 'func1/input_1_b.txt'
    '''
    expected = {'casa': 'rossa/verde', 'mare': 'blu/blu', 'sole': 'azzurro/giallo'}
    return do_func1_tests('1', expected)

def test_func1_3():
    '''
    file_input_a = 'func1/input_2_a.txt'
    file_input_b = 'func1/input_2_b.txt'
    '''
    expected = {'re': '1/8', 'mi': '2/7', 'fa': '0/3', 'sol2': '5/9'}
    return do_func1_tests('2', expected)


# %% ----------------------------------- FUNC 2 ------------------------- #

def do_func2_tests(ID, expected):
    input_file    = f'func2/input_{ID}.txt'
    output_file   = f'func2/output_{ID}.txt'
    expected_file = f'func2/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_file):
        os.remove(output_file)

    res = program.func2(input_file, output_file)
    if res is None:
        raise testlib.NotImplemented()
    if res != expected:
        my_print(f'''{SEP}\n[ERROR] Il valore ritornato non è corretto! / Returned value is incorrect!\n'''
                 f'''[ERROR] Expected {expected} returned {res}\n{SEP}''')
        return 0
    testlib.check_text_file(output_file, expected_file)
    return 2

def test_func2_1():
    '''
    input_file = func2/input_1.txt
    output_file = func2/output_1.txt
    expected = 12
    '''
    return do_func2_tests(1, 12)

def test_func2_2():
    '''
    input_file = func2/input_2.txt
    output_file = func2/output_2.txt
    expected = 6
    '''
    return do_func2_tests(2, 6)

def test_func2_3():
    '''
    input_file = func2/input_3.txt
    output_file = func2/output_3.txt
    expected = 20
    '''
    return do_func2_tests(3, 20)


# %%----------------------------------- Func 3 ----------------------------------- #

def do_func3_tests(ID, length, chars, expected):
    input_filename    = f'func3/in_0{ID}.txt'
    output_filename   = f'func3/out_0{ID}.txt'
    expected_filename = f'func3/exp_0{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_filename):
        os.remove(output_filename)

    res = program.func3(input_filename, output_filename, length, chars)
    testlib.checkList(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 2

def test_func3_1():
    '''
    input_filename = 'func3/in_01.txt'
    output_filename = 'func3/out_01.txt'
    expected_filename = 'func3/exp_01.txt'
    length = 4
    chars = 'ou'
    expected = ['ape', 'cane']
    '''
    return do_func3_tests(1, 4, 'ou', ['ape', 'cane'])

def test_func3_2():
    '''
    input_filename = 'func3/in_02.txt'
    output_filename = 'func3/out_02.txt'
    expected_filename = 'func3/exp_02.txt'
    length = 5
    chars = 'lr'
    expected = ['su', 'monti', 'nuovi']
    '''
    return do_func3_tests(2, 5, 'lr', ['su', 'monti', 'nuovi'])

def test_func3_3():
    '''
    input_filename = 'func3/in_03.txt'
    output_filename = 'func3/out_03.txt'
    expected_filename = 'func3/exp_03.txt'
    length = 5
    chars = 'x'
    expected = ['aria', 'sole', 'acqua', 'fuoco', 'terra', 'vento']
    '''
    return do_func3_tests(3, 5, 'x', ['aria', 'sole', 'acqua', 'fuoco', 'terra', 'vento'])


# ----------------------------------- FUNC. 4 ----------------------------------- #

def do_func4_tests(ID, expected):
    input_filename    = f'func4/in_{ID}.txt'
    output_filename   = f'func4/your_output_{ID}.txt'
    expected_filename = f'func4/expected_{ID}.txt'

    # remove the previous output each time if it is there
    if os.path.exists(output_filename):
        os.remove(output_filename)

    res = program.func4(input_filename, output_filename)
    if res != expected:
        my_print(f'''{SEP}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!''')
        my_print(f'''Returned={res}, expected={expected}.\n{SEP}''')
        return 0
    testlib.check_text_file(output_filename, expected_filename)
    return 1.5

def test_func4_1():
    '''
    textfile_in  = 'func4/in_1.txt'
    textfile_out = 'func4/your_output_1.txt'
    expected     = 'func4/expected_1.txt'
    result       = 6
    '''
    return do_func4_tests(1, 6)

def test_func4_2():
    '''
    textfile_in  = 'func4/in_2.txt'
    textfile_out = 'func4/your_output_2.txt'
    expected     = 'func4/expected_2.txt'
    result       = 6
    '''
    return do_func4_tests(2, 6)

def test_func4_3():
    '''
    textfile_in  = 'func4/in_3.txt'
    textfile_out = 'func4/your_output_3.txt'
    expected     = 'func4/expected_3.txt'
    result       = 10
    '''
    return do_func4_tests(3, 10)

def test_func4_4():
    '''
    textfile_in  = 'func4/in_4.txt'
    textfile_out = 'func4/your_output_4.txt'
    expected     = 'func4/expected_4.txt'
    result       = 9
    '''
    return do_func4_tests(4, 9)


# ----------------------------------- FUNC. 5 ----------------------------------- #

def do_func5_tests(ID, expected):
    input_filename = f'func5/in_{ID}.txt'
    res = program.func5(input_filename)
    if res != expected:
        my_print(f'''{SEP}\n[ERROR] Il risultato è sbagliato! / The result is incorrect!\nReturned={res}, expected={expected}.\n{SEP}''')
        return 0
    return 1.5

def test_func5_1():
    '''
    input_filename = 'func5/in_1.txt'
    expected = [[4, 1], [5, 2], [6, 3]]
    '''
    return do_func5_tests(1, [[4, 1], [5, 2], [6, 3]])

def test_func5_2():
    '''
    input_filename = 'func5/in_2.txt'
    expected = [[4, 2, -1], [5, -3, 0]]
    '''
    return do_func5_tests(2, [[4, 2, -1], [5, -3, 0]])

def test_func5_3():
    '''
    input_filename = 'func5/in_3.txt'
    expected = [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]
    '''
    return do_func5_tests(3, [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]])

def test_func5_4():
    '''
    input_filename = 'func5/in_4.txt'
    expected = [[3], [-1], [0], [8], [2]]
    '''
    return do_func5_tests(4, [[3], [-1], [0], [8], [2]])


################################################################################
# %% --------------------- TESTS ---------------------
tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1,   test_func1_2,   test_func1_3,
    test_func2_1,   test_func2_2,   test_func2_3,
    test_func3_1,   test_func3_2,   test_func3_3,
    test_func4_1,   test_func4_2,   test_func4_3,   test_func4_4,
    test_func5_1,   test_func5_2,   test_func5_3,   test_func5_4,
    test_personal_data_entry,
]

# %% --------------------- MAIN ---------------------
if __name__ == '__main__':
    test_personal_data_entry()
    # Check that input files have not been changed
    testlib.check_expected()
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)

################################################################################
# %% --------------------- END OF FILE ---------------------
