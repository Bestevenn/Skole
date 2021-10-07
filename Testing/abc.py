from math import sqrt
a,b,c = float(2),float(8),float(8)
svar1, svar2 = (-b+sqrt(b**2-4*a*c)) / (2*a), (-b-sqrt(b**2-4*a*c)) / (2*a)

if b**2-4*a*c > 0:
    print("x1: ", svar1,"x2: ", svar2)
elif b**2-4*a*c == 0:
    try:
        print("x1: ",svar1)
    except:
        print("x1: ",svar2)
elif b**2-4*a*c < 0:
    print("ingen svar")

        


