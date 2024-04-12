# DESAFIO 02

# Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatórios. 
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from operator import itemgetter

listaJogadores = []
dcJogadores = {}
listaVlrRandomico = []

for i in range(0,30):
    valorDado = randint(1,6)
    if valorDado in listaVlrRandomico:
        continue
    else:
        listaVlrRandomico.append(valorDado)  

for i in range(0,5):
    listaUsuario = [] 
    contador = i+1  
    nome = input(f"Entre com o nome do {contador}º jogador: ")
    valorDado = listaVlrRandomico[contador]#randint(1,6)
    
    listaUsuario.append(nome)
    listaUsuario.append(valorDado)
    
    listaJogadores.append(listaUsuario)

dcJogadores = dict(listaJogadores)

# ordenando o dicionario
# sorted (Quem?, Qual Chave?, Quer inverter a ordem?)
ranking = sorted(dcJogadores.items(), key=itemgetter(1),reverse=True)
   
for nome,valor in enumerate(ranking):     
     print(f"Nome do jogador: {nome} e Valor do dado: {valor}")
