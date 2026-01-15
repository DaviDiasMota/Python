print("Calculo de nota bimestral")

nome = input("Qual o nome do aluno?")
n1 = float(input(f"qual a primeira nota do {nome}?"))
n2 = float(input(f"qual a segunda nota do {nome}?"))
n3 = float(input(f"qual a terceira nota do {nome}?"))
n4 = float(input(f"qual a quarta nota do {nome}?"))
media = (n1 + n2 + n3 + n4)/4
print("A média do aluno", nome,  "é:", media)