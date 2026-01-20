#Faça um Programa que leia três números e mostre-os em ordem decrescente. 

n1 = int(input("Qual o primeiro valor a ser verificado: "))
n2 = int(input("Qual o segundo valor a ser verificado: "))
n3 = int(input("Qual o terceiro valor a ser verificado: "))

if n1 > n2 and n2 > n3:
    print(n1,n2,n3)
elif n2 > n1 and n1 > n3:
    print(n2,n1,n3)
elif n3 > n1 and n1 > n2:
    print(n3,n1,n2)
elif n3> n2 and n2 > n1:
    print(n3,n2,n1)
elif n2 > n3 and n3 > n1:
    print(n2,n3,n1)
elif n1 > n3 and n3 > n2:
    print(n1, n3, n2)