# Il file è diviso in celle: ogni cella inizia con una riga "# %%".
# In Spyder (o VS Code) potete eseguire la cella in cui si trova il cursore
# con Ctrl+Invio, oppure con Maiusc+Invio per eseguirla e passare alla
# successiva. Potete anche eseguire tutto il file, come un normale programma.
# Eseguite per prima la cella "Funzioni per i test".

# %% Funzioni per i test (eseguire per prima)
# Queste funzioni servono per eseguire i test: non è necessario capire come
# funzionano.
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


# %% Errori
# Iniziate a prendere familiarità con i messaggi di errore che Python vi da.
# Provate ad introdurre di proposito degli errori e a vedere quale messaggio
# di errore ottenete. Meglio fare errori ora e di proposito(e capirli),
# piuttosto che accidentalmente in seguito e non riuscire a capire dov'è
# l'errore. Ad esempio:

# Cosa succede se dimenticate gli apici alla fine di una stringa?

# Cosa succede se dividete un numero per `0`?

# Cosa succede se in una istruzione di stampa(print) dimenticate una o
# entrambe le parentesi?

# Per esprimere un numero negativo, si antepone il segno meno (ad esempio, `-2`).
# Cosa succede se anteponete il segno `+?` e se fate `2++2`?

# Nella notazione matematica, gli `0` iniziali sono ammessi (ad esempio, `02`).
# Cosa succede in Python?

# Nella notazione matematica, possiamo omettere il simbolo di moltiplicazione.
# Ad esempio `x*y` può essere scritto come `xy`. E' permesso anche in Python?

# In Python possiamo assegnare un numero ad una variabile, ad esempio: `n = 42`.

# Cosa succede se facciamo `42 = n`?

# Cosa succede con `x = y = 1`?

# In alcuni linguaggi, come il C, ogni istruzione termina con un punto e
# virgola (`;`). Cosa succede se mettiamo un punto e virgola alla fine di
# un'istruzione Python? E se mettiamo un punto?


# %% Calcoli: secondi
# Scrivete una espressione che calcoli il numero di secondi che ci sono in
# 42 minuti e 42 secondi.
m = 42
s = 42

s_in_m = 60 
m_in_s = m*s_in_m

tot = m_in_s+s
print(tot)




# %% Calcoli: miglia
# Scrivete una espressione che calcoli il numero di miglia che ci sono in
# 10 chilometri. (1 miglio=1.61 km).
conversione = 1.61

km = 10
m_in_km = km/conversione
print(m_in_km)



# %% Calcoli: velocità e cadenza
# Scrivete una espressione che calcoli la velocità media e la cadenza media
# (tempo per miglio, in minuti e secondi) di un corridore che corre una gara
# di 10 chilometri in 42 minuti e 42 secondi.
lunghezza = 10
tempoM = 42
tempoS = 42
conversione = 60

tempoInS = (tempoM*conversione)+tempoS

vMedia = lunghezza/tempoInS
print(vMedia*3600)

miglia = lunghezza/1.61

# dv = ds/dt -> dt = ds/dv
tempoPerMiglio = tempoInS / miglia

minutiPerMiglio = int(tempoPerMiglio / 60)
secondiPerMiglio = int(tempoPerMiglio % 60) 

print(minutiPerMiglio, secondiPerMiglio)



# %% Calcoli: volume della sfera
# Il volume di una sfera di raggio `r` è `4/3 * PI * r ^ 3`.
# Scrivere una espressione che calcoli il volume di una sfera di raggio 5.
import math
r = 5

volume = (4*math.pi*r**3)/3
print(volume)


# %% Calcoli: costo dei libri
# Il prezzo di copertina di un libro è 24.95, ma una liberia ottiene il 40%
# di sconto. I costi di spedizione sono 3 euro per la prima copia, e 75
# centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60 copie?

price = 24.95
promo = 40
fcopy = 3
ocopy = 0.75

newPrice = price-(price*promo)/100

copy = 60
tot = 0


for x in range(0, copy):
    if(x == 0):
        tot += newPrice+fcopy

    else:
        tot += newPrice+ocopy
        
print(tot)



# %% Calcoli: orario di rientro
# Se uscite di casa alle 6: 52 di mattina e correte un miglio a ritmo blando
# (8 minuti e 15 secondi al miglio), e poi 3 miglia a ritmo moderato
# (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo blando
# (9 minuti e 45 secondi al miglio), a che ora sarete tornati a casa?

outHour = 6
outMin = 52

pace1 = 8*60+15
manyMpace1 = 1

pace2 = 7*60+12
manyMpace2 = 3

pace3 = 9*60+15
manyMpace3 = 1

totOutInS = (pace1*manyMpace1) + (pace2*manyMpace2) + (pace3*manyMpace3)
totOutInM = int(totOutInS/60)

shiftHour = (outMin+totOutInM)//60
returnH = outHour+shiftHour
returnM = (outMin+totOutInM)%60

print(f"{returnH}:{returnM:02d}")











# %% Radice cubica
# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la
# radice cubica, e la ritorna.

import math
def cubic_root(n):
    if(n >= 0):
        return math.pow(n, 1/3)
    
    else:
        return math.pow(-n, 1/3)

check_test(cubic_root, 2.0, 8)
print_test(cubic_root, -1)


# %% Radici di un'equazione di secondo grado
# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e le ritorna entrambe.

import cmath
def roots(a, b, c):
    delta = b**2-4*a*c
    
    fsqrt = (-b+cmath.sqrt(delta))/2*a
    ssqrt = (-b-cmath.sqrt(delta))/2*a
    
    return fsqrt, ssqrt



print_test(roots, 2, 3, 4)
check_test(roots, (-0.020002000400097586, -199.9799979995999), 1, 200, 4)


# %% Saluto con input
# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome letto come input e poi da `Buona giornata!`
def print_hello():
    name = input()
    return(f"Ciao {name} Buona Giornata!")


print_test(print_hello)


# %% Somma delle cifre
# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale.
# Ad esempio, `s = "85721"`. Stampate la somma delle cifre contenute nella stringa.
def dec_str_to_dec(s):
    s = list(s)
    s = [int(x) for x in s]
    
    somma = 0
    for i in s:
        somma += i
        
    print(somma)
    
    


print("Risultato di dec_str_to_dec: ", end="")
dec_str_to_dec("85721")


# %% Da binario a decimale
# Scrivete una espressione che a partire da una stringa di 5 caratteri,
# rappresentante un numero binario, stampi la sua rappresentazione decimale.
# Ad esempio, `s = "00101" -> 5`.
def bin_str_to_dec(s):
    s = int(s, 2)
    
    print(s)


print("Risultato di bin_str_to_dec: ", end="")
bin_str_to_dec("00101")


# %% Numero con la virgola
# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale
# ('.'). Ad esempio, s = "52.29". Stampare il numero decimale rappresentato
# dalla stringa(stamparlo come numero, non come stringa).
def dec_frac_str_to_dec(s):
    x = float(s)
    print(x)


print("Risultato di dec_frac_str_to_dec: ", end="")
dec_frac_str_to_dec("52.29")


# %% Saluto con parametro
# Scrivere una funzione che restituisce una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    return(f"Ciao {name}. Buona giornata!")


check_test(make_hello, 'Ciao Pippo. Buona giornata!', 'Pippo')
