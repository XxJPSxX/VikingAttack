__author__ = 'João Pedro Sá Medeiros' , 'Ian Lanza'
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import  randint
from PPlay.collision import *
from PPlay.animation import *
from PPlay.sound import  *
from PPlay.mouse import *
from pygame import *
#Subprogramas
def inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY):
    #animacao = total de imagens da animacao
    #animacaoInicial = quadro inicial da animacao
    #animacaoFinal = quadro final da animacao
    #posX e posY = posições iniciais que o inimigo começa
    soldado = Sprite(endereco, animacao)
    larguraSol = soldado.width
    alturaSol = soldado.height
    soldado.set_sequence(animacaoInicial, animacaoFinal) # Tem que ser até apenas o 5 pois o Sprite está com problema.
    soldado.set_total_duration(duracao)
    soldado.set_position(posX, posY-alturaSol)
    return soldado, alturaSol
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
    if int(posX) in range(460, 465) and int(posY) in range(261, 90, -1):
        objeto.move_x(0)
        objeto.move_y(-velocidadeObjeto)
        velX = 0
        velY = -velocidadeObjeto
    if int(posX) in range(460, 661) and int(posY) in range(90, 105):
        objeto.move_x(velocidadeObjeto)
        objeto.move_y(0)
        velX = velocidadeObjeto
        velY = 0
    if int(posX) in range(661, 670) and int(posY) in range(90, 105):
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
    if (verificadorObj[2] == 0 and posY in range(415, 500)) or (verificadorObj[2] ==0 and int(posX) in range(460, 661) and int(posY) in range(90, 101)):
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

def torre(imagemTorre, bloco):
    torre = GameImage(imagemTorre)
    larguraTorre = (torre.width/2)
    alturaTorre = (torre.height/2)+20 #Sem o +20 a imagem fica exatamente no meio, com o +20 ela fica melhor posicionada
    #bloco[0] = coordenada X do centro do bloco, bloco[1]= coordenada Y do centro do bloco
    torre.set_position(bloco[0]-larguraTorre, bloco[1]-alturaTorre)
    return torre

def torreAtira(listaTorre, bloco, listaAlvo):
    #Criei um quadrado com as coordenadas, que corresponde a área de ataque da torre
    #listaTorre = [sprite, alcanceX, alcanceY, taxaDeDisparo, dano]
    #listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado]
    #Alcance em X
    areaX1 = bloco[0] - listaTorre[1]
    areaX2 = bloco[0] + listaTorre[1]
    #Alcance em Y
    areaY1 = (bloco[1] - listaTorre[2])-listaAlvo[1]
    areaY2 = bloco[1] + listaTorre[2]
    if listaAlvo[0].x in range(areaX1, areaX2) and listaAlvo[0].y in range(areaY1, areaY2):
        print("DENTRO DA AREA DA TORRE")
    #    listaAlvo[2] = listaAlvo[2] - listaTorre[4]
    return
#Principal
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
    #Soldado1
#inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY)
soldado1, alturaSol1 = inimigo("imagens\soldado1\soldado1lado1.png", 9, 0, 9, 1000, 0, 140)
vidaSol1 = 100
#listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado]
listaSoldado1 = [soldado1, alturaSol1, vidaSol1]
vetorSoldado1 =["imagens\soldado1\soldado1lado1.png", "imagens\soldado1\soldado1lado2.png", "imagens\soldado1\soldado1frente.png", "imagens\soldado1\soldado1costas.png"]
vetorVerificadoresSol1 = [0, 0, 0, 0]
velocidadeSol1 = 1
#Musica
musicaAtual = Sound("musicas\kingarthur.ogg")
musicaAtual.set_volume(10)
musicaAtual.play()
#Waves (APENAS PARA TESTE)
wave1 = 3000
wave2 = 4000
#Torres
    #Centros dos Blocos de Inserção(aproximado)
bloco1 = [322, 212]
bloco2 = [181, 388]
bloco3 = [444, 378]
spriteTorre1 = "imagens\Torres\TorrePedra.png" #Tive que definir o sprite antes
torre1 = torre(spriteTorre1, bloco1)
#listaTorre = [objeto, alcanceX, alcanceY, taxaDeDisparo, dano]
listaTorre1 = [torre1, 100, 100, "??", 10] #VALORES DESTINADOS À TESTE

#GameLoop
while True:

    janela.set_background_color((0, 0, 0))
    background.draw()
    #Inimigos

    #Soldado1
    listaSoldado1[0].move_x(0)
    listaSoldado1[0].move_y(0)
    listaSoldado1[0].update()
    listaSoldado1[0].draw()
        #Movimentacao do Soldado 1
    posXSol1 = listaSoldado1[0].x
    posYSol1 = listaSoldado1[0].y
    velXSol1, velYSol1 = movimentacao(posXSol1, posYSol1, listaSoldado1[0], velocidadeSol1)
        #Troca de animações do Soldado 1
    listaSoldado1[0] = mudancaDeAnimacao(listaSoldado1[0], velXSol1, velYSol1, vetorSoldado1, vetorVerificadoresSol1)
    #torre(posXSol1, posYSol1)
    #Torres
    listaTorre1[0].draw()
    torreAtira(listaTorre1, bloco1, listaSoldado1)
    #Musica
    #musicaAtual.play() Temporariamente coloquei o .play() fora do loop
    #PROBLEMA!! Música sendo reproduzida mais de uma vez ao mesmo tempo
    #Mouse
        #Muda o cursor OBS: https://www.pygame.org/docs/ref/cursors.html
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    janela.update()