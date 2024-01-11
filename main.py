#Fernandez Totolo Tiara Irina 
#Version final
#05/09/2022-09/11/2022

from email.mime import image
import math
from mimetypes import init
from secrets import choice
from turtle import Screen
import pygame, sys, random
from pygame.locals import*
from pantallas import*
from configuracion import*

pygame.init()

#GATO
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        jugador_walk_1 = pygame.image.load('pictures/Game screen/sachy animation/1.1.png').convert_alpha()
        jugador_walk_2 = pygame.image.load('pictures/Game screen/sachy animation/1.2.png').convert_alpha()
        jugador_walk_3 = pygame.image.load('pictures/Game screen/sachy animation/1.3.png').convert_alpha()
        jugador_walk_4 = pygame.image.load('pictures/Game screen/sachy animation/1.4.png').convert_alpha()
        jugador_walk_5 = pygame.image.load('pictures/Game screen/sachy animation/1.5.png').convert_alpha()
        jugador_walk_6 = pygame.image.load('pictures/Game screen/sachy animation/1.6.png').convert_alpha()
        self.jugador_walk = [jugador_walk_1,jugador_walk_2,jugador_walk_3,jugador_walk_4,jugador_walk_5,jugador_walk_6]
        self.jugador_index = 0

        self.image = self.jugador_walk[self.jugador_index]
        self.rect = self.image.get_rect(center = (246,400))
        self.mask = pygame.mask.from_surface(self.image)

    def jugador_input(self): #Funcion para las teclas
        self.vx, self.vy = 0,0
        tecla = pygame.key.get_pressed() #se crea una variable para ver que tecla se presiona
        #TECLAS
        if tecla[pygame.K_DOWN]:
            self.vy = 8
        if tecla [pygame.K_UP]:
            self.vy =-8
        if self.vx != 0:
            self.vx /= 1.414
        if self.vy != 0:
            self.vy /=1.414
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.top <= 192:#Limita margen de arriba
            self.rect.top = 192
        if self.rect.bottom >= 614:#Limita margen abajo
            self.rect.bottom = 614
    
    def animacion_state (self):
        self.jugador_index +=0.1
        if self.jugador_index >=len(self.jugador_walk): self.jugador_index = 0
        self.image = self.jugador_walk[int(self.jugador_index)]

    def update(self):
       self.jugador_input()
       self.animacion_state()
jugador = pygame.sprite.GroupSingle()
jugador.add(Jugador())

#OBSTACULOS
class Obstaculos(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'caja':
            self.image = pygame.image.load('pictures/Game screen/caja.png').convert_alpha()
            y_pos = choice([450,352,554])
        elif type == 'charco':
            self.image = pygame.image.load('pictures/Game screen/charco.png').convert_alpha()
            y_pos = choice([450,352,554])
        else:
            self.image = pygame.image.load('pictures/Game screen/poste.png').convert_alpha()
            y_pos = 101

        self.rect = self.image.get_rect(center = (1300,y_pos))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
obstaculo_group = pygame.sprite.Group()
obstaculos_rect_list = []

#TIMER
obstaculo_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstaculo_timer,1400)

#Colisiones
def collisions_sprite():
    if pygame.sprite.spritecollide(jugador.sprite, obstaculo_group,False,pygame.sprite.collide_mask):
        obstaculo_group.empty()
        pygame.time.wait (350)
        return False
    else: return True

#FONDO 
calle = pygame.image.load('pictures/Game screen/gameBackground street.png').convert_alpha()
fondo = pygame.image.load ('pictures/Game screen/gameBackground_costados.png').convert_alpha()
fondo_ancho = fondo.get_width()
fondo_rect = fondo.get_rect()
teclas = pygame.image.load('pictures/Game screen/teclas.png').convert_alpha()
teclas_rect = teclas.get_rect(center=(1100,50))


#VARIABLES
corriendo = True
scroll = 0
tiles = math.ceil(ANCHO/fondo_ancho)+1
max_tiempo = 30
start_time = pygame.time.get_ticks()

inicio() 

#Main game loop
while (1):
    for event in pygame.event.get():#checkea si se cierra el juego
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if corriendo:
            if event.type == obstaculo_timer:
                obstaculo_group.add(Obstaculos(choice(['caja','poste','charco'])))
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                corriendo = True
    
    if corriendo:
        #DIBUJO
        screen.blit(calle,(0,0))
        #ANIMACION FONDO
        for i in range(0, tiles):
            screen.blit(fondo, (i * fondo_ancho + scroll, 0))
            fondo_rect.x = i * fondo_ancho + scroll
        scroll -= 5 #scroll fondo
        if abs(scroll) > fondo_ancho: #reset scroll
            scroll = 0
        
        obstaculo_group.draw(screen)
        obstaculo_group.update()

        jugador.draw(screen)
        jugador.update()
        
        screen.blit(teclas,teclas_rect)

        corriendo = collisions_sprite()
    else: finJuego()

    #Update
    pygame.display.flip()
    pygame.display.update()
    reloj.tick(FPS)