from tkinter import *

root = Tk()
root.title('UI buttons')
root.geometry("500x200")
root.config(bg='palegreen')

label = Label(root, text='bob', background='springgreen')
label.grid(row=0,column=0)
label2 = Label(root, text='bob', background='springgreen')
label2.grid(row=0,column=5)

def set_text(t):
    label['text'] = t
def set_text_l2(t2):
    label2['text'] = t2


b1 = Button(root, text='<-', command=lambda: set_text('left'), background='mediumspringgreen')
b1.grid(row=2, column=0)
b2 = Button(root, text='|', command=lambda: set_text('up'), background='mediumspringgreen')
b2.grid(row=2, column=1)
b3 = Button(root, text='|', command=lambda: set_text('down'), background='mediumspringgreen')
b3.grid(row=2, column=2)
b4 = Button(root, text='->', command=lambda: set_text('right'), background='mediumspringgreen')
b4.grid(row=2, column=3)

b1_l2 = Button(root, text='5', command=lambda: set_text_l2('5'), background='mediumspringgreen')
b1_l2.grid(row=2, column=5)
b2_l2 = Button(root, text='10', command=lambda: set_text_l2('10'), background='mediumspringgreen')
b2_l2.grid(row=2, column=6)
b3_l2= Button(root, text='50', command=lambda: set_text_l2('50'), background='mediumspringgreen')
b3_l2.grid(row=2, column=7)

root.mainloop()