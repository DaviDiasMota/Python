soma = 0
i = 0
valor = 0

for i in range(5):
    valor = int(input("Digite aqui o valor da nota: "))
    soma += valor
    i = i + 1
media = (soma)/i
print(f" A soma das notas é {soma} e sua média é {media}")