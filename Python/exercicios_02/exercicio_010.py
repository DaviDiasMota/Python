#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
 
periodo = input("Em qual periodo você estuda? (M para matutino, V para vespertino e N para noturno)")

if periodo == "M":
    print("Bom Dia!")
elif periodo == "V":
    print("Boa tarde!")
elif periodo == "N":
    print("Boa Noite!")
else:
    print("Periodo invalido!")