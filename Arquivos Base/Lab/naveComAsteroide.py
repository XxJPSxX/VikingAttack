__author__ = '115031035'
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import  *
from PPlay.collision import *
from PPlay.animation import *


#Metade do largura da janela - Metade da Largura da Imagem, Metade da Altura da Janela - Metade da Altura da Imagem
janela = Window(512, 512)
janela.set_title("Janela Teste")
janela.set_background_color((0, 0, 0))

background = GameImage("space.jpg")


#Nave
spaceFighter = Sprite("spacefighter.png", 4)
largura = spaceFighter.width
altura = spaceFighter.height
spaceFighter.set_position(240, 240)
spaceFighter.set_sequence(0, 4)
spaceFighter.set_total_duration(500)
SPACE_FIGHTER_SPEED = 500

#Asteroides
    #Asteroide1
asteroide = Sprite("asteroid.png", 8)
larguraAst = asteroide.width
alturaAst = asteroide.height
asteroide.set_position(0, randint(0, 512))
asteroide.set_sequence(0, 8)
asteroide.set_total_duration(2000)
velocidadeX = 0.5
velocidadeY = 0.5
    #Asteroide2
asteroide2 = Sprite("asteroid.png", 8)
asteroide2.set_position(0, randint(0, 512))
asteroide2.set_sequence(0, 8)
asteroide2.set_total_duration(2000)
velocidadeX2 = 0.3
velocidadeY2 = 0.3
#Subprogramação do Asteroide

def asteroides(nome, posX, posY, velX, velY):
    nome = Sprite("asteroid.png", 8)
    larguraAst = asteroide.width
    alturaAst = asteroide.height
    nome.set_position(posX, posY)
    nome.set_sequence(0, 8)
    nome.set_total_duration(2000)
    velocidadeX = velX
    velocidadeY = velY
    """while True:
        posAstx = asteroide.x
        posAsty = asteroide.y
        asteroide.move_x(velocidadeX)
        asteroide.move_y(velocidadeY)
        if (posAstx < 0):
            velX = 0.5
        if (posAstx + alturaAst > 512 ):
            velX = -0.5
        if (posAsty < 0):
                velY = 0.5
        if (posAsty + larguraAst > 512):
            velY = -0.5
        asteroide.update()
        asteroide.draw()"""
    return asteroide, velocidadeX, velocidadeY, larguraAst, alturaAst

#asteroides("ast1", 0, randint(0, 512), 0.5, 0.5)
#asteroides("ast2", 0, randint(0, 512), 0.5, 0.5)


#GameLoop
while True:
    background.draw()
    if (not (spaceFighter.collided(asteroide)) or not((spaceFighter.collided(asteroide)))) == True:
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

        #Asteroides
            #Asteroide1
        posAstx = asteroide.x
        posAsty = asteroide.y
        asteroide.move_x(velocidadeX)
        asteroide.move_y(velocidadeY)
        if (posAstx < 0):
            velocidadeX = uniform(0.1, 1)
        if (posAstx + alturaAst > 512 ):
            velocidadeX = uniform(-0.1, -1)
        if (posAsty < 0):
            velocidadeY = uniform(0.1, 1)
        if (posAsty + larguraAst > 512):
            velocidadeY = uniform(-0.1, -1)
        asteroide.update()
        asteroide.draw()
            #Asteroide2
        posAstx = asteroide2.x
        posAsty = asteroide2.y
        asteroide2.move_x(velocidadeX2)
        asteroide2.move_y(velocidadeY2)
        if (posAstx < 0):
            velocidadeX2 = uniform(0.1, 1)
        if (posAstx + alturaAst > 512 ):
            velocidadeX2 = uniform(-0.1, -1)
        if (posAsty < 0):
            velocidadeY2 = uniform(0.1, 1)
        if (posAsty + larguraAst > 512):
            velocidadeY2 = uniform(-0.1, -1)
        asteroide2.update()
        asteroide2.draw()
    if ((spaceFighter.collided(asteroide)) or spaceFighter.collided(asteroide2)) == True :
        background = GameImage("perdeu.png")
        while True:
            background.draw()
            janela.update()

    janela.update()
