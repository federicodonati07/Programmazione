# %% Esercizio 1
def es1():
    number = int(input("Inserisci un numero inter: "))
    
    number += 5
    print(f"Dopo += 5: {number}")
    
    number *= 3
    print(f"Dopo *= 3: {number} ")
    
    number -= 4
    print(f"Dopo -= 4: {number}")
    
    number //= 2 
    print(f"Dopo //= 2: {number}")
    
    number %= 7
    print(f"Dopo %= 7: {number}")
    
    number **2
    print(f"Dopo **= 2: {number}")
    
    parola = input("Inserisci una parola: ")
    
    parola += "!"
    print(f"Dopo += '!': {parola}")
    
    parola *= 3
    print(f"Dopo *= 3: {parola}")
    
es1()
# %% Esercizio 2
def es2():
    x = int(input("N intero 1: "))
    y = int(input("N intero 2: "))

    print(f"x={x} b={y}")
    x, y = y, x
    print(f"Scambio x={x} y={y}")        
    
    w1 = input("w1: ")
    w2 = input("w2: ")
    w3 = input("w3: ")
    
    print(f"w1 = {w1} w2={w2} w3={w3}")
    
    w1, w2, w3 = w2, w3, w1       
    print(f"Scambio w1 = {w1} w2={w2} w3={w3}")
     
        
        
es2()

# %% Esercizio 3

def es3():
    info = input("Dati: ")
    
    nome, cognome, data = info.split(" ")
    data = int(data)
    
    
    eta = 2026-data
    
    print(f"--- Scheda ---\nNome: {nome}\nCognome: {cognome}\nData: {data}\nEta nel 2026: {eta}")


es3()

# %% Esercizio 4

def es4():
    l1 = int(input("l1: "))
    l2 = int(input("l2: "))
    l3 = int(input("l3: "))
    
    if(l1 > l2+l3):
        print("Non è un triangolo")
    
    elif(l2 > l1+l3):
        print("Non è un triangolo")
        
    elif(l3 > l1+l2):
        print("Non è un triangolo")
     
    else:   
        
        if(l1 == l2 and l2 == l3):
            print("Triangolo Equilatero")
            
        elif(l1 == l2 or l2 == l3 or l3 == l1):
            print("Triangolo Isoscele")
            
        else:
            print("Triangolo Scaleno")



es4()

# %% Esercizio 5

def es5():
    a = int(input("Primo numero: "))
    b = int(input("Secondo numero: "))
    
    oper = input("operazione: ")
    
    match oper:
        case "+":
            print(f"{a} + {b}: {a+b}")    
            
        case "-":
            print(f"{a} - {b}: {a-b}")
            
        case "*"|"x":
            print(f"{a} x {b}: {a*b}")    
            
        case "/":
            if(b == 0):
                print("Errore")
                
            else:
                print(f"{a} / {b}: {a/b}")    
                
        case "//":
            if(b == 0):
                print("Errore")
                
            else:
                print(f"{a} // {b}: {a//b}") 
                    
        case "%":
            if(b == 0):
                print("Errore")
                
            else:
                print(f"{a} % {b}: {a%b}") 
                
        case "**":
            print(f"{a} ** {b}: {a**b}")
            
            
        case _:
            print("Operatore non valido")
    
    
    
    
    
    
    
es5()

# %% Esercizio 6

def es6():
    cmd = input("comando: ")
    cmd = cmd.split(" ")
    list(cmd)
    
    print(cmd)
    
    
        
    match cmd[0]:
        case "ciao":
            if(len(cmd) == 2):
                param = cmd[1]
                
                print(f"Ciao {param}!")
            else:
                print("Ciao!")
                
        case "somma":
            if(len(cmd) == 3):
                print(f"Somma: {int(cmd[1]) + int(cmd[2])}")
                
            else:
                print("errore")
                
        case "esci"|"fine":
            print("Arrivederci!")
            
        case _:
            print("Comando non riconosciuto")
    
    
    
    
    
es6()

# %% Esercizio 7

def es7():
    n = int(input("Intero: "))
    
    tab = [n*i for i in range(1, 11)]
    
    tabs = [str(x) for x in tab]
    outputtabs = " ".join(tabs)
    
    
    print(outputtabs)

    rtab = [n*i for i in range(10, 0, -1)]
    rtabs = [str(x) for x in rtab]
    outputrtabs = " ".join(rtabs)
    
    print(outputrtabs)
    
    somma = 0
    flist = []
    
    if(n > 2):
        for i in range(1, n):
            flist.append(i)
            
    flist += tab
    for x in range(len(flist)):
        if(flist[x] % 2 == 0 and flist[x] <= n):
            somma += flist[x]
            
    
        
                
        
                
            
    print(f"somma dei pari da 2 a {n}: {somma}")
    
        
        
    
    
    
    
es7()

# %% Esercizio 8

def es8():
    n = int(input("Intero >= 2: "))
    
    if(n >= 2):
        for d in range(2, n):
            if(n % d == 0):
                print(f"{n} non è primo: è divisibile per {d}")
                break
            
        else:
            print(f"{n} è primo")
        
    
    
    
es8()

# %% Esercizio 9

def es9():
    
    n = 25
    c = 0
    t = 0
    
    while True:
        c = int(input("Indovina il numero: "))
        
        if(c > n):
            print("Troppo Alto")
            t+=1
            
        elif(c < n):
            print("Troppo basso")
            t += 1
            
        elif(c == n):
            print("Hai indovinato il numero in {t} tentativi")
            break
        
        
    
    


es9()
