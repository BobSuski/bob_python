# -*- coding: utf-8 -*-

def dodaj_imie(imie, baza=None):
    """Dodaje imie do bazy, jesli baza nie
    istnieje, tworzy nowa baze
    (str, [list]) -> list"""

    if baza == None:
        baza = []

    imie= imie.upper()
    baza.append(imie)
    return baza

anglicy = dodaj_imie("john")
print(anglicy)
framcuzi = dodaj_imie("antoin")
print(framcuzi)
rosjanie = dodaj_imie("masza")
print(rosjanie)

rosjanie = dodaj_imie("miś", rosjanie)

print(rosjanie)