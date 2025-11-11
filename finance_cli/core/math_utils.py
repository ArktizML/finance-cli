import math

def srednia(lista):
    suma = 0
    for liczba in lista:
        suma+=int(liczba)

    return suma/len(lista)


def mediana(lista):
    lista = sorted(lista)
    mediana = 0
    if len(lista) % 2 != 0:
        mediana = (math.floor(len(lista)) / 2)
        return lista[int(mediana)]
    else:
        mediana = (int(lista[len(lista) / 2]) + int(lista[(len(lista) / 2) + 1])) / 2
        return mediana

def odchylenie_std(lista):
    srednia_wynik = srednia(lista)
    x = []
    for liczba in lista:
        x.append((int(srednia_wynik)-liczba)**2)
    srednia_x = srednia(x)
    return math.sqrt(srednia_x)