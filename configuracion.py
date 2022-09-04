import pygame, sys

pygame.init()

#Config de la pantalla
ALTO = 600
ANCHO = 1200
screen= pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('¡Tarde otra vez!')
icono = pygame.image.load('pictures/icon.png').convert_alpha()
pygame.display.set_icon(icono) #icono del juego

#fonts
fuente_katto = pygame.font.Font('fonts/Katto-PersonalUse.otf',36)
fuente_kitto = pygame.font.Font('fonts/Kitto-PersonalUse.otf', 36)
