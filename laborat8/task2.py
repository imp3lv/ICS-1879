import numpy as np
import random as r

n=int(input("Введіть число: "))
masiv=np.zeros((n,n),dtype=int)

for i in range(n):
    for j in range(n):
        masiv[i][j]=r.randint(1,12)
print(masiv)

dobutok=1
for i in range(n):
    dobutok=dobutok*masiv[i][i]
print("Добуток діагоналі:",dobutok)

povtory=[]
for i in range(n):
    for j in range(n):
        if masiv[i][j] in povtory:
            masiv[i][j]=0
        else:
            povtory.append(masiv[i][j])
print(masiv)
