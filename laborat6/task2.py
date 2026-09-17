import math as m

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

x = a
while x <= b:
    y = 3 - m.log(abs(x - 6)) + m.cos(x)
    print("x=%.2f y=%.3f" % (x, y))
    x = x + h
