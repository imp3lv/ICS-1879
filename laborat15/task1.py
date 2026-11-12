import tkinter as tk
import math

def action1():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    d = b*b - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        L.config(text='x1 = ' + str(x1) + '  x2 = ' + str(x2))
    elif d == 0:
        x = -b / (2*a)
        L.config(text='x = ' + str(x))
    else:
        L.config(text='Коренів немає')

win = tk.Tk()
win.geometry('400x300')
win.config(background='green')
la = tk.Label(text='a', background='green')
entry_a = tk.Entry(width=20)
lb = tk.Label(text='b', background='green')
entry_b = tk.Entry(width=20)
lc = tk.Label(text='c', background='green')
entry_c = tk.Entry(width=20)
button = tk.Button(text='Обчислити', command=action1)
L = tk.Label(text='', background='green')
la.pack()
entry_a.pack()
lb.pack()
entry_b.pack()
lc.pack()
entry_c.pack()
button.pack()
L.pack()
win.mainloop()
