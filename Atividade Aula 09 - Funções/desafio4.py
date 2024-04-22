# DESAFIO 03

# Faça um programa que tenha uma função chamada maior(), que receba três parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(v1, v2, v3):
    if v1 > v2 and v1 > v3:
        return v1
    elif v2 > v3:
        return v2
    else: return v3
    

print(maior(1,2,3))


