from funkcje import zaladuj_zadania
from funkcje import pokaz_zadania
from funkcje import dodaj_zadanie
from funkcje import usun_zadanie
from funkcje import zapisz_zadania

wybor_zadania = -1

zadania = []
terminy = []
lista_zadan = zadania + terminy

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
    
    print("")
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Zakończ")
    print("")
    
    wybor_zadania = int(input("Wybierz operację: "))
    print("")