# DESAFIO 01

# Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 5 e 0 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

import random

numeroComputador = random.randint(0,5)

numeroInserido = int(input("Entre com um número inteiro entre 0 e 5: "))

if numeroInserido < 0 or numeroInserido > 5:
    print(f"Insira um valor válido entre 0 e 5, valor inserido é {numeroInserido}")
else:
    if numeroComputador == numeroInserido:
        print(f"VOCÊ VENCEU! - O computador gerou o número {numeroComputador} e você inseriu o número {numeroInserido}")
    else:
        print(f"VOCÊ PERDEU! - O computador gerou o número {numeroComputador} e você inseriu o número {numeroInserido}")
    