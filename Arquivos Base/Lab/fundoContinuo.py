__author__ = '115031035'
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import  randint
from PPlay.collision import *
from PPlay.animation import *
from pygame import *


#Metade do largura da janela - Metade da Largura da Imagem, Metade da Altura da Janela - Metade da Altura da Imagem


#Fundo
scrollSpeed = 30
fundoPosX = 0
fundoPosY = 0
background = GameImage("fundoMadeira2.jpg")
background.set_position(fundoPosX, fundoPosY)
larguraFundo = background.width
alturaFundo = background.height
#Fundo2
background2 = GameImage("fundoMadeira2.jpg")
background2.set_position(fundoPosX, fundoPosY-alturaFundo)


#Janela, teve que ser depois do Fundo pois é dependente de suas variáveis
janela = Window(larguraFundo, alturaFundo)
janela.set_title("Fundo Contínuo")
janela.set_background_color((0, 0, 0))
icon = pygame.image.load("ball.png").convert_alpha()
pygame.display.set_icon(icon)

#Nave
spaceFighter = Sprite("spacefighter.png", 4)
larguraNave = spaceFighter.width
alturaNave = spaceFighter.height
spaceFighter.set_position((larguraFundo-larguraNave)/2, (alturaFundo-alturaNave)/2)
spaceFighter.set_sequence(0, 4)
spaceFighter.set_total_duration(500)
SPACE_FIGHTER_SPEED = 500

while True:
    #Fundo
    janela.set_background_color((0, 0, 0))
    background.set_position(fundoPosX, fundoPosY)
    background2.set_position(fundoPosX, fundoPosY-alturaFundo)
    background2.draw()
    background.draw()

    fundoPosY = fundoPosY + scrollSpeed*janela.delta_time()
    posFundo1Y = background.y
    if int(posFundo1Y) == alturaFundo+1: #Sem o int não funciona pois o valor em ponto flutuante não é um valor exato
        fundoPosY = 0
    #Nave
    spaceFighter.move_key_x(SPACE_FIGHTER_SPEED * janela.delta_time())
    spaceFighter.move_key_y(SPACE_FIGHTER_SPEED * janela.delta_time())
    posx = spaceFighter.x
    posy = spaceFighter.y
    if (posx < 0):
        posx = 0
    if (posx + alturaNave > larguraFundo ):
        posx = larguraFundo-larguraNave
    if (posy < 0):
        posy = 0
    if (posy + larguraNave > alturaFundo):
        posy = alturaFundo-alturaNave
    spaceFighter.set_position(posx, posy)
    spaceFighter.update()
    spaceFighter.draw()


    janela.update()