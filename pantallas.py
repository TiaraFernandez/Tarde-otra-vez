from ast import While
from cProfile import label
from distutils.cmd import Command
from mimetypes import init
from configuracion import*
import pygame, sys

pygame.init()

#GATO
class Animacion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        gato_1 = pygame.image.load('pictures/Animation/1.png').convert_alpha()
        gato_2 = pygame.image.load('pictures/Animation/2.png').convert_alpha()
        gato_3 = pygame.image.load('pictures/Animation/3.png').convert_alpha()
        gato_4 = pygame.image.load('pictures/Animation/4.png').convert_alpha()
        gato_5 = pygame.image.load('pictures/Animation/5.png').convert_alpha()
        gato_6 = pygame.image.load('pictures/Animation/6.png').convert_alpha()
        gato_7 = pygame.image.load('pictures/Animation/7.png').convert_alpha()
        gato_8 = pygame.image.load('pictures/Animation/8.png').convert_alpha()
        gato_9 = pygame.image.load('pictures/Animation/9.png').convert_alpha()
        gato_10 = pygame.image.load('pictures/Animation/10.png').convert_alpha()
        gato_11 = pygame.image.load('pictures/Animation/11.png').convert_alpha()
        gato_12 = pygame.image.load('pictures/Animation/12.png').convert_alpha()
        gato_13 = pygame.image.load('pictures/Animation/13.png').convert_alpha()
        gato_14 = pygame.image.load('pictures/Animation/14.png').convert_alpha()
        gato_15 = pygame.image.load('pictures/Animation/15.png').convert_alpha()
        gato_16 = pygame.image.load('pictures/Animation/16.png').convert_alpha()
        gato_17 = pygame.image.load('pictures/Animation/17.png').convert_alpha()
        gato_18 = pygame.image.load('pictures/Animation/18.png').convert_alpha()
        gato_19 = pygame.image.load('pictures/Animation/19.png').convert_alpha()
        gato_20 = pygame.image.load('pictures/Animation/20.png').convert_alpha()
        gato_21 = pygame.image.load('pictures/Animation/21.png').convert_alpha()
        gato_22 = pygame.image.load('pictures/Animation/22.png').convert_alpha()
        gato_23 = pygame.image.load('pictures/Animation/23.png').convert_alpha()
        gato_24 = pygame.image.load('pictures/Animation/24.png').convert_alpha()
        gato_25 = pygame.image.load('pictures/Animation/25.png').convert_alpha()
        gato_26 = pygame.image.load('pictures/Animation/26.png').convert_alpha()
        gato_27 = pygame.image.load('pictures/Animation/27.png').convert_alpha()
        gato_28 = pygame.image.load('pictures/Animation/28.png').convert_alpha()
        gato_29 = pygame.image.load('pictures/Animation/29.png').convert_alpha()
        gato_30 = pygame.image.load('pictures/Animation/30.png').convert_alpha()
        gato_31 = pygame.image.load('pictures/Animation/31.png').convert_alpha()
        gato_32 = pygame.image.load('pictures/Animation/32.png').convert_alpha()
        gato_33 = pygame.image.load('pictures/Animation/33.png').convert_alpha()
        self.gato = [gato_1,gato_2,gato_3,gato_4,gato_5,gato_6,gato_7,gato_8,gato_9,gato_10,gato_11,gato_12,gato_13,gato_14,gato_15,gato_16,gato_17,gato_18,gato_19,gato_20,gato_21,gato_22,gato_23,gato_24,gato_25,gato_26,gato_27,gato_28,gato_29,gato_30,gato_31,gato_32,gato_33]
        self.gato_index = 0

        self.image = self.gato[self.gato_index]
        self.image = pygame.transform.scale(self.image,(300,300))
        self.rect = self.image.get_rect(center = (600,450))
    
    def animacion_state (self):
        self.gato_index +=0.1
        if self.gato_index >=len(self.gato): self.gato_index = 0
        self.image = self.gato[int(self.gato_index)]
        self.image = pygame.transform.scale(self.image,(300,300))

    def update(self):
       self.animacion_state()
gato = pygame.sprite.GroupSingle()
gato.add(Animacion())

#pantalla de inicio
def inicio():
    #fondo
    fondo = pygame.image.load('pictures/menu/background.png').convert()
    titulo = pygame.image.load('pictures/menu/titulo.png')
    instrucciones = pygame.image.load('pictures/Teclado y raton.png').convert()
    #Botones
    salir_normal= pygame.image.load('pictures/menu/salir_1.png').convert_alpha()
    salir_selec = pygame.image.load('pictures/menu/salir_2.png').convert_alpha()
    salir = salir_normal
    salir_rect = salir.get_rect(center=(890,452))

    jugar_normal = pygame.image.load('pictures/menu/jugar_1.png').convert_alpha()
    jugar_selec = pygame.image.load('pictures/menu/jugar_2.png').convert_alpha()
    jugar = jugar_normal
    jugar_rect = jugar.get_rect(center=(264,452))
    #musica
    pygame.mixer.music.load('music/copycat(revised).mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)
    #Cursor
    surf = pygame.image.load('pictures/menu/pointer.png').convert_alpha()
    while(1):
        #muestra fondo
        screen.blit(fondo,(0,0))
        screen.blit(titulo,(0,0))
        screen.blit(salir,salir_rect)
        screen.blit(jugar,jugar_rect)
        gato.draw(screen)
        gato.update()
        #cursor
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)
        pygame.display.update()
        #posicon del curor
        comando = pygame.event.poll()
        cursor_pos = pygame.mouse.get_pos()
        #Boton salir
        if salir_rect.collidepoint(cursor_pos):
            if(comando.type == pygame.MOUSEBUTTONDOWN):
                if comando.button == 1:
                    pygame.quit()
                    quit()
            if salir != salir_selec:
                salir = salir_selec
        elif salir != salir_normal:
            salir = salir_normal
        #Boton jugar
        if jugar_rect.collidepoint(cursor_pos):
            if(comando.type == pygame.MOUSEBUTTONDOWN):
                if comando.button == 1:
                    pygame.mixer.music.fadeout(3000)
                    return 1
            if jugar != jugar_selec:
                jugar = jugar_selec
        elif jugar != jugar_normal:
            jugar = jugar_normal
        
#Pantalla de fin del juego, si pierde.
def finJuego():
    pantallaFin = pygame.image.load('pictures/llegada tarde screen.png').convert()
    #Botones
    salir_normal= pygame.image.load('pictures/menu/salir_1.png').convert_alpha()
    salir_selec = pygame.image.load('pictures/menu/salir_2.png').convert_alpha()
    salir = salir_normal
    salir_rect = salir.get_rect(center=(600,452))
    #musica
    pygame.mixer.music.load('music/lost.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    #Cursor
    surf = pygame.image.load('pictures/menu/pointer.png').convert_alpha()
    while(1):
        screen.blit(pantallaFin,(0,0))
        screen.blit(salir,salir_rect)
        #ve las teclas que se presionan
        pygame.display.update()
        #cursor
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)
        pygame.display.update()
        #posicon del curor
        comando = pygame.event.poll()
        cursor_pos = pygame.mouse.get_pos()
        #Boton salir
        if salir_rect.collidepoint(cursor_pos):
            if(comando.type == pygame.MOUSEBUTTONDOWN):
                if comando.button == 1:
                    pygame.quit()
                    quit()
            if salir != salir_selec:
                salir = salir_selec
        elif salir != salir_normal:
            salir = salir_normal

        if comando.type == pygame.QUIT:
                pygame.quit()
                quit()

#Pantalla de llegada a tiempo, si gana.
def llegadaATiempo():
    pantallaATiempo = pygame.image.load('pictures/llegada a tiempo.png').convert()
    pygame.mixer.music.load('music/game.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    while(1):
        screen.blit(pantallaATiempo,(0,0))
        pygame.display.update()
        comando = pygame.event.poll()
        if (comando.type== pygame.KEYDOWN):
            if(comando.key == pygame.K_RETURN):
                return 1
        if comando.type == pygame.QUIT:
                pygame.quit()
                quit()
        