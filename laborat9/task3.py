n = int(input("Скільки фірм? "))
firms = {}
for i in range(n):
    name = input("Назва фірми: ")
    firms[name] = float(input("Оборотні активи: "))

total = sum(firms.values())
min_firm = min(firms, key=firms.get)
max_firm = max(firms, key=firms.get)

print("Сумарні активи:", total)
print("Найменші активи:", min_firm, firms[min_firm])
print("Найбільші активи:", max_firm, firms[max_firm])
