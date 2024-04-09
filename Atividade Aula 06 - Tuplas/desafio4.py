# DESAFIO 04

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o números pares.

tpNumeros = []
contador = contador9 = 0
valPares = []

for contador in range(1,5):
    valores = int(input("Entre com um número inteiro: "))
    tpNumeros.append(valores)    
    contador += 1 
    
    if valores % 2 == 0:
        valPares.append(valores)
        
    

print(tpNumeros)

contador9 = tpNumeros.count("9")
posicao3 = tpNumeros.index(3)

print(f"A) Quantas vezes apareceu o valor 9: {contador9}")
print(f"# B) Em que posição foi digitado o primeiro valor 3: Posição {posicao3}")
print(f"# C) Quais foram o números pares: {valPares}")
