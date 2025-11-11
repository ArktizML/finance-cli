# =============== IMPORTY ===============
from datetime import datetime
import json, os
import csv
import matplotlib.pyplot as plt

# =============== FUNKCJE PODSTAWOWE ===============
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "data.json")

def wczytaj_z_pliku():
    if os.path.exists(DATA_PATH):
        try:
            with open(DATA_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    else:
        return []
            

def zapisz_do_pliku(wydatki):
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(wydatki, file, ensure_ascii=False, indent=4)

def exportuj_do_csv(wydatki):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data", f"raport_{datetime.now().strftime("%Y-%m-%d")}.csv")
    WYKRES_PATH = os.path.join(BASE_DIR, "data", f"wykres_{datetime.now().strftime("%Y-%m-%d")}.png")

    wczytaj_z_pliku()
    
    with open(DATA_PATH, "w", newline="", encoding="utf-8") as file:
        obiekt_writer = csv.DictWriter(file, fieldnames=["data", "kategoria", "kwota"])
        obiekt_writer.writeheader()       
        for wydatek in wydatki:
            obiekt_writer.writerow(wydatek)
    
    suma_po_kategorii = {}

    for wydatek in wydatki:
        kat= wydatek["kategoria"]
        suma_po_kategorii[kat] = suma_po_kategorii.get(kat, 0) + wydatek["kwota"]

    kategorie = list(suma_po_kategorii.keys())
    kwoty = list(suma_po_kategorii.values())
    fig, ax = plt.subplots()
    plt.bar(kategorie, kwoty)
    ax.set_title("Wydatki wg. kategorii")
    ax.set_xlabel("Kategoria")
    ax.set_ylabel("Kwota [zł]")
    plt.savefig(WYKRES_PATH)

    print("✅ Dane wyeksportowane")
    print("✅ Utworzono i zapisano wykres")

# def importuj_z_csv():
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     DATA_PATH = os.path.join(BASE_DIR, "data", "export.csv")

#     if os.path.exists(DATA_PATH):
#         try:
#             with open(DATA_PATH, "r", encoding="utf-8") as file:
#                 obiekt_reader = csv.DictReader(file)
#                 wczytane_wydatki = []
#                 for wiersz in obiekt_reader:
#                     wiersz["kwota"] = float(wiersz["kwota"])
#                     wiersz.append(wczytane_wydatki)
#                 return wczytane_wydatki
#         except FileNotFoundError:
#             return []
#     else:
#         return []