n = int(input("Кількість рядків: "))
result = []

for i in range(n):
    x = input("Введіть свої літери в рядок: ")
    while len(x) % 2 != 0 or not x.isalpha():
        x = input("Помилка! Введіть лише літери і парну довжину: ")
    half = len(x) // 2
    x = x[:half-1] + x[half-1:half+1].upper() + x[half+1:]
    result.append(x)

for x in result:
    print(x)
