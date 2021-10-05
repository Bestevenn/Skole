
import math
import time
import os
from functools import reduce
import pyperclip
from sys import platform





alle_svar = [] 


def skjekke_os():
    if platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
    elif platform == "linux":
        os.system("clear")
    else:
        print()



def kalklulator(regne):
        list_med_tall_a = []
        hvormange = int(input("hvor mange tall?: "))
        for n in range(hvormange):
            tall1 = int(input("hvilken tall hvil du bruke?: "))
            list_med_tall_a.append(tall1)
        skjekke_os()
        print("")
        svar_a = regne(list_med_tall_a)
        print("Ans:",svar_a)
        alle_svar.append(svar_a)
        print("")
        copy = input("vil du kopieret svaret ditt til utklippsavtalen y/n ?: ")
        if copy == "y":
                pyperclip.copy(svar_a)
                skjekke_os()
        else:
                skjekke_os()

Fortsett = True

while Fortsett:
    # Finner ut hvilken regneopperasjon du skal bruke
    regneopprasjon = input("Hvilken regneopperasjon vil du bruke +/* og s for stopp: ")
    if regneopprasjon == "+":
        kalklulator(sum)
    elif regneopprasjon == "*":
        kalklulator(math.prod)
    # devide all
    elif regneopprasjon == "s":
        Fortsett = False
    else:
        print("du skrev noe feil")
    
skjekke_os()
print("")
printe_svar = input("Vil du printe alle svar y/n ?: ")
if printe_svar == "y":
    print(alle_svar)
else:
    print()

print("ferdig")
print("")
