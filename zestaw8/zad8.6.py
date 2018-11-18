def funkcja_p_rekurencyjnie(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i == 0:
        return 1.0
    elif j == 0:
        return 0.0

    return 0.5 * (funkcja_p_rekurencyjnie(i - 1, j) + funkcja_p_rekurencyjnie(i, j - 1))


def funkcja_p(i, j):
    wyniki = {(0, 0): 0.5}

    for ii in range(1, i + 1):
        wyniki[ii, 0] = 0.0
    for ii in range(1, j + 1):
        wyniki[0, ii] = 1.0

    for ii in range(1, i + 1):
        for b in range(1, j + 1):
            if (ii, b) not in wyniki:
                wyniki[ii, b] = 0.5 * (wyniki[ii - 1, b] + wyniki[ii, b - 1])
    return wyniki[i, j]


print(funkcja_p_rekurencyjnie(9, 4))
print(funkcja_p(9, 4))
