#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
1) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
2) entro le 12.15 consegnare SOLO il file program.py su Classroom

Il voto finale e' la somma dei punteggi dei problemi risolti.
Si supera la simulazione se si raggiunge almeno 18.
I/le ragazzi/e con DSA devono raggiungere almeno 15
(e devono farmi comunicare dal Servizio DSA di Sapienza che sono DSA).

Attenzione! DEBUG=True nel grade.py per visualizzare la stack trace degli errori.
"""

nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

# ----------------------------------- EX.1 ----------------------------------- #

"""Func 1: 6 punti

Si progetti una funzione che riceve come argomenti i path di due file
dict1 e dict2 e ritorni come output un dizionario. I due file contengono
delle righe di testo con parole separate da spazi e/o tab, dalle quali la
funzione deve generare un dizionario considerando soltanto le righe che
hanno esattamente due parole: la prima parola sara' una chiave del
dizionario e la seconda sara' il valore a questa associato.

Il dizionario finale da ritornare deve avere:

- una chiave per ogni chiave presente in entrambi i dizionari
  costruiti da dict1 e dict2 seguendo la procedura sopra descritta,

- per valore la concatenazione mediante il carattere '/' (barra) dei due
  valori associati alla stessa chiave nei due dizionari, ordinati
  secondo l'ordine alfabetico.

Es: se dai due file dict1 e dict2 sono generati i dizionari
    {'a':'cane', 'c':'gatto'} e
    {'f':'giraffa', 'a':'bue'},
    la funzione deve ritornare il dizionario {'a':'bue/cane'}.
"""
def func1 (dict1, dict2):
    pass
    # completa il codice della funzione


#%% ----------------------------------- FUNC2 ------------------------- #
""" func2: 6 punti

Si scriva una funzione func2(input_file, output_file) che riceve come argomenti
due stringhe, 'input_file' e 'output_file', che rappresentano i percorsi a due
file. All'interno del file indicato da 'input_file' e' codificata una matrice:
ogni linea del file rappresenta una riga della matrice, con i valori separati
da punto e virgola e spazi.

Ad esempio func2/input_1.txt contiene:

1;    2;  3;            25
 4; 5;      6; 17
7;   8;    9;          42

La funzione deve leggere il file in 'input_file' e scrivere in 'output_file'
la stessa matrice, scrivendo ogni riga come una tupla di numeri interi
separati da virgola e spazio, racchiusa tra parentesi tonde:

(1, 2, 3, 25)
(4, 5, 6, 17)
(7, 8, 9, 42)

Infine la funzione deve ritornare il numero di elementi della matrice.
Si apra 'func2/input_1.txt' per vedere l'input e
'func2/expected_1.txt' per vedere l'output atteso.
"""

def func2(input_file, output_file):
    pass
    # completa il codice della funzione


# print(func2('func2/input_1.txt','func2/output_1.txt'))
# print(func2('func2/input_2.txt','func2/output_2.txt'))
# print(func2('func2/input_3.txt','func2/output_3.txt'))

#%% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 punti

Definisci una funzione func3(file_in, file_out, length, chars) che riceve come argomenti:
- due stringhe che rappresentano i percorsi di due file di testo
- un intero length,
- una stringa chars.
La funzione deve restituire l'elenco di tutte le parole trovate nel file puntato
da file_in con una lunghezza *al massimo* length e che NON contengano *nessuno*
dei caratteri nella stringa chars. Le parole sono separate da spazi o a capo.
L'elenco deve essere ordinato per lunghezza crescente e, in caso di parita', in
ordine alfabetico.
Inoltre, la funzione deve scrivere le parole dell'elenco nel file puntato da
file_out separate da uno spazio.

Esempio: func3('func3/in_01.txt', 'func3/out_01.txt', 4, 'ou')
     deve tornare la lista ['ape', 'cane']
     e scrivere la stringa 'ape cane' in func3/out_01.txt.
"""

def func3(file_in : str, file_out: str, length:int, chars:str) -> list[str]:
    pass
    # completa il codice della funzione


# print(func3('func3/in_01.txt', 'func3/out_01.txt', 4, 'ou')) # ['ape', 'cane']

# ---------------------------- FUNC 4 ---------------------------- #
'''
Func 4: 6 punti
Definite la funzione func4(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

Il file indicato da textfile_in contiene dei numeri float oppure interi,
positivi o negativi, separati da spazi e/o a capo.

La funzione deve leggere i numeri, ordinarli in ordine crescente di valore
assoluto e, in caso di parita' di valore assoluto, in ordine decrescente di
valore. Quindi deve scrivere questi numeri ordinati nel file textfile_out,
separati da virgola e spazio, scrivendo ogni numero esattamente come compare
nel file di input. Infine la funzione restituisce la quantita' di numeri letti
da textfile_in.

Esempio:
se il file textfile_in contiene la riga
-23 17 -141 4.5 -4.5 3
Nel file textfile_out la funzione deve scrivere la riga
3, 4.5, -4.5, 17, -23, -141
e tornare il valore 6
'''

def func4(textfile_in, textfile_out):
    pass
    # completa il codice della funzione


# print(func4('func4/in_1.txt', 'func4/output_1.txt')) # 6

# ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 6 punti
Si definisca la funzione func5(filein) che riceve come argomento
- filein: un file di testo contenente una matrice di interi NxM
  separati da spazi

e che ritorna la matrice ruotata di 90 gradi in senso orario. La matrice da
restituire e' rappresentata come lista di liste, e ha dimensioni MxN.

Esempio:
se il file filein contiene la matrice
1 2 3
4 5 6
la funzione dovra' tornare la matrice ruotata in senso orario,
come lista di liste
[[4, 1],
 [5, 2],
 [6, 3]]
'''
def func5(input_filename):
    pass
    # completa il codice della funzione


# ---------------------------- EOF ---------------------------- #
