__author__ = 'JPS'
import pygame, sys, os
from pygame import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
background =  pygame.image.load(os.path.join("imagens\menus\iniciar.png"))
player = pygame.image.load(os.path.join("imagens\Teste.png"))
player.set_colorkey( None, RLEACCEL )
player.set_alpha(128)
player.convert()

while True:

    screen.blit(background, (10, 10))
    screen.blit(player, (10, 10))
    pygame.display.flip()

pygame.quit()