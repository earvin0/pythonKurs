# odwracanie
def iteracyjnie(L, left, right):
    if left > right:
        print("Niepoprawny zakres!")
        return

    if left > len(L) or left < 0:
        print("index left jest poza lista")
        return

    if right > len(L) or right < 0:
        print("index right jest poza lista")
        return

    r = right
    for l in range(left, right + 1):
        temp = L[l]
        L[l] = L[r]
        L[r] = temp
        r -= 1
        if r <= l:
            break

    return L


def rekurencyjnie(L, left, right):
    if left > right + 1:
        print("Niepoprawny zakres!")
        return

    if left > len(L) or left < 0:
        print("index left jest poza lista")
        return

    if right > len(L) or right < 0:
        print("index right jest poza lista")
        return

    if right <= left:
        return L

    temp = L[left]
    L[left] = L[right]
    L[right] = temp
    return rekurencyjnie(L, left + 1, right - 1)


L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(rekurencyjnie(L, 4, 7))
print(iteracyjnie(L2, 4, 7))
