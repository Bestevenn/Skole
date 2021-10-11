import math


# deffinerer en funkjson som vi kan kalle når som helst i progammret
def algoritme(tall):
    n = float(tall) # setter n som det tallet du skal utføre algoritmen i 
    tall = n # setter tall til n slik at vi kan printe det første tallet senere
    z = 0 # setter z til 0. dette er basisen for å få antall forsøk og linjer med
    print("")
    print("Tall:",n)
    print("")

    while n > 1: # loopen skal gå så lenge n er større en 0
            if n%2 == 0: # utfører den regneopprasjonen dersom restten av n/2 er lik 0
                n =  n/2   # setter verdien til n = n delt på 2
                z += 1 
                print(f"Nr.{z}     {n} ")
            elif n%2 == 1:
                n = 3*n +1
                z += 1
                print(f"Nr.{z}     {n} ")

    print("")
    print("Det tok", z-1, "forsøk og komme til 0 med tallet",tall )
    print("")

algoritme(75478543785435474578874578453784578457865675647675732748927857857567252857895783732576575787536536328695273562387563434572478567234856783456837457346578346578346576345873654785346578346785678543768543678568754376835768453785347865347863457864538675453678768)
