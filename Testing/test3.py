 
 
 
 # Definerer funksjonen f(x) som vi skal finna nullpunktet til
# Funksjonen mÃ¥ vera kontinuerlig pÃ¥ intervallet [a,b]
def f(x):
    return  k # Andregradsfunksjon med rÃ¸tene x = 2 og x = 10

e = 0.00001 # Toleranse for funksjonsverdi
N = 1000000 # Maks antal iterasjonar

a = float(input("Skriv a: ")) # Nedre grense for intervallet
b = float(input("Skriv b: ")) # Ã˜vre grense for intervallet

if f(a)*f(b) < 0:
    n = 0       # antall iterasjonar
    m = (a+b)/2 # Finn m, midtpunktet mellom a og b.
    while abs(f(m)) > e and n < N:
        n +=1
        
        if f(m) == 0:       # Vi har funne eit nullpunkt og kan avslutta
            break           # break gjer at vi gÃ¥r ut av lÃ¸kka
        elif f(m)*f(b) < 0: # Det er minst eit nullpkt mellom m og b,
            a = m           # sÃ¥ vi flytter a til midten
        else:               # Det er minst eit nullpkt mellom a og m,
            b = m           # sÃ¥ vi flytter b til midten
            
        m = (a+b)/2         # Reknar ut m igjen
        
    print("Nullpunktet er:",m)
    print("Antal iterasjonar:",n)
else:
    print("Feil: f(a) og f(b) mÃ¥ liggja pÃ¥ kvar si side av x-aksen!")