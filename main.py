import funkcje

wybor_zadania = -1

funkcje.zaladuj_zadania()

while wybor_zadania != 5:
    if wybor_zadania == 1:
        funkcje.pokaz_zadania()

    if wybor_zadania == 2:
        funkcje.dodaj_zadanie()

    if wybor_zadania == 3:
        funkcje.usun_zadanie()

    if wybor_zadania == 4:
        funkcje.zapisz_zadania()
    
    print("")
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Zakończ")
    print("")
    
    wybor_zadania = int(input("Wybierz operację: "))
    print("")