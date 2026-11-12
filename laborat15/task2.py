import tkinter as tk

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(text, shift):
    res = ''
    for ch in text.lower():
        if ch in alphabet:
            i = (alphabet.index(ch) + shift) % 26
            res = res + alphabet[i]
        else:
            res = res + ch
    return res

def action1():
    shift = int(entry.get())
    text = box1.get('1.0', tk.END)
    box2.delete('1.0', tk.END)
    box2.insert('1.0', caesar(text, shift))

def action2():
    shift = int(entry.get())
    text = box1.get('1.0', tk.END)
    box2.delete('1.0', tk.END)
    box2.insert('1.0', caesar(text, -shift))

win = tk.Tk()
L = tk.Label(text='Введіть текст (англійською) і зсув')
box1 = tk.Text(width=40, height=5)
entry = tk.Entry(width=10)
fr = tk.Frame()
button1 = tk.Button(master=fr, text='Шифрувати', command=action1)
button2 = tk.Button(master=fr, text='Дешифрувати', command=action2)
box2 = tk.Text(width=40, height=5)
L.pack()
box1.pack()
entry.pack()
fr.pack()
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
box2.pack()
win.mainloop()
