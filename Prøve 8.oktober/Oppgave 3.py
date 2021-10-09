import random

def mellomrom(): # gjorde det kun for estetikken i koden
    print("")

# a)
N = 10
tall = []
for n in range(N):
    t1 = random.randint(1,6)
    tall.append(t1)  # vet det ikke er helt rikig, men kom ikke på noen annen måte å gjøre det på

# oppave b)
t_1, t_2, t_3, t_4, t_5, t_6 = tall.count(1),tall.count(2),tall.count(3),tall.count(4),tall.count(5),tall.count(6)
print("b): ")
print("du fikk", t_1, "enere,", t_2,"torere,", t_3, "trere,", t_4, "firer,",t_5,"femere og", t_6,"seksere")
mellomrom()
print("din liste:") 
print(tall)
mellomrom()

print("c): ")
gjenomsnitt = sum(tall)/N
print("gjennomsnittet var:", gjenomsnitt)
mellomrom()

print("d): ")
tall.append(gjenomsnitt)
print(tall)
mellomrom()







