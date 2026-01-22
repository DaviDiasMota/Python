#Leia um número inteiro n (n ≥ 0) e calcule n!. Valide a entrada.

n = int(input("Digite um valor a ser transformado em fatorial:  "))
N = n
if n < 0: 
    print("Entrada Invalida!")
elif n >= 0:
    while n != 1:
        n = n-1
        N = N*n
    print(N)