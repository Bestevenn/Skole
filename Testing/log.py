from math import log
from random import randint

def logtest():
    høytall = 1000
    a,b,c = randint(1,høytall), randint(1,høytall), randint(1,høytall)
    svar1 = log(a*b*c)
    svar2 = log(a) + log(b) + log(c)
    if svar1 == svar2:
        print("TRUE")
        
    else:
        print("FALSE")


for n in range(1000):
    logtest()


