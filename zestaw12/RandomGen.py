import random
import math
import numpy as np


class RandomGen:

    @staticmethod
    def minuslist(n):
        lista = ["x" for i in range(n)]
        return lista

    @staticmethod
    def randomizeList(list):
        n = len(list)
        temp_list = RandomGen.minuslist(n)
        for i in list:
            int_rand = random.randint(0, n - 1)
            if temp_list[int_rand] == "x":
                temp_list[int_rand] = i
            else:
                while temp_list[int_rand] != "x":
                    int_rand = (int_rand + 1) % n
                temp_list[int_rand] = i
        return temp_list

    def rand(self, n):
        lista = []
        for i in range(n):
            lista.append(i)

        return RandomGen.randomizeList(lista)

    def closeRand(self, n):
        closeValue = math.ceil(math.log10(n))

        lista = [i for i in range(n)]

        i = 0
        while i < n - 1:
            int_rand = random.randint(i, i + closeValue)
            if int_rand <= n - 1:
                lista[int_rand], lista[i] = lista[i], lista[int_rand]
            i = int_rand + 1

        return lista

    def reversedCloseRand(self, n):
        lista = self.closeRand(n)

        return lista.reverse()

    def sample(self):
        x = np.random.uniform(0, 1, [2])
        z = np.sqrt(-2 * np.log(x[0])) * np.cos(2 * np.pi * x[1])
        sigma_sq = 1
        mu = 0
        return z * sigma_sq + mu

    def gaussianRand(self, n):
        lista = [self.sample() for i in range(n)]

        return RandomGen.randomizeList(lista)

    def repeatRand(self, n):
        k = math.ceil(math.sqrt(n))
        temp_list = [i for i in range(k)]
        lista = [temp_list[random.randint(0, k - 1)] for i in range(n)]
        return lista

