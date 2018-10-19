# -*- coding: utf-8 -*-

if False:
    def do_nothing():
        pass

    do_nothing()


    def print_my_name():
        print("Hello, my name is Damian!")
        print("Jak się masz")


    print_my_name()
    print_my_name()
    print_my_name()

    for i in range(100):
        print_my_name()


def func1(x):
    if x:
        print("func1: {}".format(x))
        func2(x-1)

def func2(x):
    if x:
        print("func2: {}".format(x))
        func1(x-1)

func1(5)

#func2(10)