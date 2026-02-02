def somar(n1, n2):
    return(n1 + n2)
def subtrair(n1 , n2):
    return(n1 - n2)
def dividir(n1, n2):
    return(n1/n2)
def multiplicar(n1, n2):
    return(n1*n2)

print("Calculadora")

menu = "g"
while menu != 0:
    print(" 1 - Para Somar\n 2 - Para Subtrair\n 3 - Para Dividir\n 4 - Para Multiplicar\n 0 - Para Sair")

    menu = int(input("Digite aqui a sua opção:  "))
    
    if menu == 1:
        n1 = float(input("Digite o primeiro valor:  "))
        n2 = float(input("Digite o segundo valor:  "))
        
        resultado = somar(n1, n2)
        print(f" O seu resultado é: {resultado}")
    
    elif menu == 2:
         n1 = float(input("Digite o primeiro valor:  "))
         n2 = float(input("Digite o segundo valor:  "))
         
         resultado = subtrair(n1, n2)
         
         print("O seu resultado é:  ", resultado)
         
    elif menu == 3:
        n1 = float(input("Digite aqui o valor a ser divido:   "))
        n2 - float(input("Digite aqui o valor que será o divisor:  "))
        
        resultado = dividir(n1, n2)
        
        print(f"O seu resultado é: {resultado}")
        
    elif menu == 4:
        n1 = float(input("Digite aqui o primeiro valor:  "))
        n2 = float(input("Digite aqui o segundo valor:  "))
        
        resultado = multiplicar(n1, n2)
        
        print(f"O seu resultado é: {resultado}")
        
    elif menu == 0:
        print("Saindo...")
    else:
        print("Valor inválido")
        input("Aperte Enter para tentar novamente...")