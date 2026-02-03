def tabuada(n1):
    n1 = float(input("Digite um valor para a tabudada ser exibida:  "))
    for i in range(1, 11):
        print(f"{n1} * {i} = {n1 * i}")
        i = i + 1
try :     
    valor = 0
    tabuada(valor)
except ValueError:
    print("Não aceitamos letras no calculo.")
except Exception as erro:
    print("Ocorreu um erro: ", erro)

    
