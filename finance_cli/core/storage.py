# =============== IMPORTY ===============
from datetime import datetime
import json, os
import csv

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

    wczytaj_z_pliku()
    
    with open(DATA_PATH, "w", newline="", encoding="utf-8") as file:
        obiekt_writer = csv.DictWriter(file, fieldnames=["data", "kategoria", "kwota"])
        obiekt_writer.writeheader()       
        for wydatek in wydatki:
            obiekt_writer.writerow(wydatek)
    print("✅ Dane wyeksportowane do export.csv")

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