import pygame

pygame.init()

LARGURA_TELA = 800
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
verde = (0,255,0)
cinza = (100,100,100)
rodar = True

while rodar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False

    # preencher tela com uma cor para limpar frame anterior (importante se houver movimento)
    tela.fill(cinza)

    # desenhar círculo
    pygame.draw.circle(tela, verde, (370,250), 30)

    pygame.display.update()

pygame.quit()
