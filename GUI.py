import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)


boardDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Connect 4")

boardLength = 7
boardHeight = 6

gameEnd = False

boardDisplay.fill(WHITE)
for i in range(1,boardLength+1):
    for j in range(1,boardHeight+1):
        pygame.draw.circle(boardDisplay,BLACK,[100 * i, 80 * j],30)


while not gameEnd:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameEnd = True

    pygame.display.update()

pygame.quit()