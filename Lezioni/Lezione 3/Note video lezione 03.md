# Lezione 3 (02/10/2026): cosa dice il prof nel video

Video: https://www.youtube.com/watch?v=Sj84eadhyqE (2h37). Note ricavate dai sottotitoli automatici, confrontate con `Lezione 03 slides.pdf` (in copertina c'è scritto "Lezione 2": il prof spiega che i file prendono il nome dal notebook, non dal numero della lezione). I minuti tra parentesi ti permettono di andare al punto giusto del video.

## Argomenti nell'ordine in cui li fa

1. I notebook `.ipynb` su Classroom: si aprono con VS Code (consigliato), dentro sono JSON. Le celle di codice si eseguono col tasto play (0'-9').
2. Esercizi della lezione precedente svolti dal vivo in VS Code: somma e prodotto (es. 1), parola ripetuta e `len` (es. 3), conversione ed espressione (es. 4) (10'-50').
3. `=` è **assegnazione**, non uguaglianza: prima si **valuta** la destra, poi si **assegna** a sinistra. Per questo `contatore = contatore + 1` ha senso (26'-31').
4. Operatori compatti `+=`, `-=`, `*=`, `/=` (`a *= b` equivale a `a = a * b`) (31'-34').
5. Funzioni annidate come composizione matematica `g(f(x))`: si esegue prima la più interna (22'-26').
6. Espressione "mostro" da risolvere a mano scomponendo: parentesi, poi `**`, poi `*` e `/` da sinistra a destra, poi `+`. `(-1+6)/5**2*10+(10*10)**0.5+1+3` = 16.0 (51'-59').
7. Escape `\n`, `\t`, `\\`, `\'` e stringhe su più righe con le triple virgolette (60'-63').
8. **Modello della memoria** (63'-81'): tabella dei nomi → riferimento → valore in memoria. `a = 12` e poi `a = "Paperino"` crea un nuovo oggetto e sposta il riferimento. Python è a tipizzazione dinamica: la stessa variabile può contenere tipi diversi.
9. `id()`, `a = b` (le due variabili puntano **allo stesso oggetto**), operatore `is` vs `==` (82'-103').
10. Nomi di variabili: lettere, cifre (non all'inizio) e `_`; nomi "parlanti" (`nome_personaggio`, `nomePersonaggio`) invece di `a` (103'-112').
11. **Slicing** completo `[start:end:step]` con tutti i casi particolari e gli indici negativi (113'-149').
12. Quiz finali delle slide: `"ippopotamo"[2:-2:2]` e `"BaBbuino".lower()[-1:-10:-3]`, e il metodo `.lower()` (149'-157').

## Cose dette a voce che non stanno nelle slide

- **All'esame si usa Spyder**; a lezione lui usa VS Code. Conviene conoscerli entrambi (59').
- **All'esame il computer non è collegato a internet, ma Python c'è.** Il prof lo dice chiaramente: se non ti ricordi come si fa qualcosa (es. rovesciare una stringa), **fai delle prove nell'interprete** prima di scriverlo nel programma (147'-149').
- Su Mac/Linux si avvia con `python3`, su Windows con `python`.
- "La CPU è stupida": Python non capisce il significato dei nomi. Chiamare una variabile `numero` non la rende un numero; potresti chiamarla `gismo` (43'-45').
- Nell'esercizio 4 (stringa → int e float): se l'utente scrive `1.5`, `int("1.5")` dà `ValueError` perché una stringa con il punto non si converte in intero. Per ora va bene così (48'-50').
- **Regola pratica sullo slicing** (122'-130'): `s[:n]` dà i **primi n** caratteri, `s[-n:]` gli **ultimi n**. Funziona proprio perché si conta da 0 e `end` è escluso.
- `s[2:10]` su una stringa di 8 caratteri **non dà errore**: si ferma alla fine. Invece `s[10]` (un singolo indice fuori range) dà `IndexError`.
- **Con step negativo, se ometti start si parte dalla fine**: `s[::-1]` rovescia la stringa. "Lo dovete sapere, non è solo ragionamento" (146'-149').
- La differenza tra `is` e `==` "servirà quando faremo le funzioni nostre": il passaggio dei parametri dipende da questo modello della memoria (96').
- I metodi come `.lower()` sono "funzioni di classe": la sintassi è `oggetto.metodo()`. La programmazione a oggetti forse verrà accennata alla fine del corso (153'-156').

## Errori o imprecisioni del prof (verificati in Python)

- **`"Paperino"[2:7:2]`** (136'): a voce dice che prende "P, R, L" saltando le E. Il risultato vero è **`'prn'`** (indici 2, 4, 6 = p, r, n).
- **"Python riusa sempre un valore se esiste già"** (94'-96'): con `a = 10; b = 10` vale `a is b`, ma è un'ottimizzazione di CPython (cache dei piccoli interi e di alcune stringhe), **non una regola del linguaggio**. Con `x = int("1000"); y = int("1000")` viene `x is y` → **False** ma `x == y` → True. Morale per l'esame: **per confrontare valori usa sempre `==`**, `is` solo per sapere se è lo stesso oggetto (o con `None`).
- **"Non riesco a costruire un esempio dove `==` è True e `is` è False"**: poi lo trova con l'aiuto di uno studente: `10.0 == 10` è True, `10.0 is 10` è False. Altri esempi sono qui sopra (gli interi grandi) e arriveranno con le liste (`[1] == [1]` True, `[1] is [1]` False).
- **"Python è un linguaggio non tipato"** (71'): impreciso. Python è **tipizzato dinamicamente** (il tipo sta nel valore, non nella variabile) e **fortemente** (`"5" + 5` dà errore, non converte da solo). Quello che il prof vuole dire è che la variabile non ha un tipo fisso.
- **Operatori compatti "solo con + − × ÷ e una sola operazione"** (32'): esistono anche `//=`, `%=`, `**=`, e a destra ci può essere un'espressione intera: `a += b * c` equivale a `a = a + (b * c)`.
- **Nomi di variabili "solo lettere dell'alfabeto, cifre e `_`"**: in Python 3 sono ammesse anche lettere accentate e Unicode (`città = 3` funziona). Restano vietate le parole chiave, gli spazi e i simboli come `-`, `.`, `€`.
- **Escape**: dice che `\\` funziona "come quando avevamo fatto la doppia virgoletta e il doppio apice". Il backslash funziona, il raddoppio no (vedi note della lezione 2).
- **Quiz del babbuino** (157'): a voce si confonde e dice "la A". La risposta giusta è **`'oua'`** (indici -1, -4, -7 di `"babbuino"`).
- `int()` "accetta solo cifre e il meno" (49'): accetta anche `+`, spazi iniziali e finali e `_` tra le cifre (`int(" +5_0 ")` dà 50). Il punto invece no, come dice lui.

## Domande d'esame che puoi farti

- Cosa stampano `"Paperino"[-4::-1]` e `"Paperino"[1:6:2]`?
- Dopo `a = "ciao"; b = a; a = a + "!"`, quanto vale `b`? `a is b` è True o False?
- Scrivi in forma compatta `x = x // 2` e `s = s + "-"`.
