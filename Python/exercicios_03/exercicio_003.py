#Leia um número inteiro n e imprima sua tabuada de 1 a 10

print("Gerador de tabuada")

n = int(input('Digite aqui o número que você quer saber a tabuada: '))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")