import math

Enhet = str(input("Skriv Enhet?: "))
b = float(input("Side a=?: "))
c = float(input("Side b=?: "))
SinA = float(input("Side sinA=?: "))

SinA_kalkulert = math.sin(SinA)

# Re
Arealsetningen_svar = (1/2) * b * c * SinA_kalkulert

# Skriver ut svaret
print((round(Arealsetningen_svar)),Enhet)



