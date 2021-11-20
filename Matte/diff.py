import math


def f(x):
    return x**2


def derivert(f, a, delta_x):
    return(f(a+delta_x)-f(a-delta_x))/2*(delta_x)


for n in range(1, 16):
    test = 10**-n
    dx = derivert(f, 2, test)
    avrund = round(dx)
    diff = avrund - dx
    print("ƒ(2)=", dx, "differanse =", diff)
