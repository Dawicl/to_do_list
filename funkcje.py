wybor_zadania = -1

zadania = []

def pokaz_zadania():
    numer_zadania = 0
    for zadanie in zadania:
        print(zadanie[0] + " termin realizacji: " + zadanie[1] + " " + "[" + str(numer_zadania) + "]")
        numer_zadania += 1

def dodaj_zadanie():
    zadanie = input("Podaj zadanie które chcesz dodać: ")
    termin = input("Podaj termin realizacji zadania: ")
    if len(termin) == 10 and termin[0:2].isdigit() and termin[2] == '.' and termin[3:5].isdigit() \
    and termin[5] == '.' and termin[5:-1].isdigit() and int(termin[0:2]) >= 0 and int(termin[0:2]) <= 31:
        pojedyncze_zadanie = [zadanie, termin]
        zadania.append(pojedyncze_zadanie)
        print("Zadanie zostało dodane do listy.")
    else:
        print()
        print("Podaj datę w formacie dd.mm.rrrr")
        print("Podaj zadanie jeszcze raz \n --------------------")
        dodaj_zadanie()


def usun_zadanie():
    try:
        pokaz_zadania()
        print("")
        numer_zadania = int(input("Podaj numer zadania do usunięcia: "))
        if numer_zadania < 0 or numer_zadania > len(zadania) - 1:
            print("Brak zadania o podanym numerze")
            return
    
        zadania.pop(numer_zadania)
        print("Wybrane zadanie zostało usunięte.")
    except:
        print("Podawaj tylko numery indeksów!")
        usun_zadanie()

def zapisz_zadania():
    plik = open("lista_zadan.txt", "w")
    for zadanie in zadania:
        plik.write(str(zadanie+"\n"))
    plik.close

def zaladuj_zadania():
    try:
        plik = open("lista_zadan.txt")
        for linia in plik.readlines():
            zadania.append(linia.strip())

        plik.close
    except FileNotFoundError:
        return