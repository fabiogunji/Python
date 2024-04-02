
#DESAFIO 06

#Crie um programa que faça o computador jogar Jokenpô com

import random

dicionario = {0:"Pedra", 1:"Papel", 2:"Tesoura"}

acertou = False

try:
    while acertou == False:
        
        jogadaComputador = random.randint(0,2)
    
        jogador = int(input("Entre com um número para jogar: 0 - Pedra |  - Papel | 2 - Tesoura: "))

        if (dicionario[jogadaComputador] == dicionario[jogador]):
            print(f"Você ganhou! - {dicionario[jogadaComputador]}")
            acertou = True
        else:
            print(f"Você perdeu! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
except:
    print("Entre com valores válidos")






