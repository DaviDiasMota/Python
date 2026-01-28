def somar(a, b):
    return (a + b)



def eh_par(n1):
    return( n1%2 )






def menu():
    opcao= int(input("Digite aqui sua opção( 1 - somar) (2 - pares) (3 - sair)"))
    if opcao == 1:
        v1 = int(input("Digite o seu primeiro valor:  "))
        v2 = int(input("Digite o seu segundo valor:  "))

        resultado = somar(v1 , v2)
        print(resultado)
        
    if opcao == 2:
        n1 = int(input("digite um número:  "))
        par = eh_par(n1)

        print(f" O seu número é par: {par%2 == 0}")
    if opcao == 3:
        print("Adeus!")

menu()