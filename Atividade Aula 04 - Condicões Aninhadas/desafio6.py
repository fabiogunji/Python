
#DESAFIO 06

#Crie um programa que faça o computador jogar Jokenpô com

import random

dicionario = {0:"Pedra", 1:"Papel", 2:"Tesoura"}

acertou = False

try:
    while acertou == False:
        
        jogadaComputador = random.randint(0,2)
    
        jogador = int(input("Entre com um número para jogar: 0 - Pedra | 1 - Papel | 2 - Tesoura: "))
        
        if dicionario[jogadaComputador] == "Pedra" and dicionario[jogador] == "Papel":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True
        elif dicionario[jogadaComputador] == "Papel" and dicionario[jogador] == "Pedra":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True 
             
        elif dicionario[jogadaComputador] == "Pedra" and dicionario[jogador] == "Tesoura":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True 
        elif dicionario[jogadaComputador] == "Tesoura" and dicionario[jogador] == "Pedra":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")        
            print("_____________________________________________________________________________________________")
            acertou = True        
                
        elif dicionario[jogadaComputador] == "Tesoura" and dicionario[jogador] == "Papel":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True
        elif dicionario[jogadaComputador] == "Papel" and dicionario[jogador] == "Tesoura":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True   
                
        elif dicionario[jogadaComputador] == "Pedra" and dicionario[jogador] == "Tesoura":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True  
        elif dicionario[jogadaComputador] == "Tesoura" and dicionario[jogador] == "Pedra":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True  
        
        elif dicionario[jogadaComputador] == dicionario[jogador]:
            print("_____________________________________________________________________________________________")
            print(f"Empate! - Comnputador: {dicionario[jogadaComputador]} e Jogador: {dicionario[jogador]}")
            print("_____________________________________________________________________________________________")
                  
       
except:
    print("Entre com valores válidos")






