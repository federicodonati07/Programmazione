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


# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e ritorna la maggiore.
# Se le radici sono complesse, la funzione restituisce una qualsiasi
# delle due radici
import math
import cmath
def root_max(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    delta = b**2-4*a*c
    
    if(delta < 0):
        return (-b+cmath.sqrt(delta))/(2*a)
    else:
        sqrt1 = (-b + math.sqrt(delta)) / (2 * a)
        sqrt2 = (-b - math.sqrt(delta)) / (2 * a)
        
        return(max(sqrt1, sqrt2))
    

# Scrivere una funzione che prende come input cinque numeri e ritorna la somma
# dei numeri pari meno quella dei numeri dispari.
def even_minus_odd(a, b, c, d, e):
    all = [a, b, c, d, e]
    
    pari = []
    dispari = []
    
    for x in range(len(all)):
        if all[x] % 2 == 0:
            pari.append(all[x])
            
        if all[x] % 2 != 0:
            dispari.append(all[x])
            
    sum_pari = 0
    sum_dispari = 0
    
    for paro in pari:
        sum_pari += paro
        
    for disparo in dispari:
        sum_dispari += disparo
        
    total = sum_pari - sum_dispari
    return total


# Scrivere una funzione che prende tre valori di input, e ritorna la
# loro somma se i valori sono punteggi di esame validi(`0 <= grade <= 30`),
# e altrimenti ritorna `- 1`. Scriverne poi una variante che legge i valori da
# terminale con `input`.
def check_grade(a, b, c):
    grades = [a, b, c]
    # Verifica che tutti i voti siano compresi tra 0 e 30
    if all(0 <= g <= 30 for g in grades):
        return sum(grades)
    return -1
            
            


# Scrivere una funzione che prende tre valori(`d`, `m`, `y`) e ritorna se la
# data è valida o no. Si possono ignorare gli anni bisestili. Ad esempio,
# ritorna `False` per `30/2/2017` e `True` per `1/1/1111`.
def check_date(d, m, y):
    if y <= 0 or not(1<=m<=12):
        return False
    
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return 1 <= d <= days_in_months[m]
            
        
        
            
    


# Test funzioni
print_test(root_max, 2, 3, 4)
check_test(root_max, -0.020002000400097586, 1, 200, 4)
check_test(even_minus_odd, 8, 2, 4, 1, 3, 6)
check_test(even_minus_odd, 10, 2, 2, 2, 2, 2)
check_test(even_minus_odd, -5, 1, 1, 1, 1, 1)
check_test(check_grade, 41, 21, 18, 2)
check_test(check_grade, -1, 21, 32, 2)
check_test(check_grade, -1, 21, 18, -2)
check_test(check_date, False, -1, 12, 2011)
check_test(check_date, False, 1, 14, 2011)
check_test(check_date, False, 1, 12, -1)
check_test(check_date, False, 31, 4, 2011)
check_test(check_date, True, 30, 4, 2011)
