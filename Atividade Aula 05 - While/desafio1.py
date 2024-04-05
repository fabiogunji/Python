# DESAFIO 01

# Faça um jogo, onde o computador vai “pensar” em um número entre 0 a 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

maquina = random.randint(0,10)
contador = 1

print(maquina)

while True:
    jogador = int(input("Entre com um número inteiro entre 0 e 10: "))
    
    if (jogador < 0 or jogador > 10):
        print("Favor entrar com um número entre 0 a 10: ")
        contador += 1
        continue    
    
    else:
        if maquina == jogador:
            print(f"#### Acertou o número {maquina} na {contador}º tentativa. ####")
            break
        else:
            print("Tente novamente: ")
            contador += 1
            continue    

    
            
    
            
        