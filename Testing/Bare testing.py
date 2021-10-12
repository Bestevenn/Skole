
from PIL import Image
for n in range(1, 4+1):
    img = Image.open(
        f"/Users/martinknutsen/Documents/GitHub/Skole/Bilde_Analyse/Bilder/{n}.png")
    img.show()
