
# oppgave 1

a0 = int(input("startverdi: "))
d = int(input("deifferantse: "))

fortsett = True
while fortsett:
    if d > 0:
        print("Rikig")
        fortsett = False
    elif d < 0:
        print("tallet må våre posetivt")
        d = int(input("deifferantse: "))

L1 = []
L2 = []
for n in range(a0, a0+30, d):
    L1.append(n)
    # oppgave d
    if n % 2 == 0:
        print()
    elif n % 2 == 1:  # "%" gir oss tilbake hvor mye som er i rest
        L2.append(n)

print("Oppgave b: )", L1)
print("Oppgave c: )", L2)
print("")
print("summen av tallene i oppgave b: ", sum(L1))
print("summen av tallene i oppgave c: ", sum(L2))
