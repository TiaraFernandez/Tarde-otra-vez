from ast import While
from cProfile import label
from distutils.cmd import Command
from mimetypes import init
from configuracion import*
import pygame, sys

pygame.init()

#pantalla de inicio
def inicio():
    pantallaInicio = pygame.image.load('pictures/title screen.png').convert()
    pygame.mixer.music.load('music/copycat(revised).mp3')
    pygame.mixer.music.play(-1)
    while(1):
        screen.blit(pantallaInicio,(0,0))
        label = fuente_kitto.render("Presione 'Enter' para iniciar", 1, (0,0,0))
        screen.blit(label,(450,450))
        pygame.display.update()
        comando = pygame.event.poll()
        if (comando.type == pygame.KEYDOWN):
            if(comando.key == pygame.K_RETURN):
                return 1
        if comando.type == pygame.QUIT:
            pygame.quit()
            quit()

#Pantalla de fin del juego, si pierde.
def finJuego():
    pantallaFin = pygame.image.load('pictures/llegada tarde screen.png').convert()
    pygame.mixer.music.load('music/lost.mp3')
    pygame.mixer.music.play(-1)
    while(1):
        screen.blit(pantallaFin,(0,0))
        #ve las teclas que se presionan
        pygame.display.update()
        comando = pygame.event.poll()
        if (comando.type== pygame.KEYDOWN):
            if(comando.key == pygame.K_RETURN):
                return 1
        if comando.type == pygame.QUIT:
                pygame.quit()
                quit()
