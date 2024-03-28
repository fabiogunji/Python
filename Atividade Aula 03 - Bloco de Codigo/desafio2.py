# DESAFIO 02

# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado.

# A multa vai custar R$ 7,00 por cada Km acima do limite.

import random

velocidadeCarro =  random.randint(1,200)

velocidadeMaxima = 80

if velocidadeCarro > velocidadeMaxima:
    valorAcima = float((velocidadeCarro - velocidadeMaxima) * 7)
    print(f"Multado! Você ultrapassou o limite de velocidade de {velocidadeMaxima} km/h e sua velocidade foi de {velocidadeCarro} km/h e sua multa será de R$ {valorAcima}.")
else:
    print(f"Siga em frente! - A velocidade máxima é de {velocidadeMaxima} km/h e você passou com {velocidadeCarro} km/h")