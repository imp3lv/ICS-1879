A = set(range(1, 26))
B = {x for x in A if x % 3 == 0}
C = A - B
print("A =", A)
print("B (діляться на 3) =", B)
print("C (не діляться на 3) =", C)
