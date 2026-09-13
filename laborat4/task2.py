import math as m

def raxyemo(a, b, c, d):
    x1 = a**2
    x2 = m.log(abs(b))
    x3 = m.sin(c) * m.sqrt(abs(d))
    result = x1 + x2 - x3
    return result

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))
d = float(input("Введіть d: "))

result = raxyemo(a, b, c, d)
print("result=", result)
