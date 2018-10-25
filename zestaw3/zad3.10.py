def roman2int(liczba):
    rom = ["I", "V", "X", "L", "C", "D", "M"]
    arab = [1, 5, 10, 50, 100, 500, 1000]
    slownik = dict(zip(rom, arab))

    # print(list(liczba))

    number = 0
    rozbite = list(liczba)
    for i in range(0, len(rozbite) - 1):
        if slownik[rozbite[i]] >= slownik[rozbite[i + 1]]:
            #           print("adding "+str(D[rozbite[i]]))
            number += slownik[rozbite[i]]
        else:
            #          print("subtracting " + str(D[rozbite[i]]))
            number -= slownik[rozbite[i]]
    #     print("sum: " + str(number))
    number += slownik[rozbite[-1]]

    return number


print(roman2int("MCMXCVIII"))
print(roman2int("MCCCXXIX"))
