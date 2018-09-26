# https://docs.python.org/3.5/library/functions.html#round

a = 0.1 + 0.1 + 0.1
b = 0.3
wynik = a == b

print(wynik)
print("a = {} , b = {}".format(a,b))

liczba_a = round(45.43535)
print(liczba_a)
print(round(45.4563))
print(liczba_a % 8)

wynik = round(a, 3) == round(b, 3)
print(wynik)

