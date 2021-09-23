 
import math





a = float(input("a?: "))
b = float(input("b?: "))
c = float(input("c?: "))

"""
x1 = (-b+math.sqrt(b**2-4*a*c))/2*a))
x2 = (-b-math.sqrt(b**2-4*a*c))/2*a))
"""

d = (b**2-4*a*c)

if d < 0:
    print("Ingen løsning")
elif d == 0:
    x = (-b) / (2*a)
    print("en løsning = ", x)
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(round(x1),round(x2))
   

