# =============== IMPORTY ===============
from datetime import datetime
import json, os
import expenses as ex
from utils import *
from main import wydatki

# =============== FUNKCJE PODSTAWOWE ===============
def wczytaj_z_pliku():
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    else:
        return []
            

def zapisz_do_pliku():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(wydatki, file, ensure_ascii=False, indent=4)
