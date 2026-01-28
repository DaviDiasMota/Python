def eh_par(n1):
    return( n1%2 )

n1 = int(input("digite um número:  "))
par = eh_par(n1)

print(f" O seu número é par: {par%2 == 0}")