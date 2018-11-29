import numpy as np


class Skoczek:

    def __init__(self):
        self.plansza = {}
        self.RUCHY_SKOCZKA = 8
        self.N = 5
        self.delta_x = [2, 1, -1, -2, -2, -1, 1, 2]  # różnica współrzędnej x
        self.delta_y = [1, 2, 2, 1, -1, -2, -2, -1]  # różnica współrzędnej y

    def rysuj(self):
        for i in range(self.N):
            for j in range(self.N):
                print("%2s" % self.plansza[i, j], end=' ')
            print()

    def dopuszczalny(self, x, y):
        return self.N > x >= 0 == self.plansza[x, y] and 0 <= y < self.N

    def zapisz(self, krok, x, y):
        self.plansza[x, y] = krok  # zapis ruchu

    def wymaz(self, x, y):
        self.plansza[x, y] = 0

    def probuj(self, krok, x, y):
        # krok - nr kolejnego kroku do zrobienia
        # x, y - pozycja startowa skoczka
        # Funkcja zwraca bool True/False (czy udany ruch).
        udany = False
        kandydat = 0  # numery od 0 do RUCHY_SKOCZKA-1
        while (not udany) and (kandydat < self.RUCHY_SKOCZKA):
            u = x + self.delta_x[kandydat]  # wybieramy kandydata
            v = y + self.delta_y[kandydat]
            if self.dopuszczalny(u, v):
                self.zapisz(krok, u, v)
                if krok < self.N * self.N:  # warunek końca rekurencji
                    udany = self.probuj(krok + 1, u, v)
                    if not udany:
                        self.wymaz(u, v)
                else:
                    udany = True
            kandydat += 1
        return udany

    def inicjalizacja_planszy(self):
        self.plansza = {}
        for i in range(self.N):
            for j in range(self.N):
                self.plansza[i, j] = 0
        return self.plansza

    def szukaj_rozwiazan(self, N, x, y, rysuj=False):
        self.N = N
        self.inicjalizacja_planszy()
        self.zapisz(1, x, y)
        if self.probuj(2, x, y):
            print("Mamy rozwiązanie")
            if rysuj:
                self.rysuj()
            return 1
        else:
            print("Nie istnieje rozwiązanie")
            return 0


skoczek = Skoczek()

rozwiazania = np.zeros((6, 6))

for i in [0, 3, 4]:
    for j in [0, 2, 5]:
        print("pole startowe: (%s, %s)" % (str(i), str(j)))
        rozwiazania[i, j] = skoczek.szukaj_rozwiazan(6, i, j)

print(rozwiazania)
