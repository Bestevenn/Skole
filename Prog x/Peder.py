# Peder
# program som rengner ut Areal av en sikel og ikke godtar negative svar
Fortsett = True # Setter for Fortsett til True, det gjør at løkken går 
while Fortsett: # lager en While løkke 
    G, h = float(input("Grunnlinje: ")), float(input("Høyde: ")) # spør om hva grunnnlinje og høyde er
    if G < 0 or h < 0: # skjekker om svaret er mindre enn 0
        print("") # lager litt mellom, for estetikken i koden
        print("Kan ikke ha negativ Grunnlinje eller høyde") # sier til brukeren at man ikke kan ha negativt svar
        print("") # lager litt mellom, for estetikken i koden
    else: # sier at hvis ikke det første er sant så skal den gjøre dette istendenfor
        Areal = (G*h)/2 # Regner ut arealet 
        print("Arealet til trenkanten = ", Areal) # skriver ut arealet 
        Fortsett = False # bryter løkken

