n1 = float(input("Digite o valor do primeiro número a ser verificado: "))
n2 = float(input("Digite o valor do segundo número a ser verificado: "))
n3 = float(input("Digite o valor do terceiro número a ser verificado: "))

if n1 > n2 and n1 > n3:
    print(f"{n1}, é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"{n2}, é o maior número")
else:
    print(f"{n3}, é o maior número")

if n1 < n2 and n1 < n3:
    print(f"{n1}, é o menor número")
elif n2 < n1 and n2 < n3:
    print(f"{n2}, é o menor número")
else:
    print(f"{n2}, é o menor número")