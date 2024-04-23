import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 480
largura = 640

# Definindo posições e tamanho de objetos
pos_y_retangulo = altura / 2
pos_x_retangulo = largura / 2
largura_retangulo = 30
altura_retangulo = 40

# Definindo posição e tamanho do circulo
pos_y_circulo = 40
pos_x_circulo = 20
raio_circulo = 10


# Criando a janela do game
tela = pygame.display.set_mode((largura,altura))

# definir o titulo da janela
pygame.display.set_caption("Criando Jogos")

while True:
    tela.fill((0,0,0))
    
    # Colocando os eventos no pygame
    for event in pygame.event.get():
        # Evento sair
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_UP:
                pos_y_retangulo -= 10
            
            if event.key == K_DOWN:
                pos_y_retangulo += 10
            
            if event.key == K_LEFT:
                pos_x_retangulo -= 10
            
            if event.key == K_RIGHT:
                pos_x_retangulo += 10
            
        
    
    pygame.draw.rect(tela, (0,0,255), (pos_x_retangulo,pos_y_retangulo,largura_retangulo, altura_retangulo))
    
    pygame.draw.circle(tela, (255,0,255), (pos_x_circulo,pos_y_circulo),raio_circulo)

    # Atualizar o jogo em toda a interação
    pygame.display.update()
    
    