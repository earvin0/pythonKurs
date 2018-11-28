import RandomGen as rg


def moda_py(L):
    slownik = {}
    for i in L:
        if i not in slownik:
            slownik[i] = 1
        else:
            slownik[i] += 1

    k = list(slownik.keys())
    v = list(slownik.values())
    max_index = v.index(max(v))
    print(slownik)
    print("moda to: "+str(k[max_index])+" wystapila: "+str(v[max_index]))


r = rg.RandomGen().repeatRand(20)
print(r)
moda_py(r)
