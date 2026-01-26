import random

num = random.randint(1, 100)
opcao = int(input("Digite aqui um valor: "))
tentativas = 1
while opcao != num:
    print("PARABENS, VOCÊ ERROU!!")
    if opcao > num:
        print("É um valor menor")
        opcao = int(input("Digite aqui outro valor:  "))
    if opcao < num:
        print("É um valor maior")
        opcao = int(input("Digite aqui outro valor:  "))
    tentativas = tentativas + 1

print("PARABÉNS, VOCê ACERTOU!!!")
print(f"Em {tentativas} tentativas")
