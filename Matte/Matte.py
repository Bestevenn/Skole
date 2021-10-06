def f(x):
    return (2*x**2-18)/(x-3)

delta_x = 0.1


for n in range(10):
    print((2+delta_x), "   ", f(2+delta_x))
    delta_x = delta_x * 0.1 



