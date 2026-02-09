#Constantes

# As constantes são valores que não devem mudar, eles não devem, mas eles podem sim, no entanto é uma forma de mostrar para outro programador que o valor não deve mudar. Elas são definidas por letras maiúsculas.

#Declaração de Constante
NOME = "Pedro"
PROFISSAO = "Garoto de programa"

print(f"{NOME}, é {PROFISSAO}")

#Listas

#As listas armazenam vários valores.

nomes = ["Pedro","Davi", "Amanda"]

print(f"{nomes[0]}, trabalha com front-end☠️")
print(f"{nomes[1]}, trabalha com Marketing😎")
print(f"{nomes[2]}, trabalha Roubando💵")

lista_mista = [1, "dois", 3.0, True]

for i in range(0, 4):
    print(lista_mista[i])
    
nomes.sort()

print(nomes)