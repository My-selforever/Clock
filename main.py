from tkinter import *
from tkinter.ttk import *
from time import strftime
import os

os.system('cls')

root = Tk()
root.title("Digi-Clock")

label  = Label(root,font=('Castellar',80),background='#000000',foreground='#F8A047')
label.pack(anchor='center')

def time() :
    t = strftime('%H : %M : %S %p')
    label.config(text=t)
    label.after(1000,time)

time()
mainloop()