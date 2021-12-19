import tkinter as tk
from tkinter import simpledialog


def meldingsbox(input,navn_box):
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title=f"{navn_box}", prompt=f"{input}")
    return USER_INP

