
#Leia números até digitar -1. Mostre a média dos valores digitados.
i = 0
valor_total = 0
contador = 0

while i >=0:
    i = int(input("Digite aqui o valor a ser adicionado na média:  "))
    if i < 0:
        break
    valor_total += i
    contador = contador + 1

print(valor_total/contador)