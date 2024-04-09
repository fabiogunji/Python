# DESAFIO 02

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na Tupla.

import random

tpNumeros = []
numeroMaior = contador = 0
limite = 100
numeroMenor = limite + 1

for contador in range(1,6):
    numero = random.randint(0,limite)    
    tpNumeros.append(numero)
    
    if contador == 0:
        numeroMaior = numero
        numeroMenor = numero
    else:
        if numero > numeroMaior:
            numeroMaior = numero
        
        if numero < numeroMenor:
            numeroMenor = numero
    
    contador += 1    

print(f"Segue a lista de números inteiros aleatórios: {tuple(tpNumeros)}")
print(f"O maior número da lista é {numeroMaior}")
print(f"O menor número da lista é {numeroMenor}")
