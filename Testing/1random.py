import os

svar_lagre = "C:\Windows\assembly"
t = os.access(svar_lagre, os.X_OK | os.W_OK) 

if t == False:
    print("du har ikke tilgang")
