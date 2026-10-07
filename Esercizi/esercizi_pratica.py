# %% Funzioni per i test (eseguire per prima)
from typing import Any, Callable, List
import math
import cmath

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


# %% Esercizio 1: Calcoli - Consumo di carburante
# Un'automobile percorre 15 km con 1 litro di benzina.
# Il costo della benzina è di 1.85 euro al litro.
# Scrivere una funzione che prenda la distanza in km (dist) e calcoli 
# la spesa totale del viaggio in euro, arrotondata o restituita come float.
def costo_viaggio(dist: float) -> float:
    km = 15 
    l = 1
    price_l = 1.85
    
    howmanyl = dist/km
    total_price = howmanyl*price_l
    return total_price
    
    

# %% Esercizio 2: Conversione Orario in Secondi
# Scrivere una funzione che prenda tre interi: ore, minuti e secondi,
# e restituisca il totale dei secondi trascorsi dall'inizio della giornata (00:00:00).
def orario_in_secondi(ore: int, minuti: int, secondi: int) -> int:
    ore_in_s = ore*3600
    minuti_in_s = minuti*60
    
    total = ore_in_s+minuti_in_s+secondi
    
    return total

# %% Esercizio 3: Calcolo dell'Ipotenusa
# Scrivere una funzione che prenda la lunghezza dei due cateti a e b di un
# triangolo rettangolo e restituisca la lunghezza dell'ipotenusa (usa math.sqrt).
import math
def ipotenusa(a: float, b: float) -> float:
    i = math.sqrt(a**2+b**2)
    return i

# %% Esercizio 4: Manipolazione Stringhe - Iniziali Maiuscole
# Scrivere una funzione che prenda nome e cognome come stringhe separati
# e restituisca una stringa nel formato "Cognome, N." dove N è l'iniziale
# del nome seguita da punto, con la prima lettera maiuscola.
# Esempio: formatta_nome("mario", "rossi") -> "Rossi, M."
def formatta_nome(nome: str, cognome: str) -> str:
    start_name = nome[0].upper()
    
    start_surname = cognome[0].upper()
    finish_surname = cognome[1:]
    full_surname = start_surname+finish_surname
    
    return f"{full_surname}, {start_name}."
    
    

# %% Esercizio 5: Stringa orario "HH:MM:SS" -> Secondi
# Avete una stringa di 8 caratteri nel formato "HH:MM:SS" (es. "02:15:30").
# Scrivere una funzione che estragga ore, minuti e secondi e restituisca 
# il tempo totale espresso in secondi.
def str_orario_to_secondi(s: str) -> int:
    clock = s.split(":")
    clock = [int(x) for x in clock]
    
    h_in_s = clock[0]*3600
    m_in_s = clock[1]*60
    
    return h_in_s+m_in_s+clock[2]

# %% Esercizio 6: Condizionale - Numero compreso
# Scrivere una funzione che prenda tre numeri (x, min_val, max_val) e restituisca
# True se x è strettamente compreso tra min_val e max_val (esclusi), altrimenti False.
def is_between(x: float, min_val: float, max_val: float) -> bool:
    if min_val < x < max_val:
        return True
    else:
        return False

# %% Esercizio 7: Condizionale - Anno Bisestile
# Scrivere una funzione che prenda un anno (int) e restituisca True se è bisestile,
# False altrimenti.
# Regola: Un anno è bisestile se è divisibile per 4, eccetto i secolari (divisibili per 100)
# che devono essere divisibili anche per 400.
# Es: 2000 -> True, 1900 -> False, 2024 -> True, 2023 -> False.
def is_leap_year(year: int) -> bool:
    if year%400 == 0:
        return True
    
    if(year%100 == 0 and year%400 != 0):
        return False
    
    if(year%4 == 0 and year%100 != 0):
        return True
    
    if(year%4 != 0):
        return False
    
# %% Esercizio 8: Condizionale - Massimo tra tre numeri
# Scrivere una funzione che prende tre numeri e restituisce il maggiore senza
# usare la funzione predefinita max().
def max_of_three(a: float, b: float, c: float) -> float:
    numbers = [a, b, c]
    
    if(a>b and a>c):
        return a
    
    elif(b>a and b>c):
        return b
    
    else: return c
        

# %% Esercizio 9: Calcolo Voto con Lode
# Scrivere una funzione che prenda un voto numerico (0 - 30) e un booleano (lode).
# Se il voto non è valido (minore di 0 o maggiore di 30), ritorna "NON VALIDO".
# Se la lode è True ma il voto è diverso da 30, ritorna "NON VALIDO".
# Altrimenti restituisce una stringa:
# - "BOCCIATO" se voto < 18
# - "SUPERATO" se 18 <= voto < 30 e lode è False
# - "TRENTA E LODE" se voto == 30 e lode è True
# - "TRENTA" se voto == 30 e lode è False
def valuta_esame(voto: int, lode: bool) -> str:
    if(voto < 0 or  voto > 30):
        return "NON VALIDO"
    
    elif(lode == True and voto != 30):
        return "NON VALIDO"
    
    elif(voto<18):
        return "BOCCIATO"
    
    elif(lode == False and 18<=voto<=30):
        return "SUPERATO"
    
    elif(lode == True and voto == 30):
        return "TRENTA E LODE"
    
    elif(lode == False and voto == 30):
     return "Trenta"
    
    
    
    
    
# %% Esecuzione dei Test
check_test(costo_viaggio, 12.333333333333334, 100)
check_test(orario_in_secondi, 3661, 1, 1, 1)
check_test(orario_in_secondi, 0, 0, 0, 0)
check_test(ipotenusa, 5.0, 3, 4)
check_test(formatta_nome, "Rossi, M.", "mario", "rossi")
check_test(str_orario_to_secondi, 8130, "02:15:30")
check_test(is_between, True, 5, 1, 10)
check_test(is_between, False, 1, 1, 10)
check_test(is_leap_year, True, 2000)
check_test(is_leap_year, False, 1900)
check_test(is_leap_year, True, 2024)
check_test(is_leap_year, False, 2023)
check_test(max_of_three, 15, 5, 15, 10)
check_test(valuta_esame, "NON VALIDO", 32, False)
check_test(valuta_esame, "NON VALIDO", 28, True)
check_test(valuta_esame, "BOCCIATO", 15, False)
check_test(valuta_esame, "SUPERATO", 24, False)
check_test(valuta_esame, "TRENTA E LODE", 30, True)