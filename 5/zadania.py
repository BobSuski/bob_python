#SOLVED
if False:
    def pyramid(start,end):
        ''' stworzyć funkcję która po otrzymaniu dwóch liczb będzie drukować niepełną piramidę. Dla liczba 5 i 7:'''
        i=start
        while i<=end:
            print(' '*(end-i)+'#'*(i-1)+'#'+'#'*(i-1))
            i=i+1

    pyramid(start=5,end=7)


#SOLVED
if False:
    import math
    def primeChecker(number):
        message="{} is prime".format(number);
        ln=(round(math.log1p(number))) #as far as my mind is not lying me it was enough to check only up to ln :)
        for div in range(ln):
            if number%(div+2) ==0:
                message="{} is not prime. Divisor={}".format(number,div+2)
                break
        print(message)

    [primeChecker(x) for x in range(100000)]

if False:
    def dodaj_imie(imie, imiona=[]):
        imiona.append(imie)
        return imiona

    print(dodaj_imie('Ala')) #[“Ala”]

    print(dodaj_imie('Ola')) # [“Ala”, “Ola”]
    print(dodaj_imie('Ewa')) # [“Ala”, “Ola”, “Ewa”]

if False:
    imiona=[]
    if True:
        def dodaj_imie(imie):
            imiona.append(imie)
            print(imiona)

    dodaj_imie('Ala') #[“Ala”]
    dodaj_imie('Ola') # [“Ala”, “Ola”]
    dodaj_imie('Ewa') # [“Ala”, “Ola”, “Ewa”]

    print(imiona)

if False:
    def dodaj_imie(imie, imiona=[]):
        imiona.append(imie)
        return imiona

    x=dodaj_imie('Ala') #[“Ala”]
    x=dodaj_imie('Ola') # [“Ala”, “Ola”]
    x=dodaj_imie('Ewa') # [“Ala”, “Ola”, “Ewa”]

    print(x)

if False:
    def dodaj_imie(imie, imiona=[]):
        imiona.append(imie)
        print(imiona)

    dodaj_imie('Ala') #[“Ala”]
    dodaj_imie('Ola') # [“Ala”, “Ola”]
    dodaj_imie('Ewa') # [“Ala”, “Ola”, “Ewa”]


if False:
    def dodaj_imie(imie, imiona=[]):
        imiona.append(imie)
        print(imiona)

    dodaj_imie('Ala') #[“Ala”]
    dodaj_imie('Ola') # [“Ala”, “Ola”]
    dodaj_imie('Ewa') # [“Ala”, “Ola”, “Ewa”]

if False:
    def dodaj_imie(y, x=0):
        x=x+y
        print(x)

    dodaj_imie(1) #[“Ala”]
    dodaj_imie(2) # [“Ala”, “Ola”]
    dodaj_imie(3) # [“Ala”, “Ola”, “Ewa”]

if True:
    def fun(*el):
        for i in el:
            print(i)

    fun(1,2,3,4)