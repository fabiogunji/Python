import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 480
largura = 640

# Definindo posições e tamanho de objetos
pos_y = altura / 2
pos_x = largura / 2
largura_retangulo = 30
altura_retangulo = 40

# Criando a janela do game
tela = pygame.display.set_mode((largura,altura))

# definir o titulo da janela
pygame.display.set_caption("Criando Jogos")

while True:
    # Colocando os eventos no pygame
    for event in pygame.event.get():
        # Evento sair
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.rect(tela, (0,0,255), (pos_x,pos_y,largura_retangulo, altura_retangulo))

    # Atualizar o jogo em toda a interação
    pygame.display.update()
    
    