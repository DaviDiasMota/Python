def validar_senha(senha):
    if len(senha) >= 8:
        return("senha valida!")
    elif len(senha) < 8:
        return("senha Invalida!")

senha = input("Digite aqui sua senha:  ")
    
validada = validar_senha(senha)

print("a sua senha é uma", validada)

