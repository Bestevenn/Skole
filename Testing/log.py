from math import log


def logtest():
    for n in range(100+1):
        a, b, c = n, n+1, n+2
        svar1 = log(a*b*c)
        svar2 = log(a) + log(b) + log(c)
        if svar1 == svar2:
            print("TRUE")
        else:
            print("FALSE    ", svar1, svar2, "orginale tall = ", a, b, c)


logtest()
