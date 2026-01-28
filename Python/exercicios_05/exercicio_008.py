def somar_positivos():
    i = 0
    total = 0
    while i >= 0:
        i = int(input("Digite um valor a ser somado:  "))
        if i < 0:
            break
        total += i
    print(total)

somar_positivos()