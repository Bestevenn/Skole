from pylab import *




t_liste = []
v_liste = []
s_liste = []


s = 0.0
v = 5.0
a = 2.0
t = 0.0


t_slutt = 3.0
dt = 0.1

while t < t_slutt:
    v += a*dt
    s += v*dt
    t += dt
    v_liste.append(v)
    s_liste.append(s)
    t_liste.append(t)



plot(t_liste, s_liste)
title("prosisjonsgraf")
grid()
show()

 
plot(t_liste, v_liste)
title("fartsgraf")
grid()
show()



    