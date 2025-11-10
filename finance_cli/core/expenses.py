# =============== IMPORTY ===============
from datetime import datetime
import json, os
from core import storage as st
from main import wydatki
from tabulate import tabulate # type: ignore

# =============== FUNKCJE PODSTAWOWE ===============
def dodaj_wydatek(wydatki):
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
    st.zapisz_do_pliku(wydatki)
    print("Zapisano plik automatycznie ✅")
    return wydatek

def pokaz_wydatki(wydatki):
    dane = []
    for wydatek in wydatki:
        dane.append([wydatek["data"], wydatek["kategoria"], f"{wydatek["kwota"]} zł"])
    print(tabulate(dane, headers=["Data", "Kategoria", "Kwota"], tablefmt="fancy_grid"))

def sumuj_wydatki(wydatki):
    suma = 0.0
    for wydatek in wydatki:
        suma+=float(wydatek["kwota"])
    print(f"Suma: {suma} zł")

def filtruj_po_kategorii(wydatki, kategoria):
    czy_jest = False
    for wydatek in wydatki:
        if kategoria == wydatek["kategoria"]:
            print(f"""{wydatek["data"]} | {wydatek["kategoria"]} | {wydatek["kwota"]} zł""")
            czy_jest = True
    if czy_jest == False:
        print("Brak wydatków w tej kategorii.")

def edytuj_wydatek(wydatki):
    i=1
    for wydatek in wydatki:
        print(f"""{i}. {wydatek["data"]} | {wydatek["kategoria"]} | {wydatek["kwota"]} zł""")
        i+=1
    max_i = i
    i=1
    while True:
        try:
            edytuj = int(input("Który indeks chcesz edytować?: "))
        except:
            print("Błędna kwota")
            edytuj_wydatek(wydatki)
    
        if edytuj <= 0 or edytuj >= max_i:
           print("Podałeś zły indeks! Spróbuj ponownie!")
        else:
            break
    while True:
        try:
            kwota = float(input("Podaj nową kwotę (enter = nie zmieniaj): "))
            break
        except:
            print("Podałeś błędną kwotę.") 

    kategoria = input("Podaj nową kategorię (enter = nie zmieniaj): ")
    for wydatek in wydatki:
        if i == int(edytuj):
            if kwota != "":
                wydatek["kwota"] = float(kwota)
                st.zapisz_do_pliku(wydatki)
            if kategoria != "":
                wydatek["kategoria"] = kategoria
                st.zapisz_do_pliku(wydatki)
        i+=1
    print("✅ Zaktualizowano")

def sortuj_wydatki(wydatki):
    while True:
        po_czym = input("Podaj po czym chcesz posortować wydatki? (Kwota/Kategoria/Data): ")
        if po_czym.lower() == "kwota" or po_czym.lower() == "kategoria" or po_czym.lower() == "data":
            break
        else:
            print("Podałeś błędną odpowiedź.")
    
    posortowane = sorted(wydatki, key=lambda x: x[po_czym])
    dane = []
    for wydatek in posortowane:
        dane.append([wydatek["data"], wydatek["kategoria"], f"{wydatek["kwota"]} zł"])
    print(tabulate(dane, headers=["Data", "Kategoria", "Kwota"], tablefmt="fancy_grid"))

def wyswietl_statystyki(wydatki):
    if not wydatki:
        print("Brak danych do analizy")
    else:
        suma = sum(wydatek["kwota"] for wydatek in wydatki)
        srednia = suma / len(wydatki)
        najw = max(wydatki, key=lambda x: x["kwota"])
        najm = min(wydatki, key=lambda x: x["kwota"])
        najwtxt = f"{najw["kwota"]} zł ({najw["kategoria"]}, {najw["data"]})"
        najmtxt = f"{najm["kwota"]} zł ({najm["kategoria"]}, {najm["data"]})"

        suma_po_kategorii = {}
        for wydatek in wydatki:
            kat= wydatek["kategoria"]
            suma_po_kategorii[kat] = suma_po_kategorii.get(kat, 0) + wydatek["kwota"]

        statystyka = {
            "Liczba wydatków": len(wydatki),
            "Suma całkowita": f"{suma} zł",
            "Średni wydatek": f"{srednia} zł",
            "Największy wydatek": najwtxt,
            "Najmniejszy wydatek": najmtxt
        }
        print(tabulate(statystyka.items(), headers=["Metryka", "Wartość"], tablefmt="fancy_grid"))

        print("\nWydatki po kategoriach: ")
        print(tabulate(suma_po_kategorii.items(), headers=["Kategoria", "Suma"], tablefmt="fancy_grid"))
    

    

     
    