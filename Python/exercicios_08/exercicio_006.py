notas = []
divisão = 4
for i in range(4):
    valor = float(input("Digite a not do aluno(a):   "))
    notas.append(valor)

print(f"A média do aluno(a) é :  {(notas [0] + notas[1] + notas[2] + notas [3])/4}")