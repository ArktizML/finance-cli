# =============== IMPORTY ===============
from datetime import datetime
import json, os

# =============== GLOBALNE DANE ===============
wydatki = []  # lista słowników

# =============== FUNKCJE PODSTAWOWE ===============
def wczytaj_z_pliku():
    global wydatki
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as file:
            wydatki = json.load(file)

def zapisz_do_pliku():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(wydatki, file, ensure_ascii=False, indent=4)

def dodaj_wydatek():
    while True:
        kwota_raw = input("Podaj kwotę (np. 20.50): ").strip()
        # zamiana przecinka na kropkę i próba konwersji
        kwota_raw = kwota_raw.replace(",", ".")
        try:
            kwota = float(kwota_raw)
            break
        except ValueError:
            print("Niepoprawna kwota — wpisz liczbę (np. 20.50). Spróbuj ponownie.")

    kategoria = input("Podaj kategorię: ").strip().lower()
    if not kategoria:
        kategoria = "inne"

    wydatek = {
        "kwota": kwota,
        "kategoria": kategoria,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    wydatki.append(wydatek)
    print("Dodano wydatek ✅ —", wydatek)
    return wydatek

def pokaz_wydatki():
    for wydatek in wydatki:
        print(f"""{wydatek["data"]} | {wydatek["kategoria"]} | {wydatek["kwota"]} zł""")

def sumuj_wydatki():
    suma = 0.0
    for wydatek in wydatki:
        suma+=float(wydatek["kwota"])
    print(f"Suma: {suma} zł")

def filtruj_po_kategorii(kategoria):
    czy_jest = False
    for wydatek in wydatki:
        if kategoria == wydatek["kategoria"]:
            print(f"""{wydatek["data"]} | {wydatek["kategoria"]} | {wydatek["kwota"]} zł""")
            czy_jest = True
    if czy_jest == False:
        print("Brak wydatków w tej kategorii.")

def edytuj_wydatek():
    i=1
    for wydatek in wydatki:
        print(f"""{i}. {wydatek["data"]} | {wydatek["kategoria"]} | {wydatek["kwota"]} zł""")
        i+=1
    max_i = i
    i=1
    while True:
        edytuj = int(input("Który indeks chcesz edytować?: "))
        if edytuj < 0 or edytuj > max_i:
           print("Podałeś zły indeks! Spróbuj ponownie!")
        else:
            break
    kwota = input("Podaj nową kwotę (enter = nie zmieniaj): ")
    kategoria = input("Podaj nową kategorię (enter = nie zmieniaj): ")
    for wydatek in wydatki:
        if i == int(edytuj):
            if kwota != "":
                wydatek["kwota"] = float(kwota)
                zapisz_do_pliku()
            if kategoria != "":
                wydatek["kategoria"] = kategoria
                zapisz_do_pliku()
        i+=1
    print("✅ Zaktualizowano")

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
        elif wybor == "5":
            kategoria = input("Z jakiej kategorii pokazać wydatki?: ")
            filtruj_po_kategorii(kategoria.lower())
        elif wybor == "6":
            edytuj_wydatek()
        else:
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    main()
