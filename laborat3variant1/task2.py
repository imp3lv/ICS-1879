import sys

n = int(sys.argv[1])
n1 = n // 100
n2 = (n // 10) % 10 
n3 = n % 10            
s = (n1 + n2 + n3) / 3  
print("Середнє арифметичне цифр числа =", s)
