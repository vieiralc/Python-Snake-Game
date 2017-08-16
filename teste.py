import pygame, sys, time

# Play Surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game!')

#Colors
red = pygame.Color(255,0,0) #game over
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food

done = False
clock = pygame.time.Clock()
while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    playSurface.fill(white)

    pygame.draw.rect(playSurface,black,[25,35,680,400],5)

    pygame.display.flip()