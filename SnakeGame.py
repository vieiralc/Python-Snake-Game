# Created by: Lucas Vieira
# imports
import pygame, sys, random, time

check_errors = pygame.init() # Se retornar (6, 0): 6 tarefas completas com sucesso
                             # 0 Erros

# verificar se houve erros
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1) #sai do programa caso haja erros de inicializacao
else:
    print("(+) PyGame successfully initialized!")

playSurface = pygame.display.set_mode((720,460)) #define a resolução para 720x460
pygame.display.set_caption('Aspirador de poh') # Cabeçalho da janela
#time.sleep(5) faz a tela "dormir" por 5seg

# Definindo as cores que serão usadas (r,g,b)
red = pygame.Color(255,0,0) # gameover
green = pygame.Color(0,255,0)  # snake color
black = pygame.Color(0,0,0) # font
white = pygame.Color(255,255,255) # background
brown = pygame.Color(165,42,42) # food

# Controlador de frames FPS
pfsController = pygame.time.Clock()

# Variáveis importantes
snakePos = [100,50] # posicao inical da snake
snakeBody = [[100,50],[90,50],[80,50]] # posicao inicial do corpo da snake

# define a posicao da comida randomicamente, posicao e sempre divisivel por 10
# o alcance da posicao e de 1 ate 720 no eixo x
# 1 ate 460 no eixo y
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True # Para saber se printou ou nao uma food na tela

direction = 'RIGHT' #inicialmente a snake começará a andar para a direita
changeto = direction

score = 0

# Funcao para sair do programa ***
def gameOver():
    myFont = pygame.font.SysFont('monaco',72) # definindo tipo de fonte
    # texto a ser renderizado na tela, (texto, anti-aliasing, cor do texto)
    GOsurf = myFont.render('Game Over!', True, red)
    #posicionando um retangulo na tela
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,25)
    playSurface.blit(GOsurf,GOrect)
    showScore(0)
    pygame.display.flip() # atualizar a tela para exibir informações
    time.sleep(4) # faz a tela "dormir" por 4s
    # e dps sai do programa:
    pygame.quit() #pygame exit
    sys.exit() #console exit

# evens = ocasioes especiais quando algo acontece

# funcao para mostrar pontos na tela
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 28)
    Ssurf = sFont.render('Score: {0}'.format(score), True, black) #
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80,10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)

# Lógica principal do programa
while True:
    # verificando quais teclas o usuario digitou

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # validando as direções digitadas
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Atualizar posicao da snake
    if direction == 'RIGHT':
        snakePos[0] += 10 # aumenta uma casa do eixo x
    if direction == 'LEFT':
        snakePos[0] -= 10 # diminui uma casa do eixo x
    if direction == 'UP':
        snakePos[1] -= 10 # diminui uma casa do eixo y
    if direction == 'DOWN':
        snakePos[1] += 10 # aumenta uma casa do eixo y

    # Snake body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    #Background
    playSurface.fill(white)

    # Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1, 70)*10, random.randrange(1, 44)*10]
    foodSpawn = True

    #Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green,
        pygame.Rect(pos[0],pos[1],10,10))

    #Draw Food
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))

    # Bound
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    #Check if snake hit its own body
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    #common stuff
    showScore()
    pygame.display.flip()
    pfsController.tick(23)