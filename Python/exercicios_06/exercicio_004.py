try:
    gf = float(input("Qual o valor em graus Fahrenheit a ser convertido?"))

    gc = 5*((gf-32)/9)

    print(f"a temperatura convertida em Celsius é: {gc}°C")
except Exception as erro:
    print("Ocorreu um erro: ", erro)
except ValueError:
    print("Formato Inválido!")