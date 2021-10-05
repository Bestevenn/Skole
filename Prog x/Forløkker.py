




import math
from os import sep
from posixpath import expanduser


nfaktorial = int(input("tall?: "))



a = 1
for n in range(1, nfaktorial+1):
    a = a*n
    
for TOn in range(1,nfaktorial):
    print(TOn, end="*")


print("")
print(nfaktorial,"! = ", a)


