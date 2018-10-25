L = [[], [4], [1, 2], [3, 4], (5, 6, 7)]
L2 = [0 for i in range(len(L))]

for lista in L:
    L2[L.index(lista)] = sum(lista)

print(L2)
