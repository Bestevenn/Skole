# Dette programmet finner avstand mellom to punkter i en graf

import math

# inputene dine 
x1 = float(input("x1?: ")) 
x2 = float(input("x2?: "))
y1 = float(input("y1?: "))
y2 = float(input("y2?: "))

# finner legendene vi skal bruke i pytagoras formlen
y_lengde = (y2 - y1)
x_lengde = (x2 - x1)

# skriver pytagoras formelen 
avstand_mellom_punkt = (math.sqrt(x_lengde**2 + y_lengde**2))

# printer svaret 
svar = ("Avstanden mellom de to punktene er: ", avstand_mellom_punkt)
print(svar)
print("x lengden var: ", x_lengde)
print("x lengden var: ", y_lengde)