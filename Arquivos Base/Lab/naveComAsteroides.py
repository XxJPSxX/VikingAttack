__author__ = '115031035'
__author__ = '115031035'
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import  randint
from PPlay.collision import *
from PPlay.animation import *


#Metade do largura da janela - Metade da Largura da Imagem, Metade da Altura da Janela - Metade da Altura da Imagem
janela = Window(512, 512)
janela.set_title("Janela Teste")
janela.set_background_color((0, 0, 0))

background = GameImage("space.jpg")


spaceFighter = Sprite("spacefighter.png", 4)
largura = spaceFighter.width
altura = spaceFighter.height
spaceFighter.set_position(240, 240)
spaceFighter.set_sequence(0, 4)
spaceFighter.set_total_duration(500)
SPACE_FIGHTER_SPEED = 100


asteroide = Sprite("asteroid.png", 8)
larguraAst = asteroide.width
alturaAst = asteroide.height
asteroide.set_position(0, randint(0, 512))
asteroide.set_sequence(0, 8)
asteroide.set_total_duration(2000)
velocidadeX = 0.5
velocidadeY = 0.5

def asteroideUpdate(objeto, velX, velY):
        posAstx = objeto.x
        posAsty = objeto.y
        objeto.move_x(velX)
        objeto.move_y(velY)
        if (posAstx < 0):
            velX = 0.5
        if (posAstx + alturaAst > 512 ):
            velX = -0.5
        if (posAsty < 0):
            velY = 0.5
        if (posAsty + larguraAst > 512):
            velY = -0.5
        objeto.update()
        objeto.draw()

while True:
    background.draw()
    if not (spaceFighter.collided(asteroide)):
        #Nave
        spaceFighter.move_key_x(SPACE_FIGHTER_SPEED * janela.delta_time())
        spaceFighter.move_key_y(SPACE_FIGHTER_SPEED * janela.delta_time())
        posx = spaceFighter.x
        posy = spaceFighter.y
        if (posx < 0):
            posx = 0
        if (posx + altura > 512 ):
            posx = 512-largura
        if (posy < 0):
            posy = 0
        if (posy + largura > 512):
            posy = 512-altura
        spaceFighter.set_position(posx, posy)
        spaceFighter.update()
        spaceFighter.draw()

        #Asteroide
        asteroideUpdate(asteroide, 0.5, 0.5)
        asteroideUpdate(asteroide, 0.2, 0.2)

        """
        posAstx = asteroide.x
        posAsty = asteroide.y
        asteroide.move_x(velocidadeX)
        asteroide.move_y(velocidadeY)
        if (posAstx < 0):
            velocidadeX = 0.5
        if (posAstx + alturaAst > 512 ):
            velocidadeX = -0.5
        if (posAsty < 0):
            velocidadeY = 0.5
        if (posAsty + larguraAst > 512):
            velocidadeY = -0.5
        asteroide.update()
        asteroide.draw()"""
    if (spaceFighter.collided(asteroide)):
        background = GameImage("perdeu.png")
    janela.update()
