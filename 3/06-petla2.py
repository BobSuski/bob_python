nieprawidlowe = True

while nieprawidlowe:
    nazwisko = input("Podaj nazwisko drukowanymi literami lub Q aby zakończyć: ")

    if nazwisko.upper() == 'Q':
        print("Do widzenia.")
        quit()
    elif nazwisko.isalpha():
        if nazwisko.isupper():
            nieprawidlowe = False

print("Gratulacje, jesteś zarejestrowany.")
