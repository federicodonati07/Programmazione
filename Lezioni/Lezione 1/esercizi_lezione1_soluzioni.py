# Soluzioni commentate degli esercizi di fine Lezione 1 (slide p.74-78)
# Per provarle: python esercizi_lezione1_soluzioni.py
# Ogni esercizio è in una funzione, così si possono eseguire uno alla volta.
# In fondo a ciascuno c'è una VARIANTE da risolvere da soli (senza soluzione).


# ---------------------------------------------------------------------------
# Esercizio 1 - Somma e prodotto di due interi, con i loro tipi
# ---------------------------------------------------------------------------
# Ragionamento:
#   1. input() restituisce SEMPRE una stringa: "3" non è 3.
#   2. quindi converto subito con int(...)
#   3. calcolo somma e prodotto e stampo valore e type(...)
# Se dimentichi int(): "3" + "4" == "34" (concatenazione) e "3" * "4" dà errore.
def esercizio1():
    a = int(input("Primo intero: "))
    b = int(input("Secondo intero: "))
    somma = a + b
    prodotto = a * b
    print("Somma:", somma, type(somma))            # int + int -> int
    print("Prodotto:", prodotto, type(prodotto))   # int * int -> int

# VARIANTE 1: chiedi tre numeri con la virgola (float) e stampa la loro media
# e il suo tipo. Poi prova a leggere il terzo numero come int: il tipo della
# media cambia? Perché?


# ---------------------------------------------------------------------------
# Esercizio 2 - Divisione normale, divisione intera e resto
# ---------------------------------------------------------------------------
# Ragionamento:
#   /  produce SEMPRE float, anche se la divisione è esatta (8 / 2 == 4.0)
#   // produce int se entrambi gli operandi sono int (è il quoziente intero)
#   %  è il resto della divisione intera
# Controllo utile: a == (a // b) * b + a % b  deve valere sempre True.
# Attenzione: se il secondo numero è 0 si ottiene ZeroDivisionError.
def esercizio2():
    a = int(input("Primo intero: "))
    b = int(input("Secondo intero: "))
    divisione = a / b
    quoziente = a // b
    resto = a % b
    print("Divisione normale:", divisione, type(divisione))
    print("Divisione intera:", quoziente, type(quoziente))
    print("Resto:", resto, type(resto))
    print("Verifica:", a == quoziente * b + resto)

# VARIANTE 2: chiedi un numero di secondi (es. 3725) e stampa quante ore,
# minuti e secondi sono (3725 -> 1 ora, 2 minuti, 5 secondi) usando solo // e %.
# Poi prova con un numero negativo di secondi: il risultato ti sorprende?


# ---------------------------------------------------------------------------
# Esercizio 3 - Parola ripetuta N volte, lunghezza e tipo
# ---------------------------------------------------------------------------
# Ragionamento:
#   - la parola resta una stringa, N va convertito in int
#   - stringa * intero ripete la stringa (concatenazione ripetuta)
#   - len(...) restituisce il numero di caratteri (un int)
# La slide chiede la lunghezza e il tipo della parola ORIGINALE, non di quella
# ripetuta: la parola è str, la sua lunghezza è int.
def esercizio3():
    parola = input("Parola: ")
    n = int(input("Quante volte? "))
    ripetuta = parola * n
    print("Ripetuta:", ripetuta)
    print("Lunghezza originale:", len(parola))
    print("Tipo della parola:", type(parola))
    # controllo: la lunghezza della ripetuta deve essere len(parola) * n
    print("Lunghezza ripetuta:", len(ripetuta), "=", len(parola), "*", n)

# VARIANTE 3: chiedi una parola e un intero N e stampa la parola ripetuta N
# volte separata da trattini, SENZA trattino finale:
# "ciao", 3 -> "ciao-ciao-ciao". Suggerimento: prova a ragionare su
# quante volte compare "ciao-" e cosa resta da aggiungere.


# ---------------------------------------------------------------------------
# Esercizio 4 - Stringa convertita in int e in float, poi intero + float * 2
# ---------------------------------------------------------------------------
# Ragionamento:
#   - int("7") -> 7   e   float("7") -> 7.0
#   - la precedenza è: prima *, poi +  -> intero + (float * 2)
#   - int + float dà float: basta un float nell'espressione per avere float
# Se l'utente scrive "3.5", int("3.5") dà ValueError: int() su una stringa
# accetta solo cifre intere. Per quel caso serve int(float("3.5")) -> 3.
def esercizio4():
    testo = input("Scrivi un numero intero: ")
    intero = int(testo)
    decimale = float(testo)
    risultato = intero + decimale * 2
    print("Risultato:", risultato, type(risultato))

# VARIANTE 4: chiedi un numero che può avere la virgola (es. "3.7") e stampa
# la sua parte intera come int e la parte dopo la virgola come float
# (3.7 -> 3 e circa 0.7). Stampa anche 0.1 + 0.2: perché non viene 0.3?


# ---------------------------------------------------------------------------
# Esercizio 5 - Stringa convertita in booleano
# ---------------------------------------------------------------------------
# Ragionamento:
#   bool(stringa) guarda SOLO se la stringa è vuota:
#     bool("")      -> False   (unico caso False per le stringhe)
#     bool("ciao")  -> True
#     bool("0")     -> True    (non è il numero 0, è un carattere!)
#     bool("False") -> True    (trappola: il testo "False" non è vuoto)
#     bool(" ")     -> True    (uno spazio è un carattere)
# Per ottenere False da "0" serve prima la conversione a numero: bool(int("0")).
def esercizio5():
    testo = input("Scrivi qualcosa (anche niente, premi solo Invio): ")
    valore = bool(testo)   # False solo se testo == "" (stringa vuota)
    print("Valore booleano:", valore, type(valore))

# VARIANTE 5: senza eseguirli, prevedi il risultato di:
#   bool(0), bool(0.0), bool("0"), bool(int("0")), bool(-1), int(True) + 1
# poi controlla in Python. Quali ti hanno sorpreso?


if __name__ == "__main__":
    esercizio1()
    esercizio2()
    esercizio3()
    esercizio4()
    esercizio5()
