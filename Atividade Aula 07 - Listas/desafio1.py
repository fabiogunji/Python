# DESAFIO 01

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lstValores = []

for n in range(1,6):    
    lstValores.append(int(input(f"Entre o {n}º número: ")))    
    
print(f"O maior valor da lista é {max(lstValores)} e sua posição é {lstValores.index(max(lstValores))}")
print(f"O menor valor da lista é {min(lstValores)} e sua posição é {lstValores.index(min(lstValores))}")