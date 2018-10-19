# -*- coding: utf-8 -*-

def wypisz_dane(imie, nazwisko, kurs="Python", il_dni=15):
    print("Kursant {} {}, kurs: {} trwa {} dni.".format(imie, nazwisko, kurs, il_dni))


wypisz_dane("Damian", "G")
wypisz_dane("Anna", "Kowalska", "Java")
wypisz_dane("Adam", "Nowak", "JS", 60)

wypisz_dane("Marta", "K", il_dni=10)

wypisz_dane(il_dni=20, imie="Jan", nazwisko="Pietrzak", kurs="Java")