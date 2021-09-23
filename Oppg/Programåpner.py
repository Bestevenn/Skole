
import os
import subprocess




Fortsett = True

while Fortsett:
    hvilkenprogram = str(input("Hvilken program Spotify(S)/Chrome(C): "))
    if hvilkenprogram == "S":
        subprocess.Popen(["/Applications/Spotify.app"]) 
    elif hvilkenprogram == "C":
        print("C")
    else:
        Fortsett = False

print("programmet er ferdig:")


