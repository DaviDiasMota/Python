nome = input("Digite seu nome: ")
while len(nome) < 3:
    print("Nome invalido, ele deve ter mais de 3 caracteres.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite a sua idade:  "))
while idade not in range(0,150):
    print("Idade invalida!")
    idade = int(input("Digite a sua idade:  ")) 

salario = float(input("Digite aqui o seu salário: "))
while salario <=0:
    print("Salário invalido!")
    salario = float(input("Digite aqui o seu salário:  "))
sexo = input("Qual o seu sexo? Digite 'M' para masculino e 'F' para feminino   ").upper()
while sexo  != "M" and sexo != "F":
    print("Sexo invalido!")
    sexo = input("Qual o seu sexo? Digite 'M' para masculino e 'F' para feminino").upper()
casado = input("Qual o seu estado civil? 's' pra solteiro, 'c' para casado, 'v' para viuva, 'd' para divorciado:")
while not casado == 's' or casado == 'c' or casado == 'v' or casado == 'd':
    print("Caso indefinido")
    casado = input("Qual o seu estado civil? 's' pra solteiro, 'c' para casado, 'v' para viuva, 'd' para divorciado:").lower()
    