consoantes = []
contador = 0
for i in range(10):
    letras = input("Digite aqui uma letra:  ").upper()
    
    if letras not in "AEIOU":
        consoantes.append(letras)
        contador = contador + 1
        
        
print(f" Foram digitadas {contador} consoantes e aqui estão elas:  {consoantes}")