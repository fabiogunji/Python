# DESAFIO 04

# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint

valorComputador = 0
valorJogador = 0

def validaParImpar(jogador, computador,escolhaJogador):
    soma = jogador + computador
    
    if soma % 2 == 0:
        if escolhaJogador == "P":
            print(f"#### O jogador GANHOU! {jogador} + {computador} = {soma}, O resultado é PAR ####")
            return 0
        else:
            print(f"#### O computador GANHOU! {jogador} + {computador} = {soma}, O resultado é PAR ####")
            return 1
    else:
        if escolhaJogador == 'I':
            print(f"#### O jogador GANHOU! {jogador} + {computador} = {soma}, O resultado é IMPAR ####")
            return 0
        else:
            print(f"#### O computador GANHOU! {jogador} + {computador} = {soma}, O resultado é IMPAR ####")
            return 1


while True:
    escolhaJogador = (input("Par ou impar? [P/I]: ")).upper()
    
    if escolhaJogador == "P":
        print(f">>> Jogador escolheu PAR.")
        valorJogador = int(input("Entre com um valor inteiro PAR: "))
        
        print(">>> Maquina joga com IMPAR.")                         
        
        while True:
            computador = randint(0,10)           
    
            if (computador % 2) != 0:
                escolhaComputador = computador
            break
            
                
        
    elif escolhaJogador == "I":
        print(f">>> Jogador escolheu IMPAR.")            
        valorJogador = int(input("Entre com um valor inteiro IMPAR: "))
        print(">>> Maquina joga com PAR.")
        
        while True:
            computador = randint(0,10)           
    
            if (computador % 2) == 0:
                escolhaComputador = computador
            break   
    else:
        print("Favor entrar con P ou I.")   
    
    retorno = validaParImpar(valorJogador, computador,escolhaJogador)
    
    if retorno == 0:
        continue
    else:
        break
        
        
    
    