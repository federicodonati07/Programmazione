# -*- coding: utf-8 -*-
"""
testlib.py - libreria di supporto per grade.py (versione con output colorato).

NON modificare questo file e NON usarne le funzioni in program.py.

Colori:
    - verde  = test superato
    - rosso  = test fallito / errore
    - giallo = avvisi (funzione non implementata, suggerimenti)
I colori si disattivano da soli se l'output non è un terminale (es. se lo
redirigi su file). Puoi anche forzarli:
    NO_COLOR=1    python grade.py     -> niente colori
    FORCE_COLOR=1 python grade.py     -> colori sempre
"""
import csv
import glob
import hashlib
import os
import sys
import time
import traceback


# =============================================================================
# Colori e simboli
# =============================================================================

# se la console non sa stampare qualche carattere (es. lettere accentate),
# lo sostituisce con '?' invece di andare in errore
try:
    sys.stdout.reconfigure(errors='replace')
except Exception:
    pass


def _usa_colori():
    if os.environ.get('NO_COLOR'):
        return False
    if os.environ.get('FORCE_COLOR'):
        return True
    # console di Spyder / IPython / Jupyter: capiscono i colori ANSI
    if 'SPYDER_ARGS' in os.environ or 'ipykernel' in sys.modules:
        return True
    try:
        if not sys.stdout.isatty():
            return False
    except Exception:
        return False
    if os.name == 'nt':
        os.system('')          # attiva i codici ANSI nel terminale di Windows
    return True


COLORI_ATTIVI = _usa_colori()

_ANSI = {'RED': '\033[31m', 'GREEN': '\033[32m', 'YELLOW': '\033[33m',
         'CYAN': '\033[36m', 'GREY': '\033[90m', 'BOLD': '\033[1m',
         'RST': '\033[0m', 'ENDC': '\033[0m'}
# COL resta per compatibilità con i vecchi grade.py
COL = {k: (v if COLORI_ATTIVI else '') for k, v in _ANSI.items()}


def _c(testo, *stili):
    if not COLORI_ATTIVI:
        return str(testo)
    return ''.join(_ANSI[s] for s in stili) + str(testo) + _ANSI['RST']

def verde(t):     return _c(t, 'GREEN')
def rosso(t):     return _c(t, 'RED')
def giallo(t):    return _c(t, 'YELLOW')
def ciano(t):     return _c(t, 'CYAN')
def grigio(t):    return _c(t, 'GREY')
def grassetto(t): return _c(t, 'BOLD')


def _unicode_ok():
    enc = getattr(sys.stdout, 'encoding', None) or 'ascii'
    try:
        '✔✘⚠▶█░─×'.encode(enc)
        return True
    except (UnicodeEncodeError, LookupError):
        return False


if _unicode_ok():
    S_OK, S_ERR, S_WARN, S_RUN, S_PIENO, S_VUOTO, S_LINEA, S_PER = \
        '✔', '✘', '⚠', '▶', '█', '░', '─', '×'
else:
    S_OK, S_ERR, S_WARN, S_RUN, S_PIENO, S_VUOTO, S_LINEA, S_PER = \
        'OK', 'X', '!', '>', '#', '.', '-', 'x'


# =============================================================================
# Eccezioni usate dai test
# =============================================================================

class NotImplemented(Exception):
    """La funzione dello studente ha restituito None (probabilmente c'è ancora 'pass')."""
    pass


class TestFallito(AssertionError):
    """Il risultato è diverso da quello atteso. Il messaggio spiega cosa non va."""
    pass


# =============================================================================
# Confronti
# =============================================================================

_NOMI_TIPI = {'list': 'lista', 'tuple': 'tupla', 'dict': 'dizionario', 'int': 'intero',
              'float': 'float (numero con la virgola)', 'str': 'stringa', 'bool': 'booleano',
              'set': 'insieme (set)', 'NoneType': 'None'}


def _tipo(v):
    n = type(v).__name__
    return _NOMI_TIPI.get(n, n)


def _rr(v, maxlen=200):
    s = repr(v)
    return s if len(s) <= maxlen else s[:maxlen] + ' ...'


def check_val(res, expected, cosa='valore restituito'):
    """Confronta un valore qualsiasi (numero, tupla, lista...)."""
    if res == expected and type(res) == type(expected):
        return
    if res == expected:
        # stesso valore ma tipo diverso (es. 3.0 invece di 3): va bene, ma avvisa
        if not (isinstance(res, (int, float)) and isinstance(expected, (int, float))):
            return
        print(giallo(f'    {S_WARN} avviso: il valore è giusto ma è di tipo {_tipo(res)}, '
                     f'era atteso di tipo {_tipo(expected)}'))
        return
    righe = [f'{cosa} sbagliato',
             f'    atteso:   {_rr(expected)}   ({_tipo(expected)})',
             f'    ottenuto: {_rr(res)}   ({_tipo(res)})']
    suggerimenti = []
    if type(res) != type(expected):
        suggerimenti.append(f'hai restituito un valore di tipo {_tipo(res)}, ma era atteso di tipo {_tipo(expected)}')
    if isinstance(res, (tuple, list)) and isinstance(expected, (tuple, list)):
        if len(res) != len(expected):
            suggerimenti.append(f'lunghezza sbagliata: {len(res)} elementi invece di {len(expected)}')
        else:
            pos = [i for i in range(len(res)) if res[i] != expected[i]]
            for i in pos:
                righe.append(f'    -> posizione {i}: atteso {_rr(expected[i])}, ottenuto {_rr(res[i])}')
            if len(res) == 2 and list(res) == list(expected)[::-1]:
                suggerimenti.append('i due valori sono invertiti: controlla l\'ordine nella tupla')
    if isinstance(res, (int, float)) and isinstance(expected, (int, float)) \
            and not isinstance(res, bool):
        diff = res - expected
        righe.append(f'    differenza: {diff:+}')
    for s in suggerimenti:
        righe.append(giallo(f'    {S_WARN} {s}'))
    raise TestFallito('\n'.join(righe))


def check_dict(res, expected, cosa='dizionario restituito'):
    """Confronta due dizionari e dice quali chiavi mancano/avanzano/sono sbagliate."""
    if not isinstance(res, dict):
        raise TestFallito(f'{cosa}: hai restituito un valore di tipo {_tipo(res)}, era atteso un dizionario\n'
                          f'    atteso:   {_rr(expected)}\n'
                          f'    ottenuto: {_rr(res)}')
    if res == expected:
        return
    righe = [f'{cosa} sbagliato',
             f'    atteso:   {_rr(expected)}',
             f'    ottenuto: {_rr(res)}']
    for k in expected:
        if k not in res:
            righe.append(f'    -> manca la chiave {k!r} (valore atteso {expected[k]!r})')
        elif res[k] != expected[k]:
            righe.append(f'    -> chiave {k!r}: atteso {expected[k]!r}, ottenuto {res[k]!r}')
    for k in res:
        if k not in expected:
            righe.append(f'    -> chiave in più {k!r} (valore {res[k]!r}): non doveva esserci')
    raise TestFallito('\n'.join(righe))


def check_list(res, expected, cosa='lista restituita'):
    if not isinstance(res, list):
        raise TestFallito(f'{cosa}: hai restituito un valore di tipo {_tipo(res)}, era attesa una lista')
    check_val(res, expected, cosa)

checkList = check_list
checkDict = check_dict


# =============================================================================
# Immagini
# =============================================================================

def image_load(filename):
    """Carica un PNG come lista di liste di tuple (R, G, B)."""
    import png
    with open(filename, 'rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        w *= 3
        return [[(line[i], line[i + 1], line[i + 2]) for i in range(0, w, 3)]
                for line in png_img]


MAX_PIXEL_MOSTRATI = 8
MAPPA_MAX_W = 80
MAPPA_MAX_H = 50


def check_img_file(ottenuta, attesa):
    """Confronta il PNG prodotto dallo studente (ottenuta) con quello atteso.
    In caso di differenze spiega: dimensioni, quanti pixel, dove, che colori."""
    if not os.path.exists(ottenuta):
        raise TestFallito(f'il file {ottenuta} non esiste\n' +
                          giallo(f'    {S_WARN} hai chiamato images.save(img, ...) con il percorso giusto?'))
    try:
        img_a = image_load(ottenuta)
    except Exception as e:
        raise TestFallito(f'non riesco a leggere {ottenuta} come PNG ({e.__class__.__name__}: {e})')
    img_b = image_load(attesa)

    ha, hb = len(img_a), len(img_b)
    wa = len(img_a[0]) if ha else 0
    wb = len(img_b[0]) if hb else 0
    if (wa, ha) != (wb, hb):
        righe = ['dimensioni dell\'immagine sbagliate',
                 f'    attese:   larghezza {wb}, altezza {hb}   ({wb}{S_PER}{hb})',
                 f'    ottenute: larghezza {wa}, altezza {ha}   ({wa}{S_PER}{ha})']
        if (wa, ha) == (hb, wb):
            righe.append(giallo(f'    {S_WARN} hai scambiato larghezza e altezza: '
                                'l\'immagine è una lista di RIGHE, len(img) è l\'altezza'))
        raise TestFallito('\n'.join(righe))

    diversi = []
    for y in range(hb):
        for x in range(wb):
            if img_a[y][x] != img_b[y][x]:
                diversi.append((x, y))
    if not diversi:
        return

    tot = wb * hb
    xs = [p[0] for p in diversi]
    ys = [p[1] for p in diversi]
    righe = [f'l\'immagine {ottenuta} è diversa da {attesa}',
             f'    pixel diversi: {len(diversi)} su {tot} ({100 * len(diversi) / tot:.1f}%)',
             f'    zona delle differenze: x da {min(xs)} a {max(xs)}, y da {min(ys)} a {max(ys)}',
             f'    primi pixel diversi (x = colonna, y = riga):']
    for (x, y) in diversi[:MAX_PIXEL_MOSTRATI]:
        righe.append(f'      (x={x:>3}, y={y:>3})  atteso {verde(img_b[y][x])}  ottenuto {rosso(img_a[y][x])}')
    if len(diversi) > MAX_PIXEL_MOSTRATI:
        righe.append(f'      ... e altri {len(diversi) - MAX_PIXEL_MOSTRATI}')

    # suggerimenti automatici
    sugg = []
    if all(img_a[y][x] == img_a[0][0] for y in range(ha) for x in range(wa)):
        sugg.append(f'la tua immagine è tutta di un colore {img_a[0][0]}: non hai disegnato/modificato nulla?')
    trasposta = (wa == ha) and all(img_a[y][x] == img_b[x][y] for y in range(ha) for x in range(wa))
    if trasposta:
        sugg.append('la tua immagine è la "trasposta" di quella attesa: hai scambiato x e y (img[y][x]!)')
    for s in sugg:
        righe.append(giallo(f'    {S_WARN} {s}'))

    if wb <= MAPPA_MAX_W and hb <= MAPPA_MAX_H:
        sd = set(diversi)
        righe.append(f'    mappa (' + rosso('X') + ' = pixel diverso, . = uguale):')
        righe.append('         ' + ''.join(str(x // 10) if x % 10 == 0 else ' ' for x in range(wb)))
        for y in range(hb):
            riga = ''.join(rosso('X') if (x, y) in sd else grigio('.') for x in range(wb))
            righe.append(f'    {y:>3}  {riga}')
    righe.append(grigio(f'    (apri i due file per confrontarli a occhio)'))
    raise TestFallito('\n'.join(righe))


# =============================================================================
# Controllo che i file di input/attesi non siano stati sovrascritti
# =============================================================================

def check_expected():
    files = glob.glob(os.path.join('backup', '**'), recursive=True)
    for file_b in files:
        if os.path.isfile(file_b):
            file_e = os.path.join(*file_b.split(os.sep)[1:])
            ok = os.path.exists(file_e)
            if ok:
                with open(file_b, 'rb') as frb, open(file_e, 'rb') as fre:
                    ok = hashlib.md5(frb.read()).hexdigest() == hashlib.md5(fre.read()).hexdigest()
            if not ok:
                print(rosso(grassetto(
                    f'\nATTENZIONE: il file di input/atteso "{file_e}" è stato modificato o cancellato!\n'
                    f'Ricopialo da "{file_b}" (nella cartella backup) e rilancia grade.py.\n'
                    f'Probabilmente il tuo codice salva l\'output sul file sbagliato.')))
                sys.exit(1)


# =============================================================================
# Esecuzione dei test
# =============================================================================

def _dove_in_program(tb):
    """Trova l'ultima riga di program.py coinvolta nell'errore."""
    for fr in reversed(traceback.extract_tb(tb)):
        if os.path.basename(fr.filename) == 'program.py':
            return fr
    return None


_SUGGERIMENTI_ECCEZIONI = {
    'IndexError': 'stai leggendo/scrivendo fuori dall\'immagine o dalla lista. Ricorda: img[y][x], '
                  'y va da 0 a len(img)-1 e x da 0 a len(img[0])-1',
    'FileNotFoundError': 'il percorso del file è sbagliato: usa il parametro ricevuto dalla funzione',
    'ValueError': 'spesso succede con int(...) su una stringa che non è un numero, '
                  'o con un unpacking del numero sbagliato di valori (es. r, g, b = ...)',
    'TypeError': 'controlla i tipi: stai usando una stringa al posto di un int (hai fatto int(...)?) '
                 'oppure una variabile che vale None?',
    'KeyError': 'stai leggendo una chiave che non è (ancora) nel dizionario: usa .get(k, 0) o controlla con "in"',
    'UnboundLocalError': 'usi una variabile prima di averle dato un valore',
    'NameError': 'nome non definito: errore di battitura o variabile/funzione mai creata?',
    'ZeroDivisionError': 'stai dividendo per zero',
    'RecursionError': 'ricorsione infinita',
}


def _punti_txt(p):
    return f'{p:g}'


def runOne(test, max_punti, logfile='', stack_trace=False):
    doc = (test.__doc__ or '').strip()
    print(grassetto(f'{S_RUN} {test.__name__}') + (grigio(f'   {doc}') if doc else ''))
    start = time.time()
    v = 0
    try:
        v = test() or 0
        ms = (time.time() - start) * 1000
        print(verde(f'  {S_OK} OK') + f'   {_punti_txt(v)}/{_punti_txt(max_punti)} punti' +
              grigio(f'   ({ms:.0f} ms)'))
    except NotImplemented:
        print(giallo(f'  {S_WARN} NON IMPLEMENTATA: la funzione restituisce None '
                     f'(c\'è ancora "pass" o manca il return?)') + f'   0/{_punti_txt(max_punti)}')
    except TestFallito as e:
        print(rosso(f'  {S_ERR} SBAGLIATO') + f'   0/{_punti_txt(max_punti)} punti')
        for riga in str(e).split('\n'):
            print('    ' + riga)
    except AssertionError as e:   # assert dei vecchi test
        print(rosso(f'  {S_ERR} SBAGLIATO') + f'   0/{_punti_txt(max_punti)} punti')
        print('    ' + str(e))
    except Exception as e:
        nome = e.__class__.__name__
        print(rosso(f'  {S_ERR} ERRORE durante l\'esecuzione: {nome}: {e}') +
              f'   0/{_punti_txt(max_punti)} punti')
        fr = _dove_in_program(e.__traceback__)
        if fr:
            print(f'    in program.py, riga {fr.lineno} (funzione {fr.name}):')
            print(ciano(f'        {fr.line}'))
        if nome == 'ValueError' and 'invalid literal for int()' in str(e):
            print(giallo(f'    {S_WARN} int() ha ricevuto un testo che non è un numero intero: '
                         'controlla quali righe (o quali parti della riga) stai convertendo'))
        elif nome in _SUGGERIMENTI_ECCEZIONI:
            print(giallo(f'    {S_WARN} {_SUGGERIMENTI_ECCEZIONI[nome]}'))
        if stack_trace:
            print(grigio('-' * 30 + ' STACK TRACE ' + '-' * 30))
            traceback.print_exc()
            print(grigio('-' * 73))
        elif not fr:
            print(grigio('    (lancia "python grade.py --debug" per vedere lo stack trace completo)'))
    print()
    log([(test.__name__, v)], logfile)
    return v


def emptyLog(logfile):
    if logfile:
        with open(logfile, 'w', newline='', encoding='utf8') as f:
            f.truncate()


def log(results, logfile):
    if logfile:
        with open(logfile, 'a', newline='', encoding='utf8') as f:
            csv.writer(f).writerows(results)


def _barra(p, m, n=20):
    pieni = round(n * p / m) if m else 0
    b = S_PIENO * pieni + S_VUOTO * (n - pieni)
    if p >= m:
        return verde(b)
    if p > 0:
        return giallo(b)
    return rosso(b)


def runtests(tests, punti_funzioni, logfile='grade.csv', stack_trace=False, soglia=18):
    """tests: lista di funzioni test_funcN_K
    punti_funzioni: dict {'func1': 6, ...} con il punteggio massimo di ogni funzione."""
    emptyLog(logfile)
    gruppi = {}
    for t in tests:
        gruppi.setdefault(t.__name__.split('_')[1], []).append(t)

    risultati = {}   # func -> (punti, test_ok, test_totali)
    for func, lista in gruppi.items():
        maxf = punti_funzioni.get(func, 0)
        maxt = maxf / len(lista) if lista else 0
        print(ciano(grassetto(f'{S_LINEA * 25} {func.upper()} ({_punti_txt(maxf)} punti) {S_LINEA * 25}')))
        tot, ok = 0, 0
        for t in lista:
            v = runOne(t, maxt, logfile, stack_trace)
            tot += v
            ok += 1 if v else 0
        risultati[func] = (tot, ok, len(lista))

    # ------------------------------ riepilogo ------------------------------
    print(grassetto(S_LINEA * 62))
    print(grassetto('RIEPILOGO'.center(62)))
    print(grassetto(S_LINEA * 62))
    totale, massimo = 0, 0
    for func, (p, ok, n) in risultati.items():
        m = punti_funzioni.get(func, 0)
        totale += p
        massimo += m
        if p >= m:
            stato = verde(f'{S_OK} tutto giusto')
        elif p > 0:
            stato = giallo(f'{S_WARN} {ok}/{n} test')
        else:
            stato = rosso(f'{S_ERR} 0/{n} test')
        print(f'  {func:<6} {_barra(p, m)} {_punti_txt(round(p, 2)):>5} / {_punti_txt(m):<3} {stato}')
    print(grassetto(S_LINEA * 62))
    tot_txt = f'TOTALE: {_punti_txt(round(totale, 2))} / {_punti_txt(massimo)}'
    if totale >= soglia:
        print(verde(grassetto(f'  {tot_txt}   {S_OK} SUFFICIENTE (servono almeno {soglia})')))
    else:
        print(rosso(grassetto(f'  {tot_txt}   {S_ERR} INSUFFICIENTE (servono almeno {soglia}, '
                              f'mancano {_punti_txt(round(soglia - totale, 2))})')))
    print(grassetto(S_LINEA * 62))
    return totale
