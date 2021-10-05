import webbrowser


for n in range(10):
   n = webbrowser.open_new_tab(f"https://www.youtube.com/{n}")
   print(n)

