# Ignorare le righe fino alla 31 (servono per eseguire i test)
from typing import Any, Callable, List
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "superato" if (result == expected) else "fallito"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test di {func_str} con input {args_str} {test_outcome}. Risultato: {result_str} Atteso: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERRORE: {func_str}({args_str}) => {error_str}')


# Scrivere una funzione che data una tupla (x, y, z)
# restituisca la tupla (z+1, x-1, y+2)
def tuple_ex(t: tuple) -> tuple:
    return (t[2]+1, t[0]-1, t[1]+2)


# Scrivere una funzione che calcola l'intersezione fra due liste.
# Date due liste, deve restituire una nuova lista contenente solo gli
# elementi presenti in entrambe le liste.
def intersect(a: list, b: list) -> list:
    # Soluzione che va bene, ma non elegante
    # intersection = []
    # for element in a:
    #     if element in b:
    #         intersection += [element]
    # return intersection

    # Soluzione elegante
    return [element for element in a if element in b]


# Scrivere una funzione che data una lista contenente valori >= 0,
# crei una nuova lista contentente soltanto gli elementi della lista
# originale tali che soddisfano la seguente proprietà:
#    lista[i] > 2*media(lista[0:i])
# (Il primo elemento non viene quindi mai inserito)
# Ad esempio, si consideri la lista [5, 3, 10, 0]
#  Il primo elemento è 5. Non viene inserito
#  Il secondo elemento è 3, e la media degli elementi nel range [0, 0] è 5. Poichè 3 < 5*2, l'elemento non viene inserito nella nuova lista
#  Il terzo elemento è 10, e la media degli elementi nel range [0, 1] è 4. Poichè 10 > 4*2, l'elemento viene inserito nella nuova lista
#  Il quarto elemento è 0, e la media degli elementi nel range [0, 2] è 6. Poichè 0 < 6*2, l'elemento non viene inserito nella nuova lista
def remove_avg(a: list) -> list:
    # Soluzione corretta o ok
    # if len(a) < 2:
    #     return []
    # result = []
    # sum = 0
    # for [i, value] in enumerate(a):
    #     if i > 0 and value > 2 * sum / i:
    #         result += [value]
    #     sum += value
    # return result
    # Soluzione lenta ma elegante
    return [value for i, value in enumerate(a) if i > 0 and value > 2*sum(a[0:i])/i]


# Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una
# funzione che restituisca una lista di tuple (x, y),
# dove x è un intero, e y è il numero di volte che questo
# intero appare nella lista originale.
# La lista di tuple deve essere ordinata in base al primo elemento.
# Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)]
# (ordinata in base al primo elemento perché 1 < 4 < 5)
def frequency(a: list) -> list:
    # Soluzione che va bene
    # counts = []
    # for i in range(100):
    #     counts += [0]
    # for value in a:
    #     counts[value] += 1
    # result = []
    # for value, count in enumerate(counts):
    #     if count > 0:
    #         result += [(value, count)]
    # return result
    # Soluzione elegante
    return sorted(set((value, a.count(value)) for value in a))


# Scrivere una funzione che restituisce True
# se la lista è palindroma, o False altrimenti
def is_palindrome(a: list) -> bool:
    # Soluzione che va bene
    # for index in range(len(a)):
    #     if a[index] != a[-index-1]:
    #         return False
    # return True
    # Soluzione elegante (dai tutors)
    return a == a[::-1]


# Scrivere una funzione che prende in input una lista, e
# restituisce True se la lista è ordinata in ordine
# crescente o decrescente, e False altrimenti.
# Suggerimento: fare attenzione ai valori duplicati
# Utilizzare un solo ciclo e non utilizzare sorted/sort.
def is_sorted(a: list) -> bool:
    # Soluzione corretta
    # decided, increasing = False, False
    # for index in range(1, len(a)):
    #     if decided:
    #         if increasing and a[index-1] > a[index]:
    #             return False
    #         if not increasing and a[index-1] < a[index]:
    #             return False
    #     else:
    #         if a[index-1] != a[index]:
    #             decided = True
    #             increasing = a[index-1] < a[index]
    # return True
    # Soluzione elegante ma che usa cose che non potrei fare e è troppo lenta!
    return a == sorted(a) or a == sorted(a, reverse=True)


# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
def is_sorted_half(a: list) -> bool:
    # Soluzione da guardare a casa
    peak_found = False
    for i in range(1, len(a)-1):
        if (a[i] > a[i-1]) and (a[i] > a[i+1]):
            if peak_found:
                return False
            peak_found = True
        if (a[i] < a[i-1]) and (a[i] < a[i+1]):
            if peak_found:
                return False
            peak_found = True
    return peak_found


# Test funzioni
check_test(tuple_ex, (3, -2, 1), (-1, -1, 2))
check_test(intersect, [2, 3], [1, 2, 3], [2, 3, 4])
check_test(intersect, [], [1, 2, 3], [10, 11, 12])
check_test(intersect, [], [1, 2, 3], [])
check_test(intersect, [], [], [1, 2, 3])
check_test(remove_avg, [10], [5, 3, 10, 0])
check_test(remove_avg, [20, 1000], [5, 20, 10, 1000])
check_test(remove_avg, [], [])
check_test(frequency, [(1, 1), (4, 2), (5, 1)], [5, 4, 1, 4])
check_test(frequency, [(0, 1), (23, 3), (99, 1)], [23, 99, 0, 23, 23])
check_test(is_palindrome, True, [])
check_test(is_palindrome, True, [1])
check_test(is_palindrome, True, [1, 2, 8, 2, 1])
check_test(is_palindrome, True, [1, 2, 8, 8, 2, 1])
check_test(is_palindrome, False, [1, 3, 8, 8, 2, 1])
check_test(is_sorted, True, [1])
check_test(is_sorted, True, [1, 1, 1])
check_test(is_sorted, True, [1, 2, 3, 4])
check_test(is_sorted, True, [4, 3, 2, 1])
check_test(is_sorted, True, [1, 1, 2, 3, 3, 4])
check_test(is_sorted, True, [4, 4, 3, 2, 2, 1])
check_test(is_sorted, False, [1, 1, 3, 3, 2])
check_test(is_sorted, False, [4, 4, 3, 3, 5])
check_test(is_sorted_half, False, [1, 2, 3])
check_test(is_sorted_half, False, [3, 2, 1])
check_test(is_sorted_half, True, [1, 3, 2])
check_test(is_sorted_half, True, [3, 1, 2])
check_test(is_sorted_half, True, [1, 2, 5, 6, 8, 9, 3])
