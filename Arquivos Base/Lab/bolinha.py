__author__ = '115031035'
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *


#Metade do largura da janela - Metade da Largura da Imagem, Metade da Altura da Janela - Metade da Altura da Imagem
janela = Window(512, 512)
janela.set_title("Janela Teste")
janela.set_background_color((0, 0, 0))

background = GameImage("space.jpg")


asteroide = Sprite("asteroid.png", 8)
larguraAst = asteroide.width
alturaAst = asteroide.height
asteroide.set_position(0, 256)
asteroide.set_sequence(0, 8)
asteroide.set_total_duration(2000)
velocidadeX = 0.5
velocidadeY = 0.5

while True:
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
    background.draw()
    asteroide.update()
    asteroide.draw()
    janela.update()