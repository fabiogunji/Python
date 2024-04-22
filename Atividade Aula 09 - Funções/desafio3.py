# DESAFIO 03

# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada


def contador(inicio, fim, passo):
    for i in range (inicio,fim,passo):
        print(i)
        


print(f"A) De 1 até 10, de 1 em 1: {contador(1,11,1)}")
print(f"B) De 10 até 0, de 2 em 2: {contador(10,0,-2)}")
print(f"C) Uma contagem personalizada: {contador(-100,0,20)}")