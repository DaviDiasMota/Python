n1 = int(input("Digite aqui o primeiro valor:  "))
n2 = int(input("Digite aqui o segundo valor:  "))


if n1 < n2:
    for i in range(n1 + 1,n2):
        print(i)
        i = i + 1
elif n1 > n2:
    for i in range(n2 + 1, n1):
        print(i)
        i = i + 1

else:
    print("")