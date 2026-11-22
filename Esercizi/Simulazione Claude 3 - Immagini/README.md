# Simulazione Claude 3: immagini

Simulazione dell'esonero sulle immagini, nello stesso formato di quella del corso
(`program.py` + `grade.py` + `testlib.py` + `images.py`/`png.py`), 4 funzioni, 30 punti, si passa con 18.

| Funzione | Punti | Argomento |
|---|---|---|
| func1 | 6 | contare pixel chiari e scuri (luminosità media) |
| func2 | 7 | creare l'immagine specchiata in orizzontale |
| func3 | 9 | **file di istruzioni**: leggere un file di testo e disegnare punti, segmenti e rettangoli |
| func4 | 8 | **file di istruzioni**: un "pennello" che si muove sull'immagine seguendo dei comandi |

Usa solo quello che si è fatto a lezione: `images.load`/`images.save`, liste di liste,
cicli `for`, lettura di file con `open`/`split`/`int`, dizionari.

## Come si usa

1. Apri `program.py`, scrivi nome, cognome e matricola.
2. Sostituisci i `pass` con il tuo codice (è l'unico file da modificare).
3. Dalla cartella della simulazione lancia:

```
python grade.py              # tutti i test
python grade.py func3        # solo i test di func3 (puoi metterne più di una)
python grade.py --debug      # con lo stack trace completo degli errori
```

Le immagini prodotte dalla tua funzione vengono salvate accanto a quelle attese
(es. `func2/img2_out.png` e `func2/img2_exp.png`): aprile per confrontarle.

## Come leggere l'output di grade.py

- **verde** ✔: test superato, con i punti presi.
- **rosso** ✘: test sbagliato. Sotto trovi cosa era atteso e cosa hai restituito.
  Per le immagini vedi quanti pixel sono diversi, le coordinate `(x, y)` dei primi,
  il colore atteso e quello ottenuto, e una piccola mappa con `X` sui pixel sbagliati.
  Se c'è un'eccezione vedi la riga di `program.py` dove è successa.
- **giallo** ⚠: avvisi e suggerimenti (funzione non implementata, tipo sbagliato,
  larghezza e altezza scambiate, ...).
- Alla fine c'è il **riepilogo** con i punti di ogni funzione e il totale.

I colori si spengono da soli se l'output non è un terminale. Per spegnerli o forzarli:
`NO_COLOR=1 python grade.py` oppure `FORCE_COLOR=1 python grade.py`
(su Windows PowerShell: `$env:NO_COLOR=1; python grade.py`).

La cartella `backup/` contiene una copia dei file di input e di quelli attesi: se il tuo
codice ne sovrascrive uno per sbaglio, `grade.py` te lo dice e puoi ricopiarlo da lì.
