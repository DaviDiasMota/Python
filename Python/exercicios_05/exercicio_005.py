def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
        i = i + 1

numero = int(input("Digite o valor da tabuada a ser impressa:  "))

tabuada(numero)