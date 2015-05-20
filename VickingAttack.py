__author__ = 'João Pedro Sá Medeiros' , 'Ian Lanza'
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import  randint
from PPlay.collision import *
from PPlay.animation import *
from PPlay.sound import  *
from pygame import *
#Subprogramas
def inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY):
    #animacao = total de imagens da animacao
    #animacaoInicial = quadro inicial da animacao
    #animacaoFinal = quadro final da animacao
    #posX e posY = posições iniciais que o inimigo começa
    soldado1 = Sprite(endereco, animacao)
    larguraSol1 = soldado1.width
    alturaSol1 = soldado1.height
    soldado1.set_sequence(animacaoInicial, animacaoFinal) # Tem que ser até apenas o 5 pois o Sprite está com problema.
    soldado1.set_total_duration(duracao)
    soldado1.set_position(posX, posY-alturaSol1)
    return soldado1, alturaSol1
def movimentacao(posX, posY, objeto, velocidadeObjeto):
    #Condições diferentes para cada cenário, tais coordenadas valem para o cenário 1.3.5
    #Troca de animação dependendo da direção do movimento(A fazer...)
    velX = 0
    velY = 0
    if (int(posX) < 390) and (int(posY) in range(90, 150)):
        objeto.move_x(velocidadeObjeto)
        objeto.move_y(0)
        velX = velocidadeObjeto
        velY = 0
    if int(posX) in range(390, 395) and int(posY) in range(90, 330):
        objeto.move_x(0)
        objeto.move_y(velocidadeObjeto)
        velX = 0
        velY = velocidadeObjeto
    if int(posX) in range(423, 60, -1) and int(posY) in range(250, 265):
        objeto.move_x(-velocidadeObjeto)
        objeto.move_y(0)
        velX = -velocidadeObjeto
        velY = 0
    if (int(posX) < 80) and int(posY) in range(250, 500):
        objeto.move_x(0)
        objeto.move_y(velocidadeObjeto)
        velX = 0
        velY = velocidadeObjeto
    if (int(posX) in range(60, 630)) and (int(posY) in range(415, 500)):
        objeto.move_x(velocidadeObjeto)
        objeto.move_y(0)
        velX = velocidadeObjeto
        velY = 0
    if (int(posX) in range(630, 635)) and int(posY) in range(475, 255, -1):
        objeto.move_x(0)
        objeto.move_y(-velocidadeObjeto)
        velX = 0
        velY = -velocidadeObjeto
    if int(posX) in range(630, 460, -1) and int(posY) in range(250, 260):
        objeto.move_x(-velocidadeObjeto)
        objeto.move_y(0)
        velX = -velocidadeObjeto
        velY = 0
    if int(posX) in range(460, 465) and int(posY) in range(258, 90, -1):
        objeto.move_x(0)
        objeto.move_y(-velocidadeObjeto)
        velX = 0
        velY = -velocidadeObjeto
    if int(posX) in range(460, 660) and int(posY) in range(90, 100):
        objeto.move_x(velocidadeObjeto)
        objeto.move_y(0)
        velX = velocidadeObjeto
        velY = 0
    if int(posX) in range(660, 670) and int(posY) in range(90, 100):
        print("PERDEU")
    return velX, velY

def mudancaDeAnimacao(objeto, velX, velY, vetorSprites, verificadorObj):
    posX = 0
    posY = 0
    altura = objeto.height
    if verificadorObj[0] == 0:
        if velX < 0:
            posX = objeto.x
            posY = objeto.y
            objeto, altura = inimigo(vetorSprites[1], 9, 0, 9, 1000, posX, posY + altura)
            verificadorObj[0] = 1
    if velY != 0:
        verificadorObj[0] = 0
    if verificadorObj[1] == 0:
        if velY > 0 :
            posX = objeto.x
            posY = objeto.y
            objeto, altura = inimigo(vetorSprites[2], 9, 0, 9, 1000, posX, posY + altura)
            verificadorObj[1] = 1
    if velX != 0:
        verificadorObj[1] = 0
    posX = objeto.x
    posY = objeto.y
    if (verificadorObj[2] == 0 and posY in range(415, 500)) or (verificadorObj[2] ==0 and int(posX) in range(460, 660) and int(posY) in range(90, 100)):
        if velX > 0:
            posX = objeto.x
            posY = objeto.y
            objeto, altura = inimigo(vetorSprites[0], 9, 0, 9, 1000, posX, posY + altura)
            verificadorObj[2] = 1
    if velY != 0:
        verificadorObj[2] = 0
    if verificadorObj[3] == 0:
        if velY < 0 :
            posX = objeto.x
            posY = objeto.y
            objeto, altura = inimigo(vetorSprites[3], 9, 0, 9, 1000, posX, posY + altura)
            verificadorObj[3] = 1
    if velX != 0:
        verificadorObj[3] = 0
    return objeto

#Fundo
background = GameImage("imagens\cenarios\cenario1.3.5.png")
background.set_position(0, 0)
larguraFundo = background.width
alturaFundo = background.height
#Janela
larguraJanela = 800
alturaJanela = 608
janela = Window(larguraFundo, alturaFundo)
janela.set_title("Viking Attack")
janela.set_background_color((0, 0, 0))

#Define o ícone obs:(Não funciona completamente)
icone = pygame.image.load("imagens\icone.jpg").convert_alpha()
pygame.display.set_icon(icone)
#Inimigos
soldado1, alturaSol1 = inimigo("imagens\soldado1\soldado1lado1.png", 9, 0, 9, 1000, 0, 140)
vetorSoldado1 =["imagens\soldado1\soldado1lado1.png", "imagens\soldado1\soldado1lado2.png", "imagens\soldado1\soldado1frente.png", "imagens\soldado1\soldado1costas.png"] #Vetor para ser usado posteriormente
vetorVerificadoresSol1 = [0, 0, 0, 0]
#Musica
kingarthur = Sound("musicas\kingarthur.ogg")
kingarthur.set_volume(10)

#GameLoop
while True:
    janela.set_background_color((0, 0, 0))
    background.draw()
    #Inimigos
    #Soldado1
    soldado1.move_x(0)
    soldado1.move_y(0)
    soldado1.update()
    soldado1.draw()
        #Movimentacao do Soldado1
    posXSol1 = soldado1.x
    posYSol1 = soldado1.y
    velX, velY = movimentacao(posXSol1, posYSol1, soldado1, 1)
    print(velX, velY)
        #Troca de animações do Soldado 1
    soldado1 = mudancaDeAnimacao(soldado1, velX, velY, vetorSoldado1, vetorVerificadoresSol1)
    #Musica
    kingarthur.play()
    janela.update()