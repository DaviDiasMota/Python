#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua sua senha: ")

while senha == usuario:
    print("ERRO! a senha não pode ser igual o nome de usuário")
    senha = input("Digite sua senha novamente:  ")

print("Login aceito")
