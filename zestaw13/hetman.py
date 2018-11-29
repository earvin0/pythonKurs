def rysuj():
    for w in range(N):
        for k in range(N):
            if x[k] == w:
                print("H", end=' ')
            else:
                print(".", end=' ')
        print()
    print("-----------------------")


def dopuszczalny(w, k):
    return a[w] and b[w + k] and c[w - k]


def zapisz(w, k):
    x[k] = w
    a[w] = False
    b[w + k] = False
    c[w - k] = False


def wymaz(w, k):
    a[w] = True
    b[w + k] = True
    c[w - k] = True


# def probuj(k):
#     udany = False
#     w = 0  # numery od 0 do N-1
#     while (not udany) and (w < N):
#         if dopuszczalny(w, k):
#             zapisz(w, k)
#             if k < (N - 1):
#                 udany = probuj(k + 1)
#                 if not udany:
#                     wymaz(w, k)
#             else:
#                 udany = True
#         w += 1
#     return udany

def probuj(k, liczba_rozw, rys=True):
    # Sprawdzanie wszystkich kandydatow (wiersze).
    for w in range(N):
        if dopuszczalny(w, k):
            zapisz(w, k)
            if k < (N - 1):
                liczba_rozw = probuj(k + 1, liczba_rozw, rys)
            else:
                if rys:
                    rysuj()
                liczba_rozw += 1
            wymaz(w, k)
    return liczba_rozw



for i in range(1,13):

    N = i  # bok szachownicy i jednocześnie liczba hetmanów

    x = N * [None]

    a = N * [True]

    b = (2 * N - 1) * [True]

    c = (2 * N - 1) * [True]

    liczba_rozw = 0

    liczba_rozw = probuj(0, liczba_rozw, False)

    print("Liczba rozwiazan dla planszy o rozmiarze %s: %s" % (N, liczba_rozw))

