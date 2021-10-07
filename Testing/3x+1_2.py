from matplotlib.pyplot import grid, plot, show
import pylab

l1 = []
l2 = []
def algoritme(tall):
    n = float(tall) 
    tall = n 
    z = 0 
    print("")
    print("Tall:",n) 
    print("")

    while n > 1: 
            if n%2 == 0: 
                n =  n/2   
                z += 1 
                print(f"Nr.{z}     {n} ")
            elif n%2 == 1:
                n = 3*n +1
                z += 1
                print(f"Nr.{z}     {n} ")

    print("")
    print("Det tok", z-1, "forsøk og komme til 0 med tallet",tall )
    print("")
    l1.append(z-1)
    l2.append(tall)


algoritme(837799)

plot(l2,l1)
grid()
show()