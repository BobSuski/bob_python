# -*- coding: utf-8 -*-

# 1. czy liczba jest podzielna przez 3 lub 5 lub 7

liczba = 30

if liczba % 3 == 0:
    print("Liczba {} jest podzielna przez 3".format(liczba))
if liczba % 5 == 0:
    print("Liczba {} jest podzielna przez 5".format(liczba))
if liczba % 7 == 0:
    print("Liczba {} jest podzielna przez 7".format(liczba))
if (liczba % 3 != 0) and (liczba % 5 != 0) and (liczba % 7 != 0):
    print("Liczba {} nie jest podzielna przez 3, 5 ani 7".format(liczba))

# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok = 2018
if (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0):
    print("Rok {} jest przestępny".format(rok))
else:
    print("Rok {} nie jest przestępny".format(rok))


# 3. oblicz ocenę na podstawie progu procentowego

pp = 73

if (pp > 0) and (pp < 30):
    print('Twoja ocena to 1!!! Tragedia!!!')
elif (pp >= 30) and (pp < 50):
    print('Twoja ocena to 2!! Nie jest dobrze.')
elif (pp >= 50) and (pp < 70):
    print('Twoja ocena to 3! Popraw się.')
elif (pp >= 70) and (pp < 90):
    print('Twoja oceana to 4. Jest dobrze.')
elif (pp >= 90) and (pp < 100):
    print('Twoja oceana to 5! Bardzo dobrze.')
elif pp == 100:
    print('Twoja ocena to 6!! Świetnie.')
else:
    print("Błąd")

# 4. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

miesiac = "Październik"

miasiace_30 = ["Kwiecień", "Czerwiec", "Wrzesień", "Listopad"]

if miesiac == "Luty":
    print("Miesiąc ma 29 dni")
elif miesiac in miasiace_30:
    print("Miesiąc ma 30 dni")
else:
    print("Miesiąc ma 31 dni")

# 5. inupt - miesiąc oraz dzien (np. mar-18),
#   okreslic pore roku

wiosna = ["kwi", "maj"]
lato = ["lip", "sie"]
jesien = ["paz", "lis"]
zima = ["sty", "lut"]
mieszane = ["mar", "cze", "wrz", "gru"]

data = "paz-08"

miesiac = data[0:3]
dzien = int(data[-2:])

if miesiac in wiosna:
    print("Wiosna")
elif miesiac in lato:
    print("Lato")
elif miesiac in jesien:
    print("Jesień")
elif miesiac in zima:
    print("Zima")
elif miesiac in mieszane:
    if miesiac == "mar":
        if dzien >= 20:
            print("Wiosna")
        else:
            print("Zima")
    elif miesiac == "cze":
        if dzien >= 21:
            print("Lato")
        else:
            print("Wiosna")
    elif miesiac == "wrz":
        if dzien >= 22:
            print("Jesień")
        else:
            print("Lat")
    else:
        if dzien >= 21:
            print("Zima")
        else:
            print("Jesień")
else:
    print("Błąd")
    exit()

# 6. ruletka: otrzymawszy liczbę, sprawdź czy jest ona (np. 17R, 2B):
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

pole = "19B"

if pole[-1] == "B":
    print("Czarna")
else:
    print("Czerwona")

if int(pole[:-1]) < 18:
    print("Niska")
else:
    print("Wysoka")

if int(pole[:-1]) % 2 == 0:
    print("Parzysta")
else:
    print("Nieparzysta")

# 7. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

#temperatura = "36.6C"
temperatura = "97.88F"

skala = temperatura[-1]
wartosc = float(temperatura[:-1])

if skala == "C":
    print("Temperatura {} równa się {}F".format(temperatura, wartosc * (9/5) + 32))
else:
    print("Temperatura {} równa się {}C".format(temperatura, (wartosc - 32) * (5 / 9)))

# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

bok_a = 5
bok_b = 4
bok_c = 7

if (bok_a < bok_b + bok_c) and (bok_b < bok_a + bok_c) and (bok_c < bok_a + bok_b):
    print("Uda się narysować.")
    if bok_a == bok_b and bok_b == bok_c:
        print("Trójkąt równoboczny.")
    elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnoboczny")
else:
    print("Nie uda się narysować.")


### Listy
# 1. napisz program sumujący wszystkie elementy w liscie

lista = [5, 5, 10]
suma = 0
for element in lista:
    suma += element

print(suma)

# 2. znajdz najwiekszy / najmniejszy element w liscie

lista = [700, -5, 20, 4567, 7, 17, -800]
minimalna = lista[0]
maksymalna = lista[0]

for wartosc in lista:
    if wartosc < minimalna:
        minimalna = wartosc
    if wartosc > maksymalna:
        maksymalna = wartosc

print(minimalna, maksymalna)

# 3. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

slowa = ["lol", "kaboom", "foo", "kajak"]
szukane = 0
for slowo in slowa:
    if slowo[0] == slowo[-1]:
        szukane += 1

print(szukane)

# 4. program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]

for wartosc in lista_a:
    if lista_a.count(wartosc) == 1:
        print("Wartość {} występuje tylko raz.".format(wartosc))


# 5. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10,20,30,20,10,50,60,40,80,50,40]

for wartosc in lista_b:
    if lista_b.count(wartosc) > 1:
        lista_b.remove(wartosc)

print(lista_b)

# 6. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

for element in lista_a:
    if element in lista_b:
        print("Mamy co najmniej jeden wspólny element: {}".format(element))
        break

### Pętle

# 1. program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1
#    cena, zaplacono, reszta

cena = 2.7
zaplacono = 102
do_wydania = zaplacono - cena

wartosci = [5, 2, 1, 0.5, 0.2, 0.1]

for wartosc in wartosci:
    if do_wydania // wartosc > 0:
        reszta = ", ".join([str(wartosc)] * int(do_wydania // wartosc))
        print("{}".format(reszta))
        do_wydania = do_wydania - wartosc * int(do_wydania // wartosc)
        do_wydania = round(do_wydania,1)

# 2. Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####
#

poziomy = 7

for poziom in range(poziomy):
    print("{}{}{}".format(" "*(poziomy - poziom - 1), "#"*(poziom*2+1), " "*(poziomy - poziom - 1)))

# 3. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie

parz = 0
nie_parz = 0

for liczba in range(7,77):
    if liczba % 2 == 0:
        parz += 1
    else:
        nie_parz += 1

print(parz, nie_parz)

# 4. program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

for liczba in range(21):
    if liczba % 4 != 0:
        print(liczba)

# 5. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
print("fib------------------------------------")
n_minus_2 = 0
n_minus_1 = 1
n = 1

print(n_minus_2)
print(n_minus_1)

while n_minus_2 + n_minus_1 < 100:
    n = n_minus_2 + n_minus_1
    print(n)
    n_minus_2 = n_minus_1
    n_minus_1 = n
print("end_fib-------------------------------")

# 6. oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

czlowiek = 3
lata = []

if czlowiek > 2:
    lata.append(2)
    lata.append(czlowiek - 2)
else:
    lata.append(czlowiek)
    lata.append(0)

wiek = lata[0] * 10.5 + lata[1] * 4
print(wiek)