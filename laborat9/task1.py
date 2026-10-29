a = input("Введіть дійсні числа через пробіл: ")
b = tuple(float(x) for x in a.replace(',', '.').split())
print("Кортеж:", b)
