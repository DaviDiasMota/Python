#def fatorial(n):
 #   if n == 0 or n == 1:
    #    return 1
   # else: 
    #    return n * fatorial(n - 1)
    
#print(fatorial(10))

def fatorial_interativo(n):
    if n < 0:
        return None
    fat = 1
    for i in range(1, n + 1):
        fat = fat * i
    return fat