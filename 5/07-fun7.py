# -*- coding: utf-8 -*-

imie = "Ola"

def wypisz_imie():
    global imie
    duze_imie = imie.upper()
    return duze_imie


print(wypisz_imie())
