from matplotlib.pyplot import grid, plot, show
import pylab

l1 = []
l2 = []

n = float(837799) 
tall = n 
z = 0 
print("")
print("Tall:",n) 
print("")
    
while n > 1: 
    if n%2 == 0: 
        n =  n/2   
        z += 1 
        l2.append(n)
        print(f"Nr.{z}     {n} ")
    elif n%2 == 1:
        n = 3*n +1
        z += 1
        print(f"Nr.{z}     {n} ")
        l2.append(n)
    

    
    print("")
    print("Det tok", z-1, "forsøk og komme til 0 med tallet",tall )
    print("")
    

for p in range(z+1):
    l1.append(p)


plot(l1,l2)
grid()
show()