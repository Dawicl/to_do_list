
wybor_zadania = -1

zadania = []

def pokaz_zadania():
    numer_zadania = 0
    for zadanie in zadania:
        print(zadanie + " " + str(numer_zadania))
        numer_zadania += 1

def dodaj_zadanie():
    zadanie = input("Podaj zadanie które chcesz dodać: ")
    termin = input("Podaj termin realizacji zadania: ")
    zadania.append(zadanie + " - termin realizacji: " + termin)
    print("Zadanie zostało dodane do listy.")

def usun_zadanie():
    numer_zadania = int(input("Podaj numer zadania do usunięcia: "))
    if numer_zadania < 0 or numer_zadania > len(zadania) - 1:
        print("Brak zadania o podanym numerze")
        return

    zadania.pop(numer_zadania)
    print("Wybrane zadanie zostało usunięte.")

def zapisz_zadania():
    plik = open("lista_zadan.txt", "w")
    for zadanie in zadania:
        plik.write(zadanie+"\n")
    plik.close

def zaladuj_zadania():
    plik = open("lista_zadan.txt")
    for linia in plik.readlines():
        zadania.append(linia.strip())

    plik.close

zaladuj_zadania()

while wybor_zadania != 5:
    if wybor_zadania == 1:
        pokaz_zadania()

    if wybor_zadania == 2:
        dodaj_zadanie()

    if wybor_zadania == 3:
        usun_zadanie()

    if wybor_zadania == 4:
        zapisz_zadania()
   
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Zakończ")

    wybor_zadania = int(input("Wybierz operację: "))