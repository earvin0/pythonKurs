def rys(dlugosc):

    #gora
    
    miarka = "|"
    for i in range(dlugosc):
        miarka += "....|"

    #dol

    miarka += "\n"
    for i in range(dlugosc + 1):
        miarka += str(i)
        for j in range(5 - len(str(i))):
            miarka += " "

    return miarka


napis = input("Podaj liczbe: ")
try:
    n = int(napis)
except ValueError:
    print("Podane wyrazenie nie jest liczba!")
    exit()

print(rys(n))
