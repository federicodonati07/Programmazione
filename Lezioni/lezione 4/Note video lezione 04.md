# Lezione 4 (07/10/2026): cosa dice il prof nel video

Video: https://www.youtube.com/watch?v=dOyKLa2Lq5s (1h35). Note ricavate dai sottotitoli e da `trascrizione.txt`, confrontate con `lezione 04 slides.pdf` (in copertina "Lezione 3") e con `Riassunto Lezione 4.pdf`.

## Argomenti

- Apertura (0'-5'): il notebook viene convertito in slide con `jupyter nbconvert --to slides` e poi stampato in PDF. Il mercoledì il laboratorio con De Sensi viene **prima** della teoria, quindi i condizionali li avete già provati in lab.
- Istruzioni condizionali `if` / `elif` / `else`, sintassi (la parola chiave, la condizione, i due punti, l'indentazione) e semantica.
- Esercizio dei voti 0-10 scritto in quattro versioni: `if` in sequenza, `if` annidati, `elif`, `match/case`.
- Indentazione: esempio temperatura/pioggia (64'), esercizio "rischio cardiovascolare" con `if` annidati.
- Chiusura (89'-95'): introduzione ai cicli. Esempio "leggi un milione di interi e conta i pari": senza cicli servirebbero un milione di `if`. I cicli si fanno venerdì, poi arriveranno le funzioni.

## Cose dette a voce che non stanno nelle slide

- **Errore tipico**: `v = input(...)` senza `int()` e poi `v < 6` → `TypeError` (confronto tra `str` e `int`).
- Il prof preferisce `elif` a `match` ("personalmente uso if"). `match` garantisce un solo esito ed evita alcuni errori, ma per lui è una scelta di stile.
- **Il compito per casa**: capire bene la differenza tra una sequenza di `if` indipendenti (vengono controllati tutti) e una catena `if`/`elif`/`else` (se ne esegue al massimo uno) (57').
- **Esame** (84'-85'): "sono tutte funzioni", vengono testate con molti input, "anche belli contorti ma che rispettano l'esercizio". Lo stile non conta: conta che l'output sia giusto in ogni caso.
- Ci sono tutor (studenti di 2° e 3° anno) su Classroom, dove trovi anche i notebook.

## Errori o imprecisioni

- **Il prof dice che si possono mescolare spazi e tab**: in Python 3 un'indentazione incoerente tra tab e spazi dà `TabError`. Usa sempre 4 spazi.
- **"7 e mezzo → sufficiente"**: con `int(input())`, se l'utente scrive `7.5` viene `ValueError`. Il programma accetta solo interi.
- Slide 25: il commento dice 1..9, ma `range(-12, -30, -3)` produce -12, -15, ..., -27.
- Slide 27: il commento dice "arrivo a 12", ma il codice ha `X == 22` con `while X < 20`: il `break` non scatta mai e viene eseguito l'`else` del ciclo.
- Slide 3-4: `A //= 5` è chiamato "diviso", ma è la divisione **intera**.
- `Riassunto Lezione 4.pdf`: nella versione con `elif` l'`else` finale stampa "Eccellente" anche per 11 (manca il controllo `v <= 10`). Inoltre suggerisce di provare `7.999` con un input letto come intero, che dà errore.
- `lezione-py.py`: il `match` non ha `case _`, quindi un voto fuori da 0-10 non stampa niente.
