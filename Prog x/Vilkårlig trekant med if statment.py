"""
Program som regner ut Arealet i en trekant med ved hjelp av Arealsetningen 

"""

import math

# Får de nødvednige opplysningene 
Enhet = str(input("Skriv Enhet?: "))
b = float(input("Side a=?: "))
c = float(input("Side b=?: "))
SinA = float(input("Side sinA/vinkelen=?: "))

# Regner ut Sinus til Vinkel A
SinA_kalkulert = math.sin(SinA)

# Tekst som setter svar i andre (ikke nødvdig) 
# viktig at det er str pga. hvis ikke kunne den ikke vært pluset sammen med 
kvadret = str("**2")

# Skjekker om vinkelen som er oppgitt er lik eller over 180 grader eller om den er 179 grader
if SinA >= 180: 
    print("Trenkanten går ikke")
elif SinA == 179:
    print("Trenkanten går ikke")
else:
    # Gjør de nødvednige utregenignen ved hjelp av arealsetningen 
    arealsetningen_svar = (1/2) * b * c * SinA_kalkulert
    # Skriver ut svaret + enheten
    print((round(arealsetningen_svar)),Enhet+kvadret)