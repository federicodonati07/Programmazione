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

nome = "Federico"
cognome = "Donati"
matricola = "2306212"

################################################################################
################################################################################
################################################################################


################################################################################
# %% ----------------------------------- FUNC.1 ------------------------------ #
################################################################################
'''func1: 4 punti

Si definisca la funzione func1(a_dict, char) che prende in ingresso un
dizionario 'a_dict' e un carattere 'char'. Ogni chiave del dizionario e'
una stringa che ha una lista di stringhe come valore.
La funzione deve rimuovere da CIASCUNA lista tutte le stringhe che
contengono il carattere 'char' ALMENO DUE volte, senza distinguere tra
maiuscole e minuscole (es. con char = 'a', la stringa 'Anna' contiene
'a' due volte).
Se, dopo la rimozione, una lista resta VUOTA, la sua chiave deve essere
ELIMINATA dal dizionario.
La funzione restituisce il numero TOTALE di stringhe rimosse.
Il dizionario 'a_dict' viene modificato.

Esempio:
a_dict = {'x': ['banana', 'Anna', 'kiwi'], 'y': ['casa', 'alba']}
char = 'a'
a_dict_exp = {'x': ['kiwi']}
expected = 4
'''
def func1(a_dict: dict[str, list[str]], char: str) -> int:
    char = char.lower()
    removed = 0
    
    for key in a_dict:
        for element in range(len(a_dict[key])):
            a_dict[key][element] = a_dict[key][element].lower()
    
    for key in a_dict:
        for i in range(len(a_dict[key])):
            counter_char = 0
            
            for character in a_dict[key][i]:
                if character == char:
                    counter_char += 1
                    
                    
            if(counter_char >= 2):
                a_dict[key][i] = 0
                removed += 1
                
                
    ndict = {}
    
    for key in a_dict:
        controlList = []
        control = 0
        
        for i in range(len(a_dict[key])):
            
            if a_dict[key][i] != 0:
                controlList.append(a_dict[key][i])
                control+=1
            
            
        if control != 0:
            ndict[key] = controlList
    
    
    a_dict.clear()
    a_dict.update(ndict)
    
    return removed
                    
                


# a_dict = {'x': ['banana', 'Anna', 'kiwi'], 'y': ['casa', 'alba']}
# print(func1(a_dict, 'a'))   # 4
# print(a_dict)               # {'x': ['kiwi']}

################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 4 punti
Un dizionario D e' fornito come input insieme a un intero 'soglia'.
Le chiavi di D sono stringhe (nomi) mentre i valori sono liste di interi
(punteggi, anche negativi; una lista puo' essere vuota).

Scrivi la funzione func2(D, soglia) che costruisce e ritorna la lista
dei nomi la cui SOMMA dei punteggi e' STRETTAMENTE MAGGIORE di 'soglia'.

La lista risultante deve essere ordinata per somma DECRESCENTE.
In caso di parita' di somma, l'ordinamento e' ALFABETICO CRESCENTE.

Esempio:
D = {'anna': [7, 8, 9], 'bruno': [10, 10], 'carla': [5, 5, 5, 5], 'dario': [3]}
soglia = 19
expected = ['anna', 'bruno', 'carla']
'''
def func2(D: dict[str, list[int]], soglia: int) -> list[str]:
    validi = []
   
    if not D:
        return []
    
    for key in D:
        tot = 0
        for i in range(len(D[key])):
            tot += D[key][i]
            
        if(tot > soglia):
                validi.append((key, tot))
            
    validi.sort(key=lambda x: (x[0]))
    validi.sort(key=lambda x: (x[1]), reverse=True)
    
    return [nome for nome, tot in validi]

    
    

# D = {'anna': [7, 8, 9], 'bruno': [10, 10], 'carla': [5, 5, 5, 5], 'dario': [3]}
# print(func2(D, 19))   # ['anna', 'bruno', 'carla']

################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 4 punti
Implementare la func3(strList) che:
- prende in input una lista di stringhe
- per ogni stringa, conta quante CIFRE (caratteri da '0' a '9') contiene
- restituisce la lista dei conteggi ottenuti, SENZA RIPETIZIONI,
  ordinata in modo CRESCENTE.

Esempio:
a_list = ["a1b2", "33", "abc", "9"]
expected = [0, 1, 2]
'''
def func3(strList: list[str]) -> list[int]:
    digit = '0123456789'
    count = []
    
    for i in range(len(strList)):
        counter = 0
        
        for char in strList[i]:
            if char in digit:
                counter+=1
                
        count.append(counter)
        
    
    countUnico = set(count)
    count = [valore for valore in countUnico]
    
    count.sort()
    return count

# a_list = ["a1b2", "33", "abc", "9"]
# print(func3(a_list))   # [0, 1, 2]

################################################################################
# %% ----------------------------------- FUNC.4 ------------------------------ #
################################################################################
'''  func4: 6 punti

Si definisca una funzione func4(string_list1, string_list2) che prende
in ingresso due liste di stringhe e restituisce una nuova lista di
stringhe.
La nuova lista e' costituita dalle stringhe presenti SIA in string_list1
SIA in string_list2 (intersezione tra insiemi): ogni stringa deve
comparire nel risultato UNA SOLA VOLTA.
Il confronto tra le stringhe e' esatto (maiuscole e minuscole contano).

La lista risultante deve essere ordinata per numero di VOCALI
(a, e, i, o, u, case-insensitive, contando anche le ripetute)
DECRESCENTE, in caso di parita', in ordine ALFABETICO CRESCENTE.

Esempio:
    string_list1 = ['mela', 'kiwi', 'banana', 'uva', 'kiwi']
    string_list2 = ['uva', 'kiwi', 'pera', 'banana']
    expected = ['banana', 'kiwi', 'uva']
'''
def func4(string_list1: list[str], string_list2: list[str]) -> list[str]:    
    intersezione = list(set(string_list1) & set(string_list2))
    intersezione = [elemento for elemento in intersezione]
    
    vocali = "aeiouAEIOU"
    congiunta = []
    
    for i in range(len(intersezione)):
        counter = 0
        for char in intersezione[i]:
            if char in vocali:
                counter += 1

        congiunta.append((intersezione[i], counter))
        
    congiunta.sort(key=lambda x: (x[0]))
    congiunta.sort(key=lambda x: (x[1]), reverse=True)

    return [parola for parola, tot in congiunta ]
    
    
    
    
    
# string_list1 = ['mela', 'kiwi', 'banana', 'uva', 'kiwi']
# string_list2 = ['uva', 'kiwi', 'pera', 'banana']
# print(func4(string_list1, string_list2))   # ['banana', 'kiwi', 'uva']

################################################################################
# %% -------------------------------- FUNC.5 --------------------------------- #
################################################################################
'''
func5: 8 punti

Scrivere una funzione func5(points) che prende in ingresso una lista
di coordinate (x, y) di N punti nel piano cartesiano (N >= 3).
Ogni punto e' una coppia di numeri interi.

La funzione deve:
1. Trovare i TRE punti con la coordinata X PIU' PICCOLA. Se ci sono
   piu' punti con la stessa X, a parita' si prendono quelli che
   compaiono PRIMA nella lista in input.
2. Calcolare il BARICENTRO (Gx, Gy) di questi tre punti.
   (Gx e' la media delle 3 coordinate X, Gy e' la media delle 3
    coordinate Y).

La funzione restituisce una tupla (Gx, Gy) dove entrambi i valori
devono essere arrotondati a 2 cifre decimali (si puo' usare la
funzione round).
La lista 'points' NON deve essere modificata.

Esempio:
    points = [(4, 1), (1, 2), (3, 5), (1, 7), (6, 0)]
    expected = (1.67, 4.67)
'''
def func5(points: list[tuple[int, int]]) -> tuple[float, float]:
    ordered_points = [value for value in points]
    ordered_points.sort(key=lambda x: x[0])
    
    
    ordered_points = ordered_points[:3]
    
    x = [i[0] for i in ordered_points]
    y = [i[1] for i in ordered_points]
    
    gx = round((sum(x))/3, 2)
    gy = round((sum(y))/3, 2)
    
    return (gx, gy)
    
    
# points = [(4, 1), (1, 2), (3, 5), (1, 7), (6, 0)]
# print(func5(points))   # (1.67, 4.67)

################################################################################
# #%% ---------------------------- FUNC.6 ------------------------------------ #
################################################################################
'''
Func 6: 4 punti

Si definisca la funzione func6(text) che riceve come argomento:
- text: una stringa formata da parole (solo lettere) separate da uno
  o piu' spazi
e che ritorna un dizionario che ha:
  - come chiavi le LUNGHEZZE delle parole presenti nel testo
  - come valore la LISTA delle parole di quella lunghezza, convertite
    in minuscolo, SENZA RIPETIZIONI e nell'ordine in cui compaiono
    per la prima volta nel testo.

Esempio:
text = 'Il gatto e il cane e il Gatto'
expected = {2: ['il'], 5: ['gatto'], 1: ['e'], 4: ['cane']}
'''
def func6(text: str) -> dict[int, list[str]]:
    if not text:
        return {}
    
    parole_tot = [valore.lower() for valore in text.split() if valore.isalpha()]
    parole_uniche = list(set(parole_tot))
    
    parole_uniche.sort(key=parole_tot.index)
    
    dizionario = {}
    for element in parole_uniche:
        leng = len(element)
        dizionario[leng] = []
        
    for key in dizionario:
        for element in parole_uniche:
            leng = len(element)
            
            if(key == leng):
                dizionario[key].append(element)
                
    return dizionario

# text = 'Il gatto e il cane e il Gatto'
# print(func6(text))   # {2: ['il'], 5: ['gatto'], 1: ['e'], 4: ['cane']}
