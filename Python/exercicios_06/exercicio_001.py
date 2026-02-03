def conversao_moedas_real():
    opcao = 0
    print("Olá você quer converter real para qual moeda?")
    print(" 1 - Dólar\n 2 - Libras")
    opcao = int(input())
    valor = float(input("Qual o valor em Reais a ser convertido:  "))
    if opcao == 1:
        print (f" O valor convertido é {valor/5.20:.2f} U$")
    if opcao == 2:
        print (f" O valor convertido é {valor/7.16:.2f} C")
    
def conversao_moedas_dolar():
    opcao = 0
    print("Olá você quer converter dolar para qual moeda?")
    print(" 1 - Real \n 2 - Libras")
    opcao = int(input())
    valor = float(input("Qual o valor em Dólares a ser"))
    if opcao == 1:
        print (f" O valor convertido é {valor*5.20:.2f} R$")
    if opcao == 2:
        print (f" O valor convertido é {valor/1.38:.2f} C")
    
def conversao_moedas_libras():
    opcao = 0
    print("Olá você quer converter  libras para qual moeda?")
    print(" 1 - Real \n 2 - Dólar")
    opcao = int(input())
    valor = float(input("Qual o valor em Libras a ser convetido:  "))
    if opcao == 1:
        print (f" O valor convertido é {valor/0.14:.2f} R$")
    if opcao == 2:
        print (f" O valor convertido é {valor*1.38:.2f} U$")
    
try:
    print("Olá bem vindo ao sistema de conversão de moedas")
    print(" Qual a moeda que você quer converter?")
    print(" 1 - para Real \n 2 - para Dólar \n 3 - para Libra \n 0 - para sair")    


    menu = "g"
    while menu != 0:
        menu = int(input())
    if menu == 1:
        conversao_moedas_real()
                
    elif menu == 2:
        conversao_moedas_dolar()

    elif menu == 3:
        conversao_moedas_libras()

    elif menu == 0:
        print("Saindo...")

    else:
        print("valor invalido")
except ValueError:
    print("Não aceitamos letras!")