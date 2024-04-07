from tkinter import *
from tkinter import ttk
import pygame as pg
import sys
pg.init()

root = Tk()
root.title("sound buttons")
root.geometry("500x200")

sounds = [
    pg.mixer.Sound('./sounds/accordion-loop-bubble_140bpm.wav'),
    pg.mixer.Sound('./sounds/automotive-synth-shot-loud-lead-chord_120bpm_A.wav'),
    pg.mixer.Sound('./sounds/hi-hats-fill-dubstep-style_112bpm_A#_minor.wav'),
    pg.mixer.Sound('./sounds/lo-fi-smooth-guitar-gentle-melody_70bpm_F_minor.wav'),
    pg.mixer.Sound('./sounds/processed-mixed-drums-weird-loop_128bpm_E_minor.wav')
]

def play_sound(sound_index):
    sounds[sound_index].play()



button = ttk.Button(text="sound_1", command=lambda: play_sound(0))
button.pack(side='left', expand = 1)
button = ttk.Button(text="sound_2", command=lambda: play_sound(1))
button.pack(side='left', expand = 1)
button = ttk.Button(text="sound_3", command=lambda: play_sound(2))
button.pack(side='left', expand = 1)
button = ttk.Button(text="sound_4", command=lambda: play_sound(3))
button.pack(side='left', expand = 1)
button = ttk.Button(text="bsound_5", command=lambda: play_sound(4))
button.pack(side='left', expand = 1)

root.mainloop()