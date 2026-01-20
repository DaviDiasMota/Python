#Programa de calculo de média de duas notas

nome = input("Qual o nome do aluno(a): ")
n1 = float(input("Digite aqui a sua primeira nota: "))
n2 = float(input("Digite aqui a sua segunda nota: "))

media = (n1 + n2)/2

if media < 7:
    print("Reprovado")
elif media < 9:
    print("Aprovado")
else:
    print("Aprovado com Distinção")