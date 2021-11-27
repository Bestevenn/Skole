import math 
def f(x):
    return (1+(1/x))**x

k = 2
x = 10**k
linje = 0 
for n in range(100):
    ans = f(x)
    k *= 2
    print(linje,"=",ans)
    linje += 1

