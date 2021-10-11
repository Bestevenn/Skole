


import math
import time

øking = 10**2
n = 1
while True:
    n += øking
    e = (1+(1/n))**(n)
    print(e,"   ", n)
    if n > 100000000:
        break
    elif e == math.e:
        break
    