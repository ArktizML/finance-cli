# =============== IMPORTY ===============
from datetime import datetime
import json, os
import storage as st
import expenses as ex
import utils as ut

# =============== GLOBALNE DANE ===============
wydatki = []  # lista słowników

# =============== MENU ===============
def pokaz_menu():
    print("\n=== Personal Finance CLI ===")
    print("1. Dodaj wydatek")
    print("2. Wyświetl wydatki")
    print("3. Pokaż sumę wydatków")
    print("4. Zapisz i wyjdź")
    print("5. Filtruj po kategorii")
    print("6. Edytuj wydatek")

# =============== PĘTLA GŁÓWNA ===============
def main():
    wydatki = st.wczytaj_z_pliku()
    try:
        st.wczytaj_z_pliku()
    except:
        st.zapisz_do_pliku()

    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            ex.dodaj_wydatek(wydatki)
        elif wybor == "2":
            ex.pokaz_wydatki(wydatki)
        elif wybor == "3":
            ex.sumuj_wydatki(wydatki)
        elif wybor == "4":
            st.zapisz_do_pliku()
            print("Zapisano. Do zobaczenia!")
            break
        elif wybor == "5":
            kategoria = input("Z jakiej kategorii pokazać wydatki?: ")
            ex.filtruj_po_kategorii(wydatki, kategoria.lower())
        elif wybor == "6":
            ex.edytuj_wydatek(wydatki)
        else:
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    main()
