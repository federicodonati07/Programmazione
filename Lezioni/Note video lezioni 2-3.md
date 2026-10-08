# Note dai video delle lezioni 2 e 3

Ricavate dai sottotitoli automatici di YouTube (lezione 2: `c_cNy3vChmw`, lezione 3: `Sj84eadhyqE`), corretti a contesto. Qui c'è solo quello che il prof dice a voce e che non trovi già nelle slide, più gli errori da non imparare.

## Esame e organizzazione

- All'esame avrai **un computer senza internet ma con Python**: puoi provare il codice (es. "come si inverte una stringa?" → fai prove finché funziona).
- Gli esercizi sono **in forma di problema**: la soluzione è sempre un programma che fa *esattamente* quello che il testo chiede. Saper eseguire un file non basta, conta cosa scrivi dentro.
- Le simulazioni danno **punti bonus**; la consegna sarà automatica (i file vengono copiati sul computer dei docenti).
- IDE: a lezione usa VS Code (anche per aprire i `.ipynb`), **all'esame si usa Spyder**: conviene provarli entrambi. Sconsigliato il Blocco note di Windows (codifica). Da smartphone: PythonAnywhere (account gratuito). Replit: "dimenticate quello che vi ho detto".
- I notebook `.ipynb` su Classroom hanno una numerazione diversa dalle lezioni: nella lezione 3 si usa il file "lezione 02". Ecco perché le copertine delle slide sembrano sbagliate.
- Su Linux/Mac il comando è `python3`, su Windows `python`. Un programma si scrive nell'editor, si salva come `.py`, si esegue (`python nome.py` dal terminale, dopo `cd` nella cartella).

## Concetti su cui insiste

- **Sintassi vs semantica**: per ogni costrutto il prof dà "come si scrive" e "cosa significa". Abituati a ragionare così.
- **`=` non è un'uguaglianza**: `variabile = espressione` significa 1) valuta l'espressione a destra, 2) assegna il risultato. Per questo `contatore = contatore + 1` ha senso.
- Ogni dato ha sempre **valore e tipo**. Il nome della variabile non conta per Python (`gismo = input(...)` va benissimo), conta per chi legge: usa nomi "parlanti" (`nome_personaggio`, non `a`).
- **`input()` restituisce sempre una stringa**, qualunque cosa scrivi. Per un intero: `int(input(...))`, che è una composizione di funzioni come g(f(x)): si esegue prima la più interna.
- `int('1.5')` → `ValueError`: `int` accetta solo cifre (e segno). L'esercizio 4 (int + float*2) si rompe se inserisci un decimale.
- **`print(a, b)` mette uno spazio, ma la virgola non è un operatore tra stringhe**: `t3 = t1, t2` crea una *tupla*, non una stringa. Per unire stringhe usa `+` (e lo spazio aggiungilo tu: `t1 + " " + t2`). `"81 // 7 fa " + 81 // 7` → `TypeError` (str + int).
- Precedenze: `3 + 14 * 5 / 4` = 20.5 ma `3 + 14 / 5 * 4` = 14.2 (stessa priorità → da sinistra a destra). In Python esistono solo parentesi tonde nelle espressioni.
- Apici dentro le stringhe: usa l'altro tipo di virgolette o il backslash (`'Paperina e\' un\'abile...'`). **Raddoppiare l'apice non funziona** (lo prova in aula). Tripli apici per testo su più righe (lui non li usa mai).
- **Memoria**: Python tiene una *tabella dei nomi* e ogni nome punta a un oggetto in memoria. Riassegnare sposta il riferimento. `a = b` fa puntare `a` allo stesso oggetto di `b` (non copia). `id(x)` dà l'identificatore dell'oggetto. Servirà per capire il passaggio di parametri alle funzioni.
- **`is` vs `==`**: `is` = stesso oggetto, `==` = stesso valore. Controesempio trovato in aula da uno studente: `10 == 10.0` è `True`, `10 is 10.0` è `False`.
- **Slicing** `s[start:end:step]`, `end` escluso:
  - `s[:n]` → primi n caratteri; `s[-n:]` → ultimi n caratteri (perché si conta da 0 ed `end` è escluso);
  - un `end` oltre la lunghezza non dà errore;
  - con step negativo e `start` omesso si parte dalla fine: `s[::-1]` inverte la stringa; `'Paperino'[-4::-1]` → `'repaP'`.
  - Quiz finale: `'Ippopotamo'[2:-2:2]` → `'ppt'`, `'BaBbUiNo'.lower()[-1:-10:-3]` → `'oua'`. `lower()` è un *metodo* (funzione "di classe"), per questo si scrive dopo il punto.

## Errori e semplificazioni da non imparare

| Cosa dice il prof | Come stanno le cose |
|---|---|
| `a[5]` è "slicing" | è **indicizzazione**; lo slicing è `a[i:j]` (lo dice anche lui nella lezione 3, quando introduce i due punti) |
| non si può chiamare una variabile `ord` o `type` | si può (sono funzioni built-in): la sovrascrivi e poi `ord(...)` non funziona più. Sono vietate solo le 35 **parole chiave** (`if`, `for`, `True`, …) |
| `ord('£')` = 163 "nella tabella ASCII" | ASCII arriva a 127; 163 è il codice **Unicode** |
| `chr` vuole un intero positivo | va da 0 a 1 114 111; `chr(-1)` → `ValueError` |
| Python è "non tipato" | Python è a tipizzazione **dinamica** (e forte): i valori hanno un tipo, le variabili no |
| `a = 10; b = 10` → Python riusa sempre l'oggetto, quindi `a is b` | vale solo per interi piccoli (-5…256) e alcune stringhe. Nel REPL `a = 1000` e `b = 1000` su righe separate → `a is b` è `False`; `'Paperino ' * 4 is 'Paperino ' * 4` → `False` (ma `==` → `True`). Per confrontare valori usa sempre `==` |
| non esiste un caso con `is` vero e `==` falso | esiste: `x = float('nan')` → `x is x` è `True`, `x == x` è `False` |
| operatori compatti solo con + - * / | esistono anche `//=`, `%=`, `**=` |
| nei nomi di variabile solo lettere a-z, cifre (non all'inizio) e `_` | giusto nella pratica, ma Python ammette anche lettere accentate (`è = 3` funziona). Meglio evitarle |
| "espressione monster" = 16 | Python stampa **16.0**: basta una `/` o un `** 0.5` per avere un float |
| (L2, esempio IEEE 754) mantissa "1,685" | è **1,6875** (1.1011 in binario): -1 · 2² · 1,6875 = -6,75 |
