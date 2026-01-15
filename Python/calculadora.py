n1 = (int(input("Digite o primeiro número: ")))
n2 = (int(input("Digite o segundo número: ")))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Digite o número da operação desejada: "))

if operacao == 1:
    print(n1 + n2)

elif operacao == 2:
        print(n1 - n2)

elif operacao == 3:
          print(n1 * n2)

elif  operacao == 4:
        print(n1 / n2)
        
else:
        print("Operação invalida!")

