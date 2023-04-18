wybor_zadania = -1

zadania = []
terminy = []
lista_zadan = zadania + terminy


def pokaz_zadania():
    numer_zadania = 0
    for zadanie in lista_zadan:
        print(zadanie + " " + "[" + str(numer_zadania) + "]")
        numer_zadania += 1

def dodaj_zadanie():
    zadanie = input("Podaj zadanie które chcesz dodać: ")
    termin = input("Podaj termin realizacji zadania: ")
    zadania.append(zadanie)
    terminy.append(termin)
    lista_zadan.append(zadanie + " - termin realizacji: " + termin)
    print("Zadanie zostało dodane do listy.")

def usun_zadanie():
    try:
        pokaz_zadania()
        print("")
        numer_zadania = int(input("Podaj numer zadania do usunięcia: "))
        if numer_zadania < 0 or numer_zadania > len(lista_zadan) - 1:
            print("Brak zadania o podanym numerze")
            return
    
        lista_zadan.pop(numer_zadania)
        print("Wybrane zadanie zostało usunięte.")
    except:
        print("Podawaj tylko numery indeksów!")
        usun_zadanie()

def zapisz_zadania():
    plik = open("lista_zadan.txt", "w")
    for zadanie in lista_zadan:
        plik.write(str(zadanie+"\n"))
    plik.close

def zaladuj_zadania():
    try:
        plik = open("lista_zadan.txt")
        for linia in plik.readlines():
            lista_zadan.append(linia.strip())

        plik.close
    except FileNotFoundError:
        return