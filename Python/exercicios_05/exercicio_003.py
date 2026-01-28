def calcular_media(n1,n2,n3):
    return ((n1 + n2 + n3)/3)

nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda nota: "))
nota3 = float(input("Digite aqui a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

if media >= 7:
    print(f"Você está aprovado e sua media é: {media}")

elif media > 5:
    print(f"Voce está de recuperação e sua média é: {media}" )

else:
    print(f"Você está reprovado e sua media é {media}")