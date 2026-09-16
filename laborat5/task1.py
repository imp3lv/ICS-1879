import math as m

x = float(input("Введіть x: "))

if x >= 3:
    result = m.sin(x)
elif x >= 0 and x < 3:
    result = m.cos(x)
else:
    result = m.tan(x)

print("Вiдповiдь:", result)
