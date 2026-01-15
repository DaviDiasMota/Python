nome = input("Qual o seu nome?")
peso = float(input(f"Olá {nome} qual seu peso: "))
altura = float(input("Qual sua altura em metros: "))
imc = peso/(altura * altura)



print(f"O{nome}, seu IMC é: ", imc)