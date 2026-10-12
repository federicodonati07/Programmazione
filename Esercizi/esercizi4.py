# Ignorare le righe fino alla 31 (servono per eseguire i test)
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


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    string = list(string)
    strip_string = []
    
    for x in string:
        if(x != " "):
            strip_string.append(x)
            
    output =  "".join(strip_string)
    return output
            


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    result_list = []
    current_word = ""
    
    for char in string:
        if char in characters:
            if current_word != "":
                result_list.append(current_word)
                current_word = ""
                
        else:
            current_word += char
            
    
    if current_word != "":
        result_list.append(current_word)
        
    return result_list
    

    

# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    
    output = ""
    
    i = 0
    len_find = len(find)
    
    while i < len(string):
        if(string[i:i+len_find] == find):
            output += replace
            i += len_find
            
        else:
            output += string[i]
            i += 1
    
    return output


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    
    offset = -offset if decrypt else offset
    output = []
    
    
    for char in string:
        if 'a'<=char<='z':
            base = ord('a')
            
            shifted = (ord(char)-base+offset)%26
            
            output.append(chr(base+shifted))
            
        else:
            output.append(char)
            
    return "".join(output)
    
    
            
            
        
        
    


    

# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.
def check_pwd(pwd: str) -> bool:
    simbolil = ["$", "#", "@"]        
    
    if not 6 <= len(pwd) <= 16:
        return False
    
    minuscole = any(c.islower() for c in pwd)
    maiuscole = any(c.isupper() for c in pwd)
    numeri = any(c.isdigit() for c in pwd)
    simboli = any(c in simbolil for c in pwd)
    
    non_autorizzati = any(not (c.islower() or c.isupper() or c.isdigit() or c in simbolil) for c in pwd)
    
    return minuscole and maiuscole and numeri and simboli and not non_autorizzati

# Scrivere una funzione che converte una stringa di caratteri numerici
# nell'intero corrispondente. Non usare la funzione `int(string)`.
def string_to_int(string: str) -> int:
    
    negativo = False
    
    if(string[0] == "-"):
        negativo = True
        string = string[1:]
    
    elif(string[0] == "+"):
        string = string[1:]
    
    else:
        string = string[0:]
        
    numero = 0
    
    for c in string:
        cifra = ord(c)-ord('0')

        numero = numero * 10 + cifra

    return -numero if negativo else numero  


# Scrivere una funzione che converte un intero in una stringa di caratteri
# numerici corrispondenti all'intero. Non usare la funzione `str(integer)`.
def int_to_string(integer: int) -> str:
    return f"{integer}"


# Test funzioni
check_test(strip_whitespace, 'Pippo', '  Pippo  ')
check_test(strip_whitespace, '', '   ')
check_test(split_string, ['Pippo', 'Pluto'], 'Pippo Pluto  ', ' \t\r\n')
check_test(split_string, ['Pippo', 'Pluto'], 'Pippo   Pluto  ', ' \t\r\n')
check_test(replace_substring, 'Hello Pippo. Hello Pluto.', 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
check_test(replace_substring, 'Pipp0', 'Pippo', 'o', '0')
check_test(replace_substring, 'Ciao! Pippo', 'Ciao Pippo', 'Ciao', 'Ciao!')
check_test(caesar_cypher, 'tzrf gzggf', 'ciao pippo', 17, False)
check_test(caesar_cypher, 'ciao pippo', 'tzrf gzggf', 17, True)
check_test(check_pwd, False, "a")
check_test(check_pwd, False, "000000000000000000")
check_test(check_pwd, False, "almeno6")
check_test(check_pwd, False, "Aa@09asng2/")
check_test(check_pwd, True, "Aa@09asng2")
check_test(string_to_int, 5, "5")
check_test(string_to_int, 123, "123")
check_test(int_to_string, "5", 5)
check_test(int_to_string, "123", 123)