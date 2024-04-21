from tkinter import *

root = Tk()
root.title('rgb_colors')
root.geometry("425x275")
root.config(bg='black')

canvas = Canvas(root, width=250, height=250)
canvas.grid(row=0, column=0, padx=10, pady=10)

def make_rgb_color(red, green, blue):
    return f'#{red:02x}{green:02x}{blue:02x}'

def slider_changed(event):
    red = slider_r.get()
    green = slider_g.get()
    blue = slider_b.get()
    color = make_rgb_color(red, green, blue)
    canvas.configure(bg=color)

slider_r = Scale(root, from_=0, to=255, length=250, background='darkgray', command=slider_changed)
slider_r.grid(row=0, column=2, sticky=N, pady=10)
slider_g = Scale(root, from_=0, to=255, length=250, background='darkgray', command=slider_changed)
slider_g.grid(row=0, column=3, sticky=N, pady=10)
slider_b = Scale(root, from_=0, to=255, length=250, background='darkgray', command=slider_changed)
slider_b.grid(row=0, column=4, sticky=N, pady=10)

root.mainloop()