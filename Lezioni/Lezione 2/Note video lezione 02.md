# Lezione 2 (25/09/2026): cosa dice il prof nel video

Video: https://www.youtube.com/watch?v=c_cNy3vChmw (2h30). Note ricavate dai sottotitoli automatici, confrontate con le slide della Lezione 1 e con gli appunti `Lezione 02.pdf`. I minuti tra parentesi ti permettono di andare al punto giusto del video.

## Argomenti nell'ordine in cui li fa

1. Programma = sequenza ordinata di istruzioni per la CPU, come le istruzioni IKEA della Billy: se cambi l'ordine cambia il risultato (5').
2. Interi: illimitati, si può usare `_` per leggibilità (`1_000_000`). Operatori `*`, `//`, `%`, `**`. `10**1000` non è 10.000 (9').
3. Float: rappresentazione IEEE 754 (segno, esponente, mantissa). Il prof dice esplicitamente che **i dettagli non servono quest'anno**: basta sapere che gli int sono illimitati e i float no (~16 cifre) (11'-14').
4. `type()`, e perché si chiama `float` (floating point = virgola mobile) (15'-17').
5. Precedenza degli operatori: `3 + 14 * 5 / 4` = 20.5. `*` e `/` hanno la stessa priorità e vanno **da sinistra a destra**: scambiarli cambia il risultato. In Python si usano **solo parentesi tonde**, perché quadre e graffe hanno un altro significato (17'-23').
6. `bool`: `bool(0)`, `bool(0.0)` sono False, ogni altro numero è True. `True`/`False` vanno scritti con la maiuscola, altrimenti errore (23'-28').
7. Stringhe: indici da 0 e indici negativi da -1 (30'-50').
8. **Sintassi vs semantica** (34'-44'): la sintassi è *come si scrive*, la semantica è *cosa significa*. Lo userà per ogni nuova istruzione. Esempio: `a = "Paperino"` → sintassi: nome, `=`, valore; semantica: "metti nella scatola chiamata `a` la stringa".
9. `ord` / `chr` e la tabella dei codici (50'-62'). Servono a capire perché si possono ordinare le parole (sono sequenze di numeri).
10. Concatenazione `+` e ripetizione `*` tra stringhe (73').
11. Apici e virgolette, e come mettere un apostrofo dentro una stringa (75'-90').
12. Come eseguire un programma: editor → salva `.py` → terminale → `cd` nella cartella → `python nome.py` (su Mac/Linux `python3`) (90'-110').
13. `input()` e `print()`, virgola vs `+` nel print (111'-124').
14. Esercizi 1-5 delle slide (p.74-78), conversioni `int(input(...))` (124'-149').

## Cose dette a voce che non stanno nelle slide

- **Ambiente consigliato**: Anaconda; come editor VS Code, PyCharm o Spyder. Spyder è quello consigliato (ed è quello usato all'esame, vedi lezione 3). Dal telefono o tablet si può provare Python su PythonAnywhere (account gratuito). Replit non lo consiglia più.
- **Su Windows non usare il Blocco note** per scrivere codice: meglio Notepad++ o un IDE.
- **Mostrare le estensioni dei file** su Windows (Esplora risorse → Visualizza → Mostra → Estensioni nomi file), così vedi il `.py`.
- **Formato degli esercizi d'esame**: "sono sempre in forma di problema", la soluzione è sempre un programma che fa esattamente quello che chiede il testo. Ci sarà una consegna automatica dei file.
- "Imparare a salvare ed eseguire non basta: per l'esame bisogna sapere *cosa* scrivere nel programma."
- **`input()` restituisce sempre una stringa**, qualunque cosa scriva l'utente: Python non legge il messaggio "inserisci un numero" e non controlla niente (137'-143').
- Funzioni annidate: `int(float(int(str(int(input())))))` con input `100` dà un `int` (conta solo l'ultima conversione); con input `ciao` dà errore alla prima `int` (143'-149').
- **La virgola nel `print` non è un operatore tra stringhe** (117'-124'): `print(t1, t2)` stampa con uno spazio in mezzo, ma `t3 = t1, t2` **non** crea una stringa, crea una tupla `('ciao', 'a tutti')`. Per unire stringhe si usa `+` (e lo spazio va messo a mano: `t1 + " " + t2`).
- Il nome del secondo docente è **Daniele De Sensi** (negli appunti Kiwi è trascritto male come "Daniele Altenzi"); il laboratorio del mercoledì lo fa lui.

## Errori o imprecisioni del prof (verificati in Python)

- **"Non potete chiamare una variabile `ord` o `type`"** (52'): non è vero. `ord = "x"` funziona, ma **nasconde** la funzione `ord` per il resto del programma (dopo `ord("a")` dà errore). Sono vietate solo le **parole chiave** (`if`, `for`, `True`, `None`, `def`...). Usare nomi di funzioni come variabili resta una pessima idea.
- **Raddoppiare l'apice per scriverlo dentro la stringa** (84'-89'): il prof prova `'L''ombrello'`, poi ammette che non funziona. In Python due stringhe vicine vengono solo attaccate: `'L''ombrello'` dà `Lombrello`, senza apostrofo. I modi giusti sono: delimitare con l'altro tipo di virgolette (`"L'ombrello"`), usare il backslash (`'L\'ombrello'`) o le triple virgolette.
- **"Nella tabella ASCII la sterlina è 163"** (61'): l'ASCII arriva solo a 127. `ord('£') == 163` è il codice **Unicode**. Python usa Unicode (lo dice lui stesso poco prima: "in realtà è Unicode").
- **`chr` con numeri negativi** ("credo positivo, non c'ho mai provato"): `chr(-1)` dà `ValueError`; il massimo è `chr(1114111)`.
- **Mantissa dell'esempio -6,75** (12'): dice "1,685", il valore giusto è 1,6875 (1.1011 in binario). Il risultato −4 × 1,6875 = −6,75 è corretto.
- **"Il print visualizza una tupla"** (123'): impreciso. `print(a, b)` riceve **due argomenti** e li separa con uno spazio (il separatore si può cambiare con `sep=`). La tupla c'è solo quando scrivi `t3 = a, b` fuori dal print. Inoltre una tupla non richiede elementi "di tipo diverso".

## Domande d'esame che puoi farti

- Cosa stampa `3 + 14 / 5 * 4`? (14.2: prima `14/5`, poi `*4`.)
- Che tipo ha `x` dopo `x = "5", "7"`? E dopo `x = "5" + "7"`?
- Cosa succede con `int(input())` se l'utente scrive `3.14`?
