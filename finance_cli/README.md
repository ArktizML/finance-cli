# 💰 Personal Finance CLI (v1.0)

Prosty, ale w pełni funkcjonalny **terminalowy menedżer wydatków** napisany w Pythonie.  
Aplikacja pozwala na dodawanie, edytowanie, filtrowanie i analizowanie wydatków bezpośrednio z poziomu konsoli.  
Dodatkowo generuje **raporty CSV** i **wykresy wydatków** w oparciu o dane użytkownika.

---

## 📌 Funkcjonalności

✅ Dodawanie nowych wydatków (data, kategoria, kwota)  
✅ Edycja istniejących wydatków  
✅ Filtrowanie wydatków po kategoriach  
✅ Sortowanie po kwocie, dacie lub kategorii  
✅ Wyświetlanie statystyk  
✅ Eksport danych do pliku `.csv`  
✅ Automatyczne generowanie wykresu słupkowego z wykorzystaniem `matplotlib`  
✅ Trwałe zapisywanie danych w pliku `data.json`

---

## 🗂️ Struktura projektu
```bash
finance_cli/
│
├── core/
│ ├── expenses.py # logika dodawania, edycji, filtrowania i statystyk wydatków
│ ├── storage.py # zapisywanie i odczyt danych z pliku JSON
│ ├── utils.py # pomocnicze funkcje (np. generowanie wykresów, eksport CSV)
│ ├── math_utils.py # funkcje statystyczne (średnia, mediana, odchylenie standardowe)
│
├── data/
│ └── data.json # zapisane dane użytkownika
│
├── main.py # główny plik aplikacji CLI
├── README.md # dokumentacja projektu
└── requirements.txt # wymagane biblioteki
```
---

## ⚙️ Instalacja i uruchomienie

1. **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/ArktizML/finance_cli.git
    cd finance_cli

2. **Utwórz środowisko wirtualne (zalecane):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows

3. **Zainstaluj biblioteki:**
    ```bash
    pip install -r requirements.txt

4. **Uruchom aplikację:**
```bash
python main.py
```

## 🧮 Przykładowe dane
```bash
Data	Kategoria	Kwota
2025-11-06 12:16:18	woda	15.0
2025-11-06 12:16:43	kebab	30.0
2025-11-06 12:16:48	leki	100.0
2025-11-06 12:38:18	fryzjer	50.0
```
## 📊 Statystyki i wykresy
Aplikacja automatycznie oblicza:
- Suma wszystkich wydatków
- Średnia kwota
- Największy i najmniejszy wydatek
- Sumy wydatków według kategorii
- Po wybraniu opcji 10. Pokaż aktualny wykres wydatków — otwiera się okno z wykresem słupkowym.
- Przy eksporcie danych (opcja 9) tworzony jest również plik wykres_<data>.png.

## 📁 Eksport danych
Po wybraniu opcji 9. Eksportuj dane do CSV, aplikacja tworzy plik:

raport_<data>.csv

Przykład zawartości:

```bash
data,kategoria,kwota
2025-11-06 12:16:18,woda,15.0
2025-11-06 12:16:38,cola,20.0
2025-11-06 12:16:43,kebab,30.0
2025-11-06 12:16:48,leki,100.0
```

## 🧠 Technologie i biblioteki
- Python 3.10+
- matplotlib – generowanie wykresów
- tabulate – ładne tabele w konsoli
- json – zapis i odczyt danych
- csv – eksport raportów
- datetime, math – obsługa dat i obliczenia statystyczne

## 🏁 Status projektu
✅ Zakończony – wersja 1.0.0
Projekt archiwalny, pozostawiony jako przykład czystego kodu proceduralnego w Pythonie.
Docelowo zastąpiony będzie nową wersją napisaną obiektowo (OOP) z użyciem API i modułu AI.

## 👨‍💻 Autor
Mateusz Lewicki [ArktizML]
Projekt stworzony w ramach nauki Pythona i dobrych praktyk w pisaniu kodu CLI.

## 📜 Licencja
Ten projekt jest udostępniany na licencji MIT – możesz go dowolnie modyfikować i rozwijać.
