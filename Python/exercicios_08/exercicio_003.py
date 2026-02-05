lista_nomes = []
opcao = ""

while opcao !="0":
    opcao = input("Digite o nome da pessoa que deseja adicionar e digite '0' para sair:   ")
    if opcao != "0":
        lista_nomes.append(opcao)
        
print("A sua lista de nomes é: ", lista_nomes)
        
