def rysuj(xx, yy):
    if xx <= 0 or yy <= 0:
        print("Podane dane sa niepoprawne!")
        exit()
    prostokat = ""
    for i in range((yy * 2) + 1):
        # i nawiguje po rzedach ,j po kolumnach
        if i % 2 == 0:
            prostokat += "\n+"
        else:
            prostokat += "\n|"
        for j in range(xx):
            if i % 2 == 1:
                prostokat += "   |"
            else:
                prostokat += "---+"

    return prostokat


height = input("Podaj wysokosc: ")
width = input("Podaj szerokosc: ")
try:
    x = int(width)
except ValueError:
    print("Podane wyrazenie nie jest liczba!")
    exit()
try:
    y = int(height)
except ValueError:
    print("Podane wyrazenie nie jest liczba!")
    exit()

print(rysuj(x, y))
