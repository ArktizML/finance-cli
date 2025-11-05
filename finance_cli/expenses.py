# =============== IMPORTY ===============
from datetime import datetime
import json, os
import storage as st
from utils import *
from main import wydatki

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
    st.zapisz_do_pliku()
    print("Zapisano plik automatycznie ✅")
    return wydatek

def pokaz_wydatki(wydatki):
    for wydatek in wydatki:
        print(f"""{wydatek["data"]} | {wydatek["kategoria"]} | {wydatek["kwota"]} zł""")

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
                st.zapisz_do_pliku()
            if kategoria != "":
                wydatek["kategoria"] = kategoria
                st.zapisz_do_pliku()
        i+=1
    print("✅ Zaktualizowano")