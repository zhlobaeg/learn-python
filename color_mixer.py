from tkinter import *
import random

root = Tk()
root.title('rgb_colors')
root.geometry("600x500")
root.config(bg='black')

canvas = Canvas(root, width=200, height=200)
canvas.grid(row=0, column=0, padx=10, pady=10)
canvas_mix = Canvas(root, width=100, height=200)
canvas_mix.grid(row=0, column=1, pady=10)
canvas_2 = Canvas(root, width=200, height=200)
canvas_2.grid(row=0, column=2, padx=10, pady=10)

def make_rgb_color(red, green, blue):
    return f'#{red:02x}{green:02x}{blue:02x}'

def set_col1(event):
    red = slider_r.get()
    green = slider_g.get()
    blue = slider_b.get()
    color = make_rgb_color(red, green, blue)
    canvas.configure(bg=color)
    mix_colors()

def set_col2(event):
    red = slider_r2.get()
    green = slider_g2.get()
    blue = slider_b2.get()
    color_2 = make_rgb_color(red, green, blue)
    canvas_2.configure(bg=color_2)
    mix_colors()

def mix_colors():
    red = mix_chanel(slider_r.get(), slider_r2.get())
    green = mix_chanel(slider_g.get(), slider_g2.get())
    blue = mix_chanel(slider_b.get(), slider_b2.get())
    color_3 = make_rgb_color(red, green, blue)
    canvas_mix.configure(bg=color_3)

def mix_chanel(a,b):
    new_chanel = (a + b)//2
    return new_chanel

def random_colors():
    slider_r.set(random.randint(0, 255))
    slider_g.set(random.randint(0, 255))
    slider_b.set(random.randint(0, 255))

    slider_r2.set(random.randint(0, 255))
    slider_g2.set(random.randint(0, 255))
    slider_b2.set(random.randint(0, 255))
    mix_colors()


slider_r = Scale(root, from_=0, to=255, length=200, orient=HORIZONTAL, background='darkgray', command=set_col1)
slider_r.grid(row=1, column=0, sticky=N, pady=10)
slider_g = Scale(root, from_=0, to=255, length=200, orient=HORIZONTAL, background='darkgray', command=set_col1)
slider_g.grid(row=2, column=0, sticky=N, pady=10)
slider_b = Scale(root, from_=0, to=255, length=200, orient=HORIZONTAL, background='darkgray', command=set_col1)
slider_b.grid(row=3, column=0, sticky=N, pady=10)

b1 = Button(root, text='random_col', width=10, background='lightgray', command=random_colors)
b1.grid(row=1, column=1, padx=10, pady=10)

slider_r2 = Scale(root, from_=0, to=255, length=200, orient=HORIZONTAL, background='darkgray', command=set_col2)
slider_r2.grid(row=1, column=2, sticky=N, pady=10)
slider_g2 = Scale(root, from_=0, to=255, length=200, orient=HORIZONTAL, background='darkgray', command=set_col2)
slider_g2.grid(row=2, column=2, sticky=N, pady=10)
slider_b2 = Scale(root, from_=0, to=255, length=200, orient=HORIZONTAL, background='darkgray', command=set_col2)
slider_b2.grid(row=3, column=2, sticky=N, pady=10)

root.mainloop()