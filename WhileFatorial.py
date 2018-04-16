n= int(input("Digite um número inteiro: "))
# leia n e calcula fatorial, para de calcular quando digitar num negativo
while n>=0:
    fatorial=1  
    while n>1: #calcula fatorial
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n= int(input("Digite um número inteiro: "))
    
