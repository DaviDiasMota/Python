nota = int(input("digite o valor de uma nota: "))

while nota not in (range(1, 10)):
    print("Nota invalida!")
    nota = int(input("digite o valor de uma nota: "))
