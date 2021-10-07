from math import sqrt
def svar_skjekk(a,b,c):
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

        
svar_skjekk(2,8,8)
