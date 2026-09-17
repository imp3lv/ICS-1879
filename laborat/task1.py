import math as m

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

n = int((b - a) / h) + 1

for i in range(n):
    x = a + i * h
    y = 3 - m.log(abs(x - 6)) + m.cos(x)
    print("x=%.2f y=%.3f" % (x, y))
