#
import serial
import time
import sys
from tkinter import *
from tkinter import ttk
#import tkinter

def get_angle(event):
    angle = int(angulo.get())
    
root = Tk()

#root.master.title(text='Hello')
Label(root, text="Voltaje en Potenciómetro (V):").grid(row=0,column=0)
Label(root, text="Ángulo del servo (grados)").grid(row=1,column=0)
Label(root, text="Ingrese un valor entre 0 y 180:").grid(row=2,column=0)
angulo = Entry(root).grid(row=2, column=1)#, sticky=E)
ingresar = Button(root, text="Enter").grid(row=2, column=2)#.bind("<Button-1>", get_angle)

root.mainloop()
