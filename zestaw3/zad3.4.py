while 1:
    userInput = input("Podaj liczbę: ")
    if userInput == "stop":
        exit()
    try:
        number = float(userInput)
        print(number, ",", number * number * number)
    except ValueError:
        print("Podane wyrazenie nie jest liczba!")
