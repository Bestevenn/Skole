
from pylab import * 
import matplotlib.pyplot as plt

print("")
print("Skriv ført in antall tall som du vil ha")
print("")
Antall_input = int(input("antall: "))
L_x = []
L_y = []


for n in range(Antall_input):
    tall = float(input("x tall:"))
    L_x.append(tall)
print("")
print("")
for n in range(Antall_input):
    tall = float(input("y tall?:"))
    L_y.append(tall) 


print(L_x,L_y)
navn_på_graf = input("Skriv navnet på grafen: ")

plot(L_x, L_y)
xlabel("x-akse")
ylabel("y-akse")
title(navn_på_graf)
grid()
show()


# 