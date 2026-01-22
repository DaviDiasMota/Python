#Leia uma quantidade definida de números e mostre o maior e o menor, sem usar min ou max

valor_variavel = 0
valor_final_maior = 0
valor_final_menor = 999999999999999999999999

for i in range (1,11):
    valor_variavel = int(input("Digite aqui um valor númerico:  "))
    if valor_variavel > valor_final_maior:
        valor_final_maior = valor_variavel
    elif valor_variavel < valor_final_menor:
        valor_final_menor = valor_variavel

print(f"O menor valor é {valor_final_menor}.")
print(f"O maior valor é {valor_final_maior}")