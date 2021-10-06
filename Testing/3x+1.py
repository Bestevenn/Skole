



import math




n = float(2**9)
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


