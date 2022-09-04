from mimetypes import init
import pygame, sys
from pygame.locals import*
from pantallas import*
from configuracion import*

pygame.init()

#poner una varriable para la posicion en x de los obstaculos que cambie entre los carrile, la pos y siempre la misma al principio

#IMAGENES
#fondo del main game
calle = pygame.image.load("pictures/Game screen/gameBackground street.png").convert_alpha()
costadoFondo = pygame.image.load ('pictures/Game screen/gameBackground_costados.png').convert_alpha()
#obstaculos
pos_y=200
pos_x = 600
conosImage = pygame.image.load('pictures/Game screen/conos.png').convert_alpha()
charcoImage = pygame.image.load('pictures/Game screen/charco.png').convert_alpha()
posteImage = pygame.image.load('pictures/Game screen/poste.png').convert_alpha()

inicio() #muestra la pantalla de inicio(from 'pantallas')

while (1):
    #Variables
    FPS = 40
    reloj = pygame.time.Clock()
    corriendo = 1
    #musica
    pygame.mixer.music.load('music/Catsong.mp3')#cambiar el volumen y arreglar el cambio de cancion entre
    pygame.mixer.music.play(-1)
    
    #Game loop
    while (corriendo):
        for event in pygame.event.get():#checkea si se cierra el juego
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        #Fondo de pantalla
        screen.blit(calle,(0,0))
        screen.blit(costadoFondo,(0,0))
        
        pygame.display.update()
        reloj.tick(FPS)
    finJuego()#muestra la pantalla de llegada tarde
