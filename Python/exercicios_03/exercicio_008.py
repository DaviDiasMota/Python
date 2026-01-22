#Leia dois inteiros a e b e imprima todos os números primos entre eles.

a = int(input("Digite aqui um valor inicial:  "))
b = int(input("Digite aqui um valor limite:  "))

if a > b:
    inicio = b
    fim = a

else: 
    inicio = a
    fim = b


for num in range (inicio, fim + 1):
    if num > 1:
        primo = True

        for divisor in range (2, num):
            if num % divisor == 0:
                primo = False
                break
        if primo:
            print(num)    
    