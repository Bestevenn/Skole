
from pylab import * 
import matplotlib.pyplot as plt


Antall_input = int(input("numbers: "))
L_x = []
L_y = []


for n in range(Antall_input):
    tall = float(input("x numbers:"))
    L_x.append(tall)
print("")
print("")
for n in range(Antall_input):
    tall = float(input("y numbers?:"))
    L_y.append(tall) 


print(L_x,L_y)


plot(L_x, L_y)
grid()
show()