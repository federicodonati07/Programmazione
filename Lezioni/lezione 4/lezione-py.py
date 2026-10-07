voto = int(input("Inserisci voto: "))

match voto:
    case 0 | 1 | 2 | 3 | 4 | 5:
        print("Insufficiente")
        
    case 6 | 7:
        print("Sufficiente")

    case 8 | 9:
        print("Ottimo")
        
    case 10:
        print("Eccellente")