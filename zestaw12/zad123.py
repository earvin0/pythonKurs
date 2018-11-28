import RandomGen as rg


def swap(L, left, right):
    L[left], L[right] = L[right], L[left]


def cmp(a, b):
    return int(a < b)


def selectsort(L, left, right, cmpfunc=cmp):
    for i in range(left, right):
        k = i
        for j in range(i + 1, right + 1):
            if cmpfunc(L[j], L[k]) > 0:
                k = j
        # print(str(L[j]) + "  " + str(L[k]) + "  " + str(cmpfunc(L[j], L[k])))
        swap(L, i, k)
    return L


def mediana_sort(L, left, right):
    selectsort(L, left, right)
    return L[len(L) // 2]


r = rg.RandomGen().rand(100)

print(r)
print(mediana_sort(r, 0, 99))
