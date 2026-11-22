# -*- coding: utf-8 -*-
"""
grade.py - correttore della Simulazione Claude 3 (immagini).

    python grade.py              -> tutti i test
    python grade.py func3        -> solo i test di func3 (anche: func1 func4 ...)
    python grade.py --debug      -> mostra lo stack trace completo degli errori
    NO_COLOR=1 python grade.py   -> senza colori

Il punteggio di ogni test viene scritto anche in grade.csv.
"""
import os
import sys

import testlib
from testlib import verde, rosso, giallo, grassetto

import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

DEBUG = '--debug' in sys.argv    # oppure metti True per vedere sempre lo stack trace

PUNTI = {'func1': 6, 'func2': 7, 'func3': 9, 'func4': 8}


def test_personal_data_entry():
    mancanti = [v for v, segnaposto in (('nome', 'NOME'), ('cognome', 'COGNOME'),
                                        ('matricola', 'MATRICOLA'))
                if getattr(program, v, segnaposto) == segnaposto]
    if mancanti:
        print(giallo(f'ERRORE: assegna in program.py le variabili: {", ".join(mancanti)}'))
        return False
    print(verde(f'Dati studente: {program.nome} {program.cognome} {program.matricola}'))
    return True


def _pulisci(path):
    if os.path.exists(path):
        os.remove(path)


# % ----------------------------------- FUNC1 ------------------------- #

def do_test_func1(ID, soglia, expected):
    img_in = f'func1/img{ID}_in.png'
    res = program.func1(img_in, soglia)
    if res is None:
        raise testlib.NotImplemented
    testlib.check_val(res, expected, cosa=f'risultato di func1({img_in!r}, {soglia})')
    return PUNTI['func1'] / 4


def test_func1_1():
    '''func1/img1_in.png, soglia=128'''
    return do_test_func1(1, 128, (506, 694))

def test_func1_2():
    '''func1/img2_in.png, soglia=100'''
    return do_test_func1(2, 100, (448, 177))

def test_func1_3():
    '''func1/img3_in.png, soglia=200'''
    return do_test_func1(3, 200, (18, 2682))

def test_func1_4():
    '''func1/img4_in.png, soglia=120 (tante luminosità vicine alla soglia)'''
    return do_test_func1(4, 120, (448, 329))


# % ----------------------------------- FUNC2 ------------------------- #

def do_test_func2(ID, expected):
    img_in = f'func2/img{ID}_in.png'
    img_out = f'func2/img{ID}_out.png'
    img_exp = f'func2/img{ID}_exp.png'
    _pulisci(img_out)
    res = program.func2(img_in, img_out)
    if res is None:
        raise testlib.NotImplemented
    testlib.check_img_file(img_out, img_exp)
    testlib.check_val(res, expected, cosa=f'numero di pixel uguali restituito da func2')
    return PUNTI['func2'] / 4


def test_func2_1():
    '''func2/img1_in.png -> func2/img1_out.png (immagine già simmetrica)'''
    return do_test_func2(1, 400)

def test_func2_2():
    '''func2/img2_in.png -> func2/img2_out.png (larghezza dispari)'''
    return do_test_func2(2, 279)

def test_func2_3():
    '''func2/img3_in.png -> func2/img3_out.png (più alta che larga)'''
    return do_test_func2(3, 300)

def test_func2_4():
    '''func2/img4_in.png -> func2/img4_out.png'''
    return do_test_func2(4, 209)


# % ----------------------------------- FUNC3 ------------------------- #

def do_test_func3(ID, expected):
    txt = f'func3/disegno{ID}.txt'
    img_out = f'func3/disegno{ID}_out.png'
    img_exp = f'func3/disegno{ID}_exp.png'
    _pulisci(img_out)
    res = program.func3(txt, img_out)
    if res is None:
        raise testlib.NotImplemented
    testlib.check_img_file(img_out, img_exp)
    testlib.check_dict(res, expected, cosa='dizionario restituito da func3')
    return PUNTI['func3'] / 4


def test_func3_1():
    '''func3/disegno1.txt (l'esempio del testo)'''
    return do_test_func3(1, {'RETT': 1, 'ORIZ': 1, 'VERT': 1, 'PUNTO': 1})

def test_func3_2():
    '''func3/disegno2.txt (con un commento)'''
    return do_test_func3(2, {'RETT': 2, 'ORIZ': 3, 'VERT': 2, 'PUNTO': 3})

def test_func3_3():
    '''func3/disegno3.txt (figure che escono dall'immagine)'''
    return do_test_func3(3, {'VERT': 5, 'ORIZ': 2, 'PUNTO': 4, 'RETT': 3})

def test_func3_4():
    '''func3/disegno4.txt (commenti, righe vuote, figure fuori)'''
    return do_test_func3(4, {'RETT': 9, 'ORIZ': 10, 'PUNTO': 10, 'VERT': 11})


# % ----------------------------------- FUNC4 ------------------------- #

def do_test_func4(ID, expected):
    img_in = f'func4/tela{ID}.png'
    txt = f'func4/comandi{ID}.txt'
    img_out = f'func4/tela{ID}_out.png'
    img_exp = f'func4/tela{ID}_exp.png'
    _pulisci(img_out)
    res = program.func4(img_in, txt, img_out)
    if res is None:
        raise testlib.NotImplemented
    testlib.check_img_file(img_out, img_exp)
    testlib.check_val(res, expected, cosa='tupla (x, y, passi) restituita da func4')
    return PUNTI['func4'] / 4


def test_func4_1():
    '''func4/tela1.png + func4/comandi1.txt (l'esempio del testo)'''
    return do_test_func4(1, (2, 2, 20))

def test_func4_2():
    '''func4/tela2.png + func4/comandi2.txt (con COLORE)'''
    return do_test_func4(2, (16, 14, 50))

def test_func4_3():
    '''func4/tela3.png + func4/comandi3.txt (con COLORE e SALTA)'''
    return do_test_func4(3, (23, 18, 163))

def test_func4_4():
    '''func4/tela4.png + func4/comandi4.txt (percorso lungo)'''
    return do_test_func4(4, (57, 33, 689))


# % --------------------- TESTS ---------------------
tests = [
    # PER ESEGUIRE SOLO ALCUNI TEST, commenta le voci che non ti servono
    # (oppure lancia: python grade.py func2)
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
]

if __name__ == '__main__':
    # lavora sempre nella cartella di grade.py (utile se lo lanci da Spyder/VS Code)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if not test_personal_data_entry():
        print(rosso(grassetto('DATI PERSONALI MANCANTI: compila nome, cognome e matricola in program.py')))
        sys.exit(1)
    testlib.check_expected()

    scelte = [a for a in sys.argv[1:] if a.startswith('func')]
    da_fare = [t for t in tests if not scelte or t.__name__.split('_')[1] in scelte]
    if scelte:
        print(giallo(f'Eseguo solo i test di: {", ".join(scelte)}'))
    print()
    testlib.runtests(da_fare, {f: p for f, p in PUNTI.items()
                               if any(t.__name__.split('_')[1] == f for t in da_fare)},
                     logfile='grade.csv', stack_trace=DEBUG)
    print(f'Nome: {program.nome}   Cognome: {program.cognome}   Matricola: {program.matricola}')
################################################################################
