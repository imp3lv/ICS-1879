import math as m

def raxyemo(a, b, c, d):
    x1 = a**2
    x2 = m.log(abs(b))
    x3 = m.sin(c) * m.sqrt(abs(d))
    result = x1 + x2 - x3
    return result

a = float(input("Введіть x: "))
b = float(input("Введіть a: "))
c = float(input("Введіть b: "))
d = float(input("Введіть c: "))

result = raxyemo(a, b, c, d)
print("result=", result)
