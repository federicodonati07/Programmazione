# Ignorare le righe fino alla 44 (servono per eseguire i test)
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


# Stampa il risultato di un test (senza controllarlo)
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERRORE: {func_str}({args_str}) => {error_str}')


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


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    # Soluzione non elegante
    sum = 0
    for element in elements:
        sum += element * element
    return sum
    # Soluzione elegante
    # return sum(element * element for element in elements)


# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    max_ = float('-inf')
    for element in elements:
        if element >= max_:
            max_ = element
    return max_


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    result = []
    for element in elements:
        if element not in result:
            result += [element]
    return result


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    # Implementazione lenta
    reversed = []
    for element in elements:
        reversed = [element] + reversed
    return reversed


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e ritorna una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    flattened = []
    for element in elements:
        if isinstance(element, list):
            flattened += flatten_list(element)
            # flattened.extend(element)
        else:
            flattened += [element]
            # flattened.append(element)
    return flattened


# Scrivere una funzione che data una tupla (x, y, z)
# restituisca la tupla (z+1, x-1, y+2)
def tuple_ex(t: tuple) -> tuple:
    return (t[2]+1, t[0]-1, t[1]+2)


# Scrivere una funzione che calcola l'intersezione fra due liste.
# Date due liste, deve restituire una nuova lista contenente solo gli
# elementi presenti in entrambe le liste.
def intersect(a: list, b: list) -> list:
    r = []
    for i in a:
        if i in b:
            r += [i]
    return r


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
    r = []
    partial_sum = 0
    for i in range(0, len(a)):
        if i > 0:
            avg = partial_sum / i
            if a[i] > 2*avg:
                r += [a[i]]             
        partial_sum += a[i]
    return r


# Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una
# funzione che restituisca una lista di tuple (x, y),
# dove x è un intero, e y è il numero di volte che questo
# intero appare nella lista originale.
# La lista di tuple deve essere ordinata in base al primo elemento.
# Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)]
# (ordinata in base al primo elemento perché 1 < 4 < 5)
def frequency(a: list) -> list:
    v = [0] * 100
    for x in a:
        v[x] += 1
    r = []
    for i in range(0, len(v)):
        if v[i]:
            r += [(i, v[i])]
    return r


# Scrivere una funzione che restituisce True
# se la lista è palindroma, o False altrimenti
def is_palindrome(a: list) -> bool:
    for i in range(0, len(a) // 2):
        if a[i] != a[len(a) - 1 - i]:
            return False
    return True


# Scrivere una funzione che prende in input una lista, e 
# restituisce True se la lista è ordinata in ordine
# crescente o decrescente, e False altrimenti.
# Suggerimento: fare attenzione ai valori duplicati
# Utilizzare un solo ciclo e non utilizzare sorted/sort.
def is_sorted(a: list) -> bool:
    if len(a) == 1:
        return True
    dir = 'S' # 'S' = Sconosciuta, 'C' = Crescente, 'D' = Decrescente
    for i in range(1, len(a)):
        if (a[i] > a[i-1]):
            if dir == 'D':
                return False
            dir = 'C'
        if (a[i] < a[i-1]):
            if dir == 'C':
                return False
            dir = 'D'                
    return True


# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
def is_sorted_half(a: list) -> bool:
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
check_test(sum_squares, 14, [1, 2, 3])
check_test(max_element, 3, [1, 2, 3, -1, -2])
check_test(max_element, -1, [-1, -2])
print_test(max_element, [])
check_test(remove_duplicates, [1, 2, 3], [1, 2, 3, 2, 3])
check_test(reverse_list, [3, 2, 1], [1, 2, 3])
check_test(flatten_list, [1, 2, 3], [1, [2, 3]])
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
