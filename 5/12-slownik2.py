# -*- coding: utf-8 -*-

# w tej sytucji chcemy mieć słownik, w którym będziemy trzymać wpisy
# aby w słowniku trzymać cokolwiek, potrzebujemy klucz, po którym będziemy
# wyszukiwać daną wartość
# najczęściej kluczem będzie unikalny identyfikator danego rekordu - id
# liczba całkowita, bo najprościej jest nią operować


osoby = {}
print(osoby)

# w liście jest to trywialne - poszczególne słowniki są elementami
# kolejność, w której dodaliśmy element jest ważna
rekordy = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
{"imie": "Anna", "nazwisko":"nowak", "wiek":23},
{"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
{"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]

# nasza baza słownikowa jest uzupełniana elementami
# tworzymy unikatowy klucz - indeks z listy
for indeks, rekord in enumerate(rekordy):
    osoby[indeks] = rekord

print(osoby)

print(len(osoby))

# jeśli chcielibyśmy kontynuować dodawanie wartości do bazy
# to musimy zastanowić się w jaki sposób kontynuować dodawanie,
# tak aby klucze były unikalne
najw_indeks = max(osoby.keys())
print(najw_indeks)

osoby[najw_indeks+1] = {"imie": "Anna", "nazwisko":"nowak", "wiek":23}


