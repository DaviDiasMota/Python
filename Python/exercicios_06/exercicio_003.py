try:
    nome = str(input("Qual o seu nome?"))
    peso = float(input(f"Olá {nome} qual seu peso em kg: "))
    altura = float(input("Qual sua altura em metros: "))
    imc = peso/(altura * altura)



    print(f"O{nome}, seu IMC é: ", imc)
except ValueError:
    print("Formato Inválido!")

except Exception as erro:
    print("Ocorreu um erro", erro)
    