#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o uguale a 18.
"""

nome = "NOME"
cognome = "COGNOME"
matricola = "MATRICOLA"

################################################################################
################################################################################
################################################################################


################################################################################
# %% ----------------------------------- FUNC.1 ------------------------------ #
################################################################################
'''func1: 8 punti

Si definisca la funzione func1(vector, word) che prende in ingresso una
lista di stringhe 'vector' e una stringa 'word'. 
La funzione deve leggere tutte le stringhe in 'vector', 
contando tutte le stringhe che hanno la STESSA LUNGHEZZA di 'word' e che 
iniziano con lo STESSO PRIMO CARATTERE di 'word' (case-sensitive, cioè
considerando minuscole e maiuscole).

La funzione restituisce il numero TOTALE di stringhe contate.

Esempio:
vector = ["Apple", "Banana", "Axe", "Avocado", "Ant", "Air", "Berry"]
word = "Arc"
"Axe", "Ant", "Air" hanno lunghezza 3 e iniziano con 'A'
valore da ritornare = 3
'''
def func1(vector: list, word: str) -> int:
    pass

# vector = ["Apple", "Banana", "Axe", "Avocado", "Ant", "Air", "Berry"]
# word = "Arc"
# print(func1(vector, word)) # 3


################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 8 punti

Si definisca la funzione func2(data) che prende in ingresso una lista 'data'
di tuple (k, s), dove 'k' è un numero intero e 's' è una stringa.

La funzione costruisce e ritorna una nuova lista W contenente le stringhe 's'
di tutte le tuple (k, s) la cui lunghezza sia STRETTAMENTE MAGGIORE del valore
'k' ad esse associato. Le stringhe in W compaiono nello stesso ordine in cui 
compaiono in 'data' (eventuali duplicati vengono mantenuti).

Esempio:
data = [(3, "cat"), (5, "giraffa"), (4, "cat"), (6, "snake"), (5, "zebra")]
# "cat": 3 > 3? no | "giraffa": 7 > 5? si | "cat": 3 > 4? no
# "snake": 5 > 6? no | "zebra": 5 > 5? no
expected = ['giraffa']

Suggerimento:
- data una lista L e una stringa S, il comando L.append(S) aggiunge
  la stringa S in coda alla lista L
'''
def func2(data: list[tuple[int, str]]) -> list[str]:
    pass

# data = [(3, "cat"), (5, "giraffa"), (4, "cat"), (6, "snake"), (5, "zebra")]
# print(func2(data)) # ['giraffa']


################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''
func3: 16 punti

Scrivere una funzione func3(points) che prende in ingresso una lista di tuple
che rappresentano delle coordinate (x, y) di N punti nel piano cartesiano (N >= 3).
Ogni punto è una coppia di numeri interi o float.

La funzione deve calcolare:
   - Mx: la media aritmetica delle coordinate X degli N punti.
   - My: la mediana delle coordinate Y degli N punti (la mediana è
     il valore centrale delle coordinate Y degli N punti ordinate in
     modo crescente o decrescente; se N è pari, è la media aritmetica
     dei due valori centrali).

La funzione restituisce una tupla (Mx, My) dove entrambi i valori sono
riportati con una precisione di 2 cifre decimali (usando la funzione round).

Esempio:
points = [(10, 5), (2, 8), (2, 4), (5, 12), (1, 6)]
# Mx = (10 + 2 + 2 + 5 + 1) / 5 = 4.0
# Valori Y = [5, 8, 4, 12, 6] -> ordinati [4, 5, 6, 8, 12] -> Mediana Y = 6.0
expected = (4.0, 6.0)
'''
def func3(points: list[tuple[float, float]]) -> tuple[float, float]:
    pass

# points = [(10, 5), (2, 8), (2, 4), (5, 12), (1, 6)]
# print(func3(points)) # (4.0, 6.0)
