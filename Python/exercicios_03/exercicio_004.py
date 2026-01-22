#Leia números inteiros até o usuário digitar 0. Ao final, mostre a soma

i = 1
valor = 0
while i != 0:
    i = int(input("Digite um valor a ser somado"))
    valor += i

print(f"Os valores somados é {valor}")