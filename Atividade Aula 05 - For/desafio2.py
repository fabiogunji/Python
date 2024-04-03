#DESAFIO 02

#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


for elemento in range (1,51):    
    resto = elemento % 2
    if resto == 0:
        print(f"Números pares - {elemento}")
    #else:
    #    print(f"Número impar - {elemento}")
    
    
    