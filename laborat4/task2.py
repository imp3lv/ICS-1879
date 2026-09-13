import math as m

def raxyemo(x, a, b, c):
    x1 = a**2
    x2 = m.log(abs(b))
    x3 = m.sin(c) * m.sqrt(abs(d))
    result = x1 + x2 - x3
    return result

x = float(input("Введіть x: "))
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

result = raxyemo(x, a, b, c)
print("result=", result)
