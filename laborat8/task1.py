from array import array

n = int(input("Введіть ціле число: "))
d = array('i', [])

for i in range(1, n + 1):
    if n % i == 0:
        d.append(i)
print("Дільники:", d.tolist())

d.remove(max(d))
d.remove(min(d))
print("Дільники без найбільшого і найменшого:", d.tolist())
