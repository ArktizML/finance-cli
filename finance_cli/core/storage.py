# =============== IMPORTY ===============
from datetime import datetime
import json, os

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
