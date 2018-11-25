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


r = rg.RandomLists().rand(10)

print(r)

print(selectsort(r, 0, 9))
r = rg.RandomLists().rand(10)
print(r)
print(selectsort(r, 0, 9, lambda x, y: int(x > y)))
