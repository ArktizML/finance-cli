# =============== IMPORTY ===============
from datetime import datetime
import json, os
from core import storage as st
from core import expenses as ex
from tabulate import tabulate # type: ignore
import matplotlib.pyplot as plt

# ============== FUNKCJE ================
def rysuj_wykres(wydatki):
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
    plt.show()