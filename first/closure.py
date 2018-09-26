def powers_2(initial):
    p = initial

    def do_pow():
        nonlocal p
        p = p + p
        print(p)

    return do_pow


def powers_2_lambda(initial):
    p = initial

    def do_pow():
        nonlocal p
        p = p + p
        print(p)

    return do_pow


def fibonacci():
    x = 1
    y = 1

    def do_fib():
        nonlocal x, y
        if x == 1 and y == 1:
            print(x)
            print(y)
        p = x + y
        x = y
        y = p
        print(p)

    # do_fib()
    return do_fib


def f_lambda(n):
    return lambda a: a + n


print("###################")

f1 = powers_2(1)
f1()
f1()

print("###################")

f2 = fibonacci()
f2()
f2()
f2()
f2()

print("###################")

f3 = f_lambda(10)
print(f3(5))
