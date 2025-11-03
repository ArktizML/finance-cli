# =============== IMPORTY ===============
from datetime import datetime

# =============== GLOBALNE DANE ===============
wydatki = []  # lista słowników

# =============== FUNKCJE PODSTAWOWE ===============
def wczytaj_z_pliku():
    pass  # TODO: wczytaj dane z pliku i dodaj do listy 'wydatki'

def zapisz_do_pliku():
    pass  # TODO: zapisz listę wydatków do pliku

def dodaj_wydatek():
    x = input("Podaj kwotę: ")
    y = input("Podaj kategorię: ")
    wydatek ={
        "kwota": x,
        "kategoria": y
    }
    wydatki.append(wydatek)
    print("Dodano wydatek ✅")
    pass  # TODO: input użytkownika, dodaj słownik {"kwota": x, "kategoria": y, "data": dzisiaj}

def pokaz_wydatki():
    pass  # TODO: ładnie wypisz wszystkie wydatki

def sumuj_wydatki():
    pass  # TODO: policz sumę i wypisz wynik

# =============== MENU ===============
def pokaz_menu():
    print("\n=== Personal Finance CLI ===")
    print("1. Dodaj wydatek")
    print("2. Wyświetl wydatki")
    print("3. Pokaż sumę wydatków")
    print("4. Zapisz i wyjdź")

# =============== PĘTLA GŁÓWNA ===============
def main():
    wczytaj_z_pliku()

    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_wydatek()
        elif wybor == "2":
            pokaz_wydatki()
        elif wybor == "3":
            sumuj_wydatki()
        elif wybor == "4":
            zapisz_do_pliku()
            print("Zapisano. Do zobaczenia!")
            break
        else:
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    main()
