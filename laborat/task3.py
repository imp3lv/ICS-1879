import math as m

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

spisok = []
x = a
while x <= b:
    y = 3 - m.log(abs(x - 6)) + m.cos(x)
    spisok.append(y)
    x = x + h

print("Список в рядок:", spisok)
print("Список у стовпчик:")
for i in spisok:
    print(i)
