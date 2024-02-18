from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Bomberman")
root.geometry("250x200")

def quit():
    exit()

def click():
    window = Tk()
    window.title("game_over")
    window.geometry("250x200")
    label = ttk.Label(window, text="sus amogus was an imposter")
    label.pack(anchor=CENTER, expand = 2)
    close_button = ttk.Button(window, text="close sus amogus", command=quit)
    close_button.pack(anchor="center", expand = 3)

button = ttk.Button(text="imposter", command=click)
button.pack(anchor=CENTER, expand = 1)

root.mainloop()