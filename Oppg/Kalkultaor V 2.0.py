import math
import time
import os
from functools import reduce
from datetime import date
from sys import platform

# skjekker om pyperclip er installert
try:
    import pyperclip
except:
    print("")
    print("pyperclip er ikke installert")
    print("Installer med pip3/pip install pyperclip https://pypi.org/project/pyperclip/")
    time.sleep(2)


Dato = date.today()
Fortsett = True # deffinerer Fortsett, gjør det mulig for oss å bryte løkken etterpå
Filnavn_og_plasering = print()
# lager en funksjon som vi kan kalle på når som helst
# den skjekker hvilket oppreastivsystem du er på og rensker terminalen med riktig komanndo
def skjekke_os():
    if platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
    elif platform == "linux":
        os.system("clear")
    else:
        print()

Alle_svar = []  #lager en tom liste som vi kan legge svarene inni


while Fortsett:
    # Finner ut hvilken regneopperasjon du skal bruke
    regneopprasjon = input("Hvilken regneopperasjon vil du bruke +/-/* og s for stopp: ")

    # se "*" for full forklaring 
    if regneopprasjon == "+":
        hvormange_a = int(input("hvor mange tall?: "))
        list_med_tall_a = []
        for n in range(hvormange_a):
            tall1 = int(input("hvilken tall hvil du plusse?: "))
            list_med_tall_a.append(tall1)
        skjekke_os()
        print("")
        svar_a = sum(list_med_tall_a)
        print("Ans:",svar_a)
        Alle_svar.append(svar_a)
        print("")
        copy = input("vil du kopieret svaret ditt til utklippsavtalen y/n ?: ")
        if copy == "y":
                pyperclip.copy(svar_a)
                skjekke_os()
        else:
                skjekke_os()
    # se "*" for full forklaring 
    elif regneopprasjon == "-":
        hvormange_b = int(input("hvor mange tall?: "))
        list_med_tall_b = []
        for n in range(hvormange_b):
            tall1 = int(input("hvilken tall hvil du subtraherer?: "))
            list_med_tall_b.append(tall1)
        skjekke_os()
        print("")
        # vet ikke helt hvordan den fungere fant den på nettet 
        # men det subtraherer alle tallene
        svar_b = reduce(lambda x, y: x - y, list_med_tall_b)
        print("Ans:",svar_b)
        Alle_svar.append(svar_b)
        print("")
        copy = input("vil du kopieret svaret ditt til utklippsavtalen y/n ?: ")
        if copy == "y":
                pyperclip.copy(svar_b)
                skjekke_os()
        else:
                skjekke_os()
    elif regneopprasjon == "*":                          # skjekker inputen for *
        hvormange_c = int(input("hvor mange tall?: "))   # finner ut hvor mange ganer løkkken skal kjøre
        list_med_tall_c = []                             # lager en tom liste
        for n in range(hvormange_c):                     # lager en for loop, grunnet at vi skal kjøre den et spesefikt antall ganger 
            tall1 = int(input("hvilken tall hvil du gange?: ")) # spør etter hvilken tall som skal ganges
            list_med_tall_c.append(tall1)                 # putter tallet som skal ganges i listen 
        skjekke_os()                                      # rensker terminalen med en funksjon
        print("")      
        svar_c = math.prod(list_med_tall_c)                # tar produket av listen med tall 
        print("Ans:", svar_c)                              # skriver ut svare
        Alle_svar.append(svar_c)                           # lagrer svaret i en liste
        print("") 
        copy = input("vil du kopieret svaret ditt til utklippsavtalen y/n ?: ")  # spør om du vi kopiere svaret til utklippsavtalen
        if copy == "y":
                pyperclip.copy(svar_b)                      # komierer svatet med pyperclip.copy
                skjekke_os()
        else:
                skjekke_os()                 
        # gjør det mulig å renske terminalen når som helst
    elif regneopprasjon == "clear":
        skjekke_os()
        # gjør det mulig å stoppe loopen
    elif regneopprasjon == "s":
        Fortsett = False
        # retter deg dersom du skriver feil
    else:
        print("Error")
        print("")
        time.sleep(0.5)
        print("Restarting")
        time.sleep(0.5)
        print("3")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("1")
        time.sleep(0.5)
        skjekke_os()

    


print_alle_svar = input("vil du printe alle svar y/n: ")
if print_alle_svar == "y":
    print("")
    print("Dine svar:", Alle_svar)
    print("")
    Lagre = input("vil du lagre svarerene dine i en fil y/n: ")
    if Lagre == "y":
        print("")
        print("NB! python må ha tilgang til mappesystmet og filtype må være med eks: .txt ")
        print("")
        navn_fil = str(input("hva skal filen hete?: "))
        svar_lagre = str(input("Hvor vil du lagre filen?: "))
        print("")
        Filnavn_og_plasering = svar_lagre+navn_fil
        print("")
        with open(Filnavn_og_plasering, "w+") as f:
            print(f"Dine svar fra {Dato} = ",Alle_svar, file=f)
else:
    print()



skjekke_os()
print("")
print("svaret ble skrevet til", Filnavn_og_plasering)
print("")
print("parent is shutting down, bye...")
print("")   

