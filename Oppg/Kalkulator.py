# while loop 
import time
import math
import os

# Setter while løkken til sann slik at den ikke bryter
Fortsett = True

while Fortsett:
    # Finner ut hvilken regneopperasjon du skal bruke
    regneopprasjon = input("Hvilken regneopperasjon vil du bruke +/-/*/(/)/sqrt og s for stopp: ")
    # Skjekker input for hvilken opperasjon, så utfører den oppraasjonen og skriver svaret:
    if regneopprasjon == "+":
        talla1 = int(input("skriv første tall: "))
        talla2 = int(input("skriv andre tall: "))
        svar_a = talla1+talla2
        os.system("clear")
        print("")
        print("Ans:",svar_a)
        print("")
    elif regneopprasjon == "-":
        tallb1 = int(input("skriv første tall: "))
        tallb2 = int(input("skriv andre tall: "))
        svar_b = tallb1+tallb2
        os.system("clear")
        print("")
        print("Ans:",svar_b)
        print("")
    elif regneopprasjon == "*":
        tallc1 = int(input("skriv første tall: "))
        tallc2 = int(input("skriv andre tall: "))
        svar_c = tallc1*tallc2
        os.system("clear")
        print("")
        print("Ans:",svar_c)
        print("")
    elif regneopprasjon == "/":
        talld1 = int(input("skriv første tall: "))
        talld2 = int(input("skriv andre tall: "))
        svar_d = talld1/talld2
        os.system("clear")
        print("")
        print("Ans:",svar_d)
        print("")
    elif regneopprasjon == "sqrt":
        talle = int(input("hvilken tall vil du ta kvadratroten av?: "))
        svar_e = math.sqrt(talle)
        os.system("clear")
        print("")
        print("Ans:",svar_e)
        print("")
    elif regneopprasjon == "clear":
        os.system("clear")
    elif regneopprasjon == "s":
        Fortsett = False
    else:
        print("")
        print("Skriv en riktig regneopperasjon")
        print("")
        os.system("clear")
        time.sleep(0.5)
    

# Skriver ut noe etter du har brøte løkken
# time.sleep gjør slik at programmet tar en pause i så og så mange sekunder
os.system("clear")
time.sleep(0.5)
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(1)
Ferdigprogram = str("parent is shutting down, bye...") 
print(Ferdigprogram)
time.sleep(1)
