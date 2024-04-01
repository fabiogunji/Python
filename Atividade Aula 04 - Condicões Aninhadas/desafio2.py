#DESAFIO 02

# Escreva um programa que leia dois números inteiros e compare- os, mostrando na tela uma mensagem:

# O primeiro valor é maior

# O segundo valor é maior

# Não existe valor maior, os dois são iguais

v1 = int(input("Entre com o primeiro valor inteiro: "))
v2 = int(input("Entre com o segundo valor inteiro: "))

# v1 > v2
# v2 > v1
# v1 = v2

if(v1 > v2):
    print(f"Primeiro valor {v1} maior que o segundo valor {v2}.")
elif(v2 > v1):
    print(f"Segundo valor {v2} maior que o primeiro valor {v1}.")
else:
    print(f"Valores iguais {v1} e {v2}.")