import tkinter as tk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

#Initialiser la fenêtre
root = tk.Tk()
root.title("Calculatrice")

#Dimensions de la fenêtre
root_width = 480
root_height = 640
#Dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#Calculer le centre
centerx = (int(screen_width/2 - root_width/2))
centery = (int(screen_height/2 - root_height/2))

root.geometry(f'{root_width}x{root_height}+{centerx}+{centery}')
root.resizable(False, False)
root.attributes('-topmost', 1)




root.mainloop()

