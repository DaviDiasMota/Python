#Leia um inteiro n e imprima um triângulo de * com n linhas
n = int(input("Digite o Número de linhas que o triangulo deve ter:   "))

i = 1

for i in range (1, n + 1):
    print("*" * i)