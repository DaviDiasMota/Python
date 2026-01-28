
def contar_pares(n1, n2):
    pares = 0
    for i in range(n1, n2 + 1):
        if (i%2 == 0): 
            pares = pares + 1
        i = i + 1
    print(f"Nesse intervalo há {pares}, números pares.")

valor1 = int(input("Digite aqui o número inicial do intervalo:  "))
valor2 = int(input("Digite aqui o valor final do intervalo:  "))
    
contar_pares(valor1 , valor2)