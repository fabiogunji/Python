# DESAFIO 02

# Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatórios. 
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.

import random

listaJogadores = []
dcJogadores = {}

for i in range(0,5):
    listaUsuario = []    
    nome = input(f"Entre com o nome do {i+1}º jogador: ")
    valorDado = random.randint(1,6)
    listaUsuario.append(nome)
    listaUsuario.append(valorDado)
    
    listaJogadores.append(listaUsuario)

dcJogadores = tuple(listaJogadores)
    
print(dcJogadores)
