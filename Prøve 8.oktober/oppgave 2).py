# oppgave 2

import random

antall_kast = 3
for n in range(antall_kast):
    terning1 = random.randint(1, 6)
    print("ditt kast")
    print(terning1)
    t1 = 0
    if terning1 == 6:
        print("Du fikk seks. kast en gang til")
        t1 = input("skriv kast for å kaste en gang til: ")
    if t1 == "kast":
        terning = random.randint(1, 6)
        print("Du kan flytte", terning, "fremover")
        exit()
else:
    print("du må vente til neste runde")
