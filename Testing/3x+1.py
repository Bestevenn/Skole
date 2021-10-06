



import math




#deffinerer en funkjson som vi kan kalle når som helst i progammret
def algoritme(tall):
    n = float(tall)
    tall = n
    z = 0
    print("")
    print("Tall:",n)
    print("")

    while n > 1:
            if n%2 == 0:
                n =  n/2
                z += 1
                print(f"Nr.{z}     {n} ")
            elif n%2 == 1:
                n = 3*n +1
                z += 1
                print(f"Nr.{z}     {n} ")

    print("")
    print("Det tok", z-1, "forsøk og komme til 0 med tallet",tall )
    print("")


Fortsett = True

while Fortsett:
    print("")
    brukertall = input("skriv et tall/eller skriv 'flere' for flere tall s for stopp : ")
    print("")
    if brukertall == "s":
        Fortsett = False
    elif brukertall == "flere":
        start = int(input("start?: "))
        stop = int(input("stop?: "))

        for n in range(start,stop+1):
            algoritme(n)
    else:
        algoritme(brukertall)


