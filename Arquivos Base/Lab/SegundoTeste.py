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


SpaceFighter = Sprite("spacefighter.png", 4)
SpaceFighter.set_sequence(0, 4)
SpaceFighter.set_total_duration(500)
SPACE_FIGHTER_SPEED = 100

while True:
    background.draw()
    SpaceFighter.move_key_x(SPACE_FIGHTER_SPEED * janela.delta_time())
    SpaceFighter.move_key_y(SPACE_FIGHTER_SPEED * janela.delta_time())
    SpaceFighter.update()
    SpaceFighter.draw()
    janela.update()
