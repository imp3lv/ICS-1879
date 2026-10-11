x = input("Введіть рядок зі словами: ")
words = x.split()
print("Кількість слів:", len(words))
if words:
    print("Найдовше слово:", max(words, key=len))
