# DESAFIO 05

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for impar desconsidere-o.

total = 0
for n in range (1,7):   
    numero = int(input("Digite o sexto número inteiro: "))
    if numero % 2 == 0:
        total = total + numero 
else:
    print(f"A soma total dos números pares é {total}")
    