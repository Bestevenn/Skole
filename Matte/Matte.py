def f(x):
    return (2*x**2-18)/(x-3)

delta_x = 0.1


for n in range(15):
    print((3+delta_x), "   ", f(3+delta_x))
    delta_x = delta_x * 0.1 



