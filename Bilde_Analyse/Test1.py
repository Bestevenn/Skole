import pytesseract
from PIL import Image
import os

alle_områder = []

for n in range(2, 8+1):
    img = Image.open(
        f"/Users/martinknutsen/Documents/GitHub/Skole/Bilde_Analyse/Bilder/{n}.png")
    text = pytesseract.image_to_string(img)
    os.system(f"mkdir /Users/martinknutsen/Documents/GitHub/Skole/Bilde_Analyse/Bilder/Testmappe/{text}")
