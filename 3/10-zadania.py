### Listy
# 1. napisz program sumujący wszystkie elementy w liscie
#SOLVED
if False:
    sum=0
    for i in [1,2,3,4,5,6,7,9]:
        sum+=i
    print(sum)

# 2. znajdz najwiekszy / najmniejszy element w liscie
#SOLVED
if False:
     elements=[11,18,17,16,15,14,13,12,11]
     print(elements)
     elements.sort()
     print(elements)
     print("Min={0}, Max={1}".format(elements[0],elements[len(elements)-1]))


# 3. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2
#################################################3
#SOLVED

if False:
    elements2=['abc', 'xyzx', 'aba', '1221']
    num=0

    for i in elements2:
        if i[0]==i[len(i)-1]:
            num+=1
    print(num)

# 4. program znajdujacy wartosci, ktre wystepuja tylko raz
#SOLVED
if False:
    lista_a = [10,20,30,20,10,50,60,40,111,80,50,40]
    #lista_a = [10,20,30,20,10,50,60,40,80,50,40]



    seq=0
    for i in lista_a:
        if i not in lista_a[:seq-1] and i not in lista_a[seq+1:]:
            print(i)
        seq+=1

# 5. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
#SOLVED
if False:
    lista_b = [10,20,30,20,10,50,60,40,80,50,40]
    print("Oryginal {}".format(lista_b))

    lista_b.sort()
    prev=lista_b[0]

    for i in lista_b[1:]:
        if prev==i:
                lista_b.remove(i)
        else:
            prev=i
    print("After dedup {}".format(lista_b))

#with set
if False:
    lista_b = [10,20,30,20,10,50,60,40,80,50,40]
    print(set(lista_b))

# 6. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True
#SOLVED
if False:
    lista_c = [10,20,30,20,10,50,60,40,80,50,40]
    lista_d = [1,2,3,4,50,6,50,7]

    for i in lista_c:
        if lista_d.__contains__(i):
            print(True)
            break

#with style
if False:
    lista_c = [10,20,30,20,10,50,60,40,80,50,40]
    lista_d = [1,2,3,4,51,6,510,7]
    set_c=set(lista_c)
    set_d=set(lista_d)
    if set_c.intersection(set_d) != set():
        print(True)

### Pętle

# 1. program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1
#    cena, zaplacono, reszta
#SOLVED
if False:
    def kasa(cena, zaplacono):
        reszta=zaplacono-cena
        print("cena={}, zaplacono={}, reszta={}".format(cena,zaplacono,reszta))
        print("Wydaje reszte")
        monety=[5,2,1,0.5,0.2,0.1]
        resztaList=[]
        while round(reszta,1)>0:
            found=False
            for i in monety:
                if reszta>=i:
                    print("znalazlem pasujaca monete {}".format(i))
                    resztaList.append(i)
                    reszta=reszta-i
                    print("Zostalo {}".format(reszta))
                    found=True
                    break
            if not found:
                break
        print("Wydana reszta {}".format(resztaList))

    print("START")
    kasa(1.8,12.7)
    print("END")


# 2. Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####
########
#SOLVED
if False:
    def pyramid(size):
        i=1
        while i<size:
            print(' '*(size-i)+'#'*(i-1)+'#'+'#'*(i-1))
            i=i+1

    pyramid(10)

# 3. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie
#SOLVED
if False:
    def counter(list):
        even=0
        odd=0
        for i in list:
            if i % 2:
                even+=1
            else:
                odd+=1
        print ("Even:{0}, Odd:{1}".format(even,odd))

    counter([1,2,3,4,11,32,322,19,17])

# 4. program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
#SOLVED
if False:
    for i in range(21):
        print(i,end=',') if i % 4!=0 else print(end='')

# 5. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
#SOLVED
if False:
    def fibonacci():
        x = 0
        y = 1

        def do_fib():
            nonlocal x, y
            if x == 0 and y == 1:
                print(x)
                print(y)
            p = x + y
            x = y
            y = p
            print(p)

        return do_fib

    f2 = fibonacci()
    [f2() for _ in range(100)]


# 6. oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata  15=2+2+x*4
#SOLVED
if False:
    def HumanAge2DogAge(human):
        dogAge=0
        humanAge=human
        #first two years processing
        for i in range(2):
            if humanAge>=1:
                dogAge=dogAge+10.5
            elif humanAge>=0:
                dogAge=dogAge+humanAge*10.5
            humanAge=humanAge-1
            if humanAge<0:
                break

        if humanAge>0:
            dogAge=dogAge+humanAge*4
        print(dogAge)

    HumanAge2DogAge(15)
