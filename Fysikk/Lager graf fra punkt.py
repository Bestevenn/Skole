
from pylab import * 


Antall_input = int(input("hvor mange tall?: "))
L_x = []
L_y = []


for n in range(Antall_input):
    tall = float(input("x Tall?:"))
    L_x.append(tall)
print("")
print("")
for n in range(Antall_input):
    tall = float(input("y Tall?:"))
    L_y.append(tall) 


print(L_x,L_y)


plot(L_x, L_y)
grid()
show()