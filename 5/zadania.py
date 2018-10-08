#SOLVED
if False:
    def pyramid(start,end):
        ''' stworzyć funkcję która po otrzymaniu dwóch liczb będzie drukować niepełną piramidę. Dla liczba 5 i 7:'''
        i=start
        while i<end:
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

