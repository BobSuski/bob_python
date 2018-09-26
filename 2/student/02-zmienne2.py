zdanie = "Ala ma kota, kot ma Ale."
zdanie2 = ' Ale ja "wolę" psy!'
print(zdanie, end='____')
print(zdanie2)

print(zdanie + zdanie2)
print(zdanie, zdanie2)


moj_plik = "01-zmienne.py"

print(moj_plik)


print("1 ####################################################################################################")

x = ['a', 'b', 'c', 'd']
y = x
y.append('e')
print(x, y)

print("2 ####################################################################################################")

x = ['a', 'b', 'c', 'd']
y = x[:]
y.append('f')
print(x, y)
