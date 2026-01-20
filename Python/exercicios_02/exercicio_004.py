letra = input("Digite aqui a letra a ser verificada")
letra = letra.upper()

if letra == ("A" or "E" or "I" or "O" or "U"):
    print("A sua letra é uma vogal")
elif letra == ("H" or "W" or "W"):
    print("A sua letra é uam letra muda")
else:
    print("A sua letra é uma consoante")