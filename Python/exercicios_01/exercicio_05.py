opcao = int(input("Digite 1 para converter cm em metros e 2 para converter metros em cm"))
if opcao == 1:
    cm = float(input("Digite o valor em cm para serem convertidoss para metros: "))
    print(cm/100)

elif opcao == 2:
    metros = float(input("Digite o valor em metros a serem convertidos para centimetros:"))
    print(metros*100)
else:
    print("Opção Invalida!")
