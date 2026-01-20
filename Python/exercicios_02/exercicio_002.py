#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

number = float(input("Digite o valor númérico aqui: "))

if number>= 0:
    print(f"{number} é positivo")
else:
    print(f"{number} é negativo")