import math as m

x = float(input("Введіть x: "))

x1 = (3 * m.tan(x)) / (m.log(m.cos(x)) + 4)
x2 = abs(x - x**2)

result = x1 + x2
print("result=", result)
