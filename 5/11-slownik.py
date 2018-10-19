# -*- coding: utf-8 -*-

elementy = { 1:"ola", 0:"ala",  2:"ela" }

print(elementy)
print(elementy[1])

slownik = {"imie": "Adam", "nazwisko":"kowalski", "wiek":32}

# klucze
print(slownik.keys())
# wartości
print(slownik.values())

# items() zwraca parę - klucz oraz wartość
for klucz, wartosc in slownik.items():
    print("Klucz: {} ma wartość {}".format(klucz, wartosc))

if "adres" in slownik.keys():
    print("Adres dostępny")
else:
    print("adres niedostępny")

print(slownik)
# jeśli przypiszemy wartość do nieistniejącego klucza
# to zostanie on utworzony
slownik["adres"] = "Gdańsk"
print(slownik)
# jeśli przypisujemy wartość do istniejącego klucza
# to zmieniamy/nadpisujemy jego wartość
slownik["adres"] = "Gdynia"
print(slownik)
