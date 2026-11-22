#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE    ####################

PRIMA DI TUTTO:
    Assegna le seguenti variabili con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio, esegui il file grade.py contenuto nella cartella:

    python grade.py              -> tutti i test
    python grade.py func3        -> solo i test di func3
    python grade.py --debug      -> con lo stack trace completo degli errori

Per superare la simulazione è sufficiente ottenere un punteggio >= 18 (su 30).

Ricorda: un'immagine è una LISTA DI RIGHE. img[y][x] è il pixel nella
riga y (dall'alto) e nella colonna x (da sinistra).
    altezza   H = len(img)
    larghezza W = len(img[0])
"""

nome      = "NOME"
cognome   = "COGNOME"
matricola = "MATRICOLA"

# NOTA: NON importate altre librerie oltre a images

import images

################################################################################
################################################################################

# %% ----------------------------------- FUNC1 ------------------------- #
""" func1: 6 punti

Definisci una funzione func1(img_in, soglia) che prende in input
    - img_in: il percorso di un file con un'immagine PNG
    - soglia: un numero intero tra 0 e 255

La luminosità di un pixel (R, G, B) è la media aritmetica dei suoi tre
canali, cioè (R + G + B) / 3, SENZA arrotondare.
Un pixel è "chiaro" se la sua luminosità è strettamente maggiore di soglia,
altrimenti è "scuro".

La funzione deve restituire una TUPLA (chiari, scuri) con il numero di
pixel chiari e il numero di pixel scuri dell'immagine.

Esempio: in un'immagine con i 3 pixel (100, 100, 101), (90, 90, 90) e
(255, 0, 0), con soglia = 100 la funzione restituisce (1, 2):
    (100+100+101)/3 = 100.33 > 100   -> chiaro
    (90+90+90)/3    = 90             -> scuro
    (255+0+0)/3     = 85             -> scuro

Per leggere l'immagine usa la funzione load del modulo images.
"""

def func1(img_in, soglia):
    pass
    # inserisci qui il tuo codice


# print(func1('func1/img1_in.png', 128))


# %% ----------------------------------- FUNC2 ------------------------- #
""" func2: 7 punti

Definisci una funzione func2(img_in, img_out) che prende in input
    - img_in:  il percorso di un file con un'immagine PNG
    - img_out: il percorso del file PNG da creare

La funzione deve creare l'immagine SPECCHIATA in orizzontale (come in uno
specchio messo di lato): la prima colonna diventa l'ultima, la seconda
diventa la penultima, e così via. Le righe restano nello stesso ordine.
L'immagine ottenuta va salvata nel file img_out.

La funzione deve restituire il numero di pixel che hanno lo STESSO colore
nell'immagine originale e in quella specchiata (cioè i pixel (x, y) tali che
il colore in (x, y) prima e dopo lo specchio è uguale).

Esempio (ogni lettera è un colore), immagine 4x2:
    A B C D            D C B A
    E F F E    --->    E F F E
I pixel che non cambiano sono i 4 della seconda riga: la funzione restituisce 4.

ATTENZIONE: per costruire l'immagine specchiata devi leggere i colori
dell'immagine ORIGINALE.

Per leggere/salvare le immagini usa le funzioni load/save del modulo images.
"""

def func2(img_in, img_out):
    pass
    # inserisci qui il tuo codice


# print(func2('func2/img2_in.png', 'func2/img2_out.png'))


# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 9 punti     (FILE DI ISTRUZIONI)

Definisci una funzione func3(file_disegno, img_out) che prende in input
    - file_disegno: il percorso di un file di testo con le istruzioni di disegno
    - img_out:      il percorso del file PNG da creare

Il file contiene una istruzione per riga; le parti di ogni istruzione sono
separate da uno o più spazi. Le righe vuote e le righe che iniziano con '#'
(commenti) vanno ignorate.

La PRIMA istruzione (non commento) è sempre
    IMMAGINE W H R G B
e dice di creare un'immagine larga W e alta H, tutta del colore (R, G, B).

Le istruzioni successive disegnano figure, nell'ordine in cui compaiono
(una figura disegnata dopo copre quelle disegnate prima):
    PUNTO x y R G B        colora il solo pixel (x, y)
    ORIZ  x y L R G B      segmento orizzontale di L pixel: (x, y), (x+1, y), ..., (x+L-1, y)
    VERT  x y L R G B      segmento verticale di L pixel:   (x, y), (x, y+1), ..., (x, y+L-1)
    RETT  x y w h R G B    rettangolo pieno largo w e alto h, con l'angolo in alto
                           a sinistra in (x, y): tutti i pixel con
                           x <= colonna < x+w  e  y <= riga < y+h

ATTENZIONE: una figura può uscire in parte dall'immagine (le coordinate
possono essere anche negative). In quel caso si disegnano SOLO i pixel che
cadono dentro l'immagine, gli altri si ignorano.

La funzione salva l'immagine nel file img_out e restituisce un dizionario
che ha come chiavi i tipi di figura presenti nel file ('PUNTO', 'ORIZ',
'VERT', 'RETT') e come valori quante volte compare ciascuno.
Non vanno messi nel dizionario 'IMMAGINE' né i tipi che non compaiono.

Esempio: se il file func3/disegno1.txt contiene
    IMMAGINE 12 8 0 0 0
    RETT 1 1 4 3 255 0 0
    ORIZ 0 6 12 0 255 0
    VERT 9 0 8 0 0 255
    PUNTO 3 2 255 255 255
func3('func3/disegno1.txt', 'func3/disegno1_out.png') crea un'immagine uguale
a func3/disegno1_exp.png e restituisce
    {'RETT': 1, 'ORIZ': 1, 'VERT': 1, 'PUNTO': 1}

Per salvare l'immagine usa la funzione save del modulo images.
"""

def func3(file_disegno, img_out):
    pass
    # inserisci qui il tuo codice


# print(func3('func3/disegno1.txt', 'func3/disegno1_out.png'))


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 8 punti     (FILE DI ISTRUZIONI: il pennello)

Definisci una funzione func4(img_in, file_comandi, img_out) che prende in input
    - img_in:       il percorso di un'immagine PNG su cui disegnare
    - file_comandi: il percorso di un file di testo con i comandi per un pennello
    - img_out:      il percorso del file PNG da creare

Un pennello si muove sull'immagine un pixel alla volta. All'inizio il
colore del pennello è bianco (255, 255, 255).
Il file contiene un comando per riga:
    START x y       (sempre la prima riga) il pennello parte dal pixel (x, y),
                    SENZA colorarlo
    COLORE R G B    da ora in poi il pennello usa il colore (R, G, B)
    DESTRA n        il pennello si sposta di n pixel verso destra   (x aumenta)
    SINISTRA n      il pennello si sposta di n pixel verso sinistra (x diminuisce)
    GIU n           il pennello si sposta di n pixel verso il basso (y aumenta)
    SU n            il pennello si sposta di n pixel verso l'alto   (y diminuisce)
    SALTA x y       il pennello si alza e va direttamente nel pixel (x, y),
                    SENZA colorare nulla

Quando il pennello si sposta di n pixel (DESTRA/SINISTRA/GIU/SU) colora con il
colore corrente ognuno degli n pixel su cui arriva (non quello da cui parte).
Il pennello non esce mai dall'immagine.

La funzione salva l'immagine modificata nel file img_out e restituisce una
tupla (x, y, passi), dove (x, y) è la posizione finale del pennello e passi
è il numero totale di pixel su cui il pennello è passato con DESTRA, SINISTRA,
GIU e SU (contando più volte un pixel su cui passa più volte).

Esempio: con l'immagine func4/tela1.png (10x10 nera) e il file func4/comandi1.txt
    START 2 2
    DESTRA 5
    GIU 5
    SINISTRA 5
    SU 5
il pennello disegna il bordo bianco di un quadrato con angoli (2,2) e (7,7),
torna al punto di partenza e la funzione restituisce (2, 2, 20).
Il pixel (2, 2) viene colorato dall'ultimo passo di SU.

Per leggere/salvare le immagini usa le funzioni load/save del modulo images.
"""

def func4(img_in, file_comandi, img_out):
    pass
    # inserisci qui il tuo codice


# print(func4('func4/tela1.png', 'func4/comandi1.txt', 'func4/tela1_out.png'))
