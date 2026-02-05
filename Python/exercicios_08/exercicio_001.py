#Introdução ao Pygame
import pygame
import pygame.draw
import random

#Inicializar o pygame
pygame.init()

vermelho = 255
verde = 255
azul = 255

#Configurações da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Exemplo com pygame.")

#definindo um clock para controlar FPS 
clock = pygame.time.Clock()
FPS = 120

#Definindo a posição x e y como no centro da tela
posicao_x_retangulo = LARGURA// 2
posicao_y_retangulo = ALTURA// 2

#Definindo a velociade em x e y do retangulo.
velocidade_x_retangulo = 2
velocidade_y_retangulo = 2

#Detecção de colisão com as bordas da tela


    
rodando = True
while rodando:
    #Inicio loop Procurando por eventos
    for evento in pygame.event.get():
        #SE o evento fechar o jogo existir
        if evento.type == pygame.QUIT:
            #Muda a variável para false (Fecha o programa)
            rodando = False
        #Fim do loop de eventos
    #Lógica de movimento do retangulo.
    posicao_x_retangulo += velocidade_x_retangulo
    posicao_y_retangulo += velocidade_y_retangulo
    
    if posicao_x_retangulo >= (LARGURA-25) or posicao_x_retangulo <= 0:
        velocidade_x_retangulo *= -1
        vermelho = random.randint(0, 255)
        verde = random.randint(0, 255)
        azul = random.randint(0, 255)
    
    if posicao_y_retangulo >= (ALTURA - 25) or posicao_y_retangulo <=0:
        velocidade_y_retangulo *= -1
        vermelho = random.randint(0, 255)
        verde = random.randint(0, 255)
        azul = random.randint(0, 255)
    tela.fill(( 0, 0, 0))
       #Aqui desenhamos os elementos gráficos.
    pygame.draw.rect(tela, (vermelho , verde, azul), (posicao_x_retangulo, posicao_y_retangulo, 25, 25))
   # pygame.draw.rect(tela,(255, 255, 255), (420,300, 10, 5))
    #pygame.draw.rect(tela,(255, 255, 255), (400,320, 5, 10))
    #pygame.draw.rect(tela,(255, 255, 255), (380,300, 10, 5))
    #pygame.draw.rect(tela,(255, 255, 255), (400,280, 5, 10))
    
    #Atualizalizando com FPS
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

    