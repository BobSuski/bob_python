
imie = "Damian"
Imie = "Piotr"
nazwisko = "Melniczuk"
wiek = 33

print(imie)
print(imie[3:5])
print(3 + 7)
print(3 == 5)
print(imie.lower())

print(imie.count('a'))

print(imie + ' ' + nazwisko + 'ma' + str(wiek) + 'lata.')

print("{} {} ma {} lata.".format(imie, nazwisko, wiek/2))
print("{1} {0} ma {2} lata".format(imie, nazwisko, wiek))



# Więcej o printach: https://pyformat.info/

print("####################################################################################################")

#None
n = None
print(n)

print("this is string".capitalize().__len__())

print("{1} {0} ma {2} lata".format(imie, nazwisko, wiek)+"{3}")


print("{1} {0} ma {2} lata {{3}}".format(imie, nazwisko, wiek)+"{3}")


#try:
#    print(imie2.lower())
#except Exception as e:
#    print(e)
#    exit(1)

