import pytesseract
from PIL import Image
import os
img = Image.open(
    "Bilde_Analyse/Skjermbilde 2021-10-12 kl. 00.53.47.png")
text = pytesseract.image_to_string(img)
print(text)
