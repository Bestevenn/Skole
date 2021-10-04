

L = []
antall_tall = 100 
for n in range(antall_tall):
    if (n%3 == 0):    # % skjekker om resten er like null altså eks. f.eks 8/4  = 2 dermerd null i 7/2 går ikke opp dermed 1 i rest
        L.append(n)
    elif (n%5 == 0):
        L.append(n)
    else:
        print()


print("Alle tall",L)
svar = sum(L)
print(svar)
    



