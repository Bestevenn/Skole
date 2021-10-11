import pytesseract
from PIL import Image

path = input("Bilde: ")

img = Image.open(path)

text = pytesseract.image_to_string(img)
print(text)
