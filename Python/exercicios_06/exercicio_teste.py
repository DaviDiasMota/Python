try:
    resultado = 10 / 0

except:
    
    print("Ocorreu um erro durante a operação!")
    
    
num1 = input("Digite o primeiro número:   ")
num2 = input("Digite o segundo número:   ")

try:
    num1 = int(num1)
    num2 = int(num2)
    
    print(f" A soma dois dois números é: {num1 + num2}")
except:
    print("Digite um número correto!")