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
# %% -------------------------------- FUNC.1 --------------------------------- #
################################################################################
'''func1: 8 punti

Implementare la funzione func1(str_list) che:
- prende in input una lista di stringhe 'str_list'
- per ogni stringa, conta il numero di CONSONANTI (lettere minuscole dell'alfabeto
  inglese a-z, escluse le vocali 'a', 'e', 'i', 'o', 'u').
- restituisce una lista contenente i conteggi ottenuti, ordinati in ordine CRESCENTE.

Esempio:
str_list = ["python", "chat", "code", "ai"]
# "python" -> 5, "chat" -> 3, "code" -> 2, "ai" -> 0
expected = [0, 2, 3, 5]

Suggerimenti:
- data una lista L e un numero N, il comando L.append(N) aggiunge
  il numero N in coda alla lista L
- data una lista L e una stringa S, l'espressione booleana S in L
  varrà False se S non è presente in L, True se S è presente in L
'''
def func1(str_list: list[str]) -> list[int]:
    pass

# str_list = ["python", "chat", "code", "ai"]
# print(func1(str_list)) # [0, 2, 3, 5]




################################################################################
# %% ---------------------------- FUNC.2 ------------------------------------ #
################################################################################
'''
func2: 8 punti

Si definisca la funzione func2(text) che riceve come argomento:
- text: una stringa minuscola formata da parole separate da spazi e punteggiatura.

La funzione deve restituire una lista di 5 liste di due elementi
[vocale, frequenza] (liste, NON tuple), una per ciascuna vocale, nell'ordine
'a', 'e', 'i', 'o', 'u' (anche se la vocale non compare nel testo).
Ogni lista contiene:
- la vocale minuscola ('a', 'e', 'i', 'o', 'u')
- la frequenza totale di quella vocale nell'intero testo (0 se assente).

Esempio:
text = "an apple a day keeps the doctor away!"
# 'a': 6, 'e': 4, 'i': 0, 'o': 2, 'u': 0
expected = [['a', 6], ['e', 4], ['i', 0], ['o', 2], ['u', 0]]
'''
def func2(text: str) -> list[list]:
    pass

# text = "an apple a day keeps the doctor away!"
# print(func2(text)) # [['a', 6], ['e', 4], ['i', 0], ['o', 2], ['u', 0]]


################################################################################
# %% ----------------------------------- FUNC.3 ------------------------------ #
################################################################################
''' func3: 16 punti

Si definisca la funzione func3(list1, list2) che prende in ingresso due liste
di stringhe e restituisce una nuova lista di stringhe.
La nuova lista è costituita da tutte le stringhe presenti in list1 ma NON
presenti in list2 (senza duplicati nella lista finale).

La lista risultante deve essere ordinata in ordine ALFABETICO CRESCENTE
(ordinamento standard delle stringhe in Python, cioè quello di sorted()).

Esempio:
list1 = ["a123", "b12", "c12", "test", "a123", "no_digits"]
list2 = ["test", "other"]
expected = ['a123', 'b12', 'c12', 'no_digits']
'''
def func3(list1: list[str], list2: list[str]) -> list[str]:
    pass

# list1 = ["a123", "b12", "c12", "test", "a123", "no_digits"]
# list2 = ["test", "other"]
# print(func3(list1, list2)) # ['a123', 'b12', 'c12', 'no_digits']
