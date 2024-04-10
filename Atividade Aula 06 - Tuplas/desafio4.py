# DESAFIO 04

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o números pares.

tpNumeros = []
contador = contador9 = posicao3 = 0 
valPares = []


for contador in range(1,5):
    valores = int(input("Entre com um número inteiro: "))
    tpNumeros.append(valores)    
    contador += 1 
    
    if valores % 2 == 0:
        valPares.append(valores)      

tpnum = tuple(tpNumeros)

print(tpnum)

contador9 = tpnum.count(9)

if 3 in tpnum:    
    posicao3 = tpnum.index(3)
else:
    print(">>> O número 3 não consta na lista")   

'''
#Segunda Maneira
numeros = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),\
            int(input('Digite um número: ')),int(input('Digite um número: ')))
''' 

print(f"A) Quantas vezes apareceu o valor 9: {contador9}")
print(f"# B) Em que posição foi digitado o primeiro valor 3: Posição {posicao3}")
print(f"# C) Quais foram o números pares: {tuple(valPares)}")
