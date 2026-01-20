#Programa que imrime o sexo do Usuário

sexo = (input("Qual o seu sexo? M para masculino e F feminino"))
sexo = sexo.upper()

if sexo == "F":
    print("Seu sexo é feminino")
elif sexo == "M":
    print("seu sexo é masculino")
else:
    print("Sexo invalido")