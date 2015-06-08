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
#Game_Estate
Game_Estate = 0
#Teclado
teclado = janela.get_keyboard()
#Subprogramas

def inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY):
    #animacao = total de imagens da animacao
    #animacaoInicial = quadro inicial da animacao
    #animacaoFinal = quadro final da animacao
    #posX e posY = posições iniciais que o inimigo começa
    soldado = Sprite(endereco, animacao)
    larguraSol = soldado.width
    alturaSol = soldado.height
    soldado.set_sequence(animacaoInicial, animacaoFinal)
    soldado.set_total_duration(duracao)
    soldado.set_position(posX, posY-alturaSol)
    return soldado, alturaSol
def movimentacao(posX, posY, objeto, velocidadeObjeto, deltaTime):
    #Condições diferentes para cada cenário, tais coordenadas valem para o cenário 1.3.5
    #Troca de animação dependendo da direção do movimento(A fazer...)
    global Game_Estate
    velX = 0
    velY = 0
    delta = velocidadeObjeto * deltaTime# * janela.delta_time() #Criou-se o "delta" para que a velocidade seja igual em todas as máquinas
    velocidadeObjeto = delta
    if (int(posX) < 390) and (int(posY) in range(90, 150)):
        objeto.move_x(delta)
        objeto.move_y(0)
        velX = velocidadeObjeto
        velY = 0
    if int(posX) in range(390, 395) and int(posY) in range(90, 330):
        objeto.move_x(0)
        objeto.move_y(delta)
        velX = 0
        velY = velocidadeObjeto
    if int(posX) in range(423, 60, -1) and int(posY) in range(250, 265):
        objeto.move_x(-delta)
        objeto.move_y(0)
        velX = -velocidadeObjeto
        velY = 0
    if (int(posX) < 80) and int(posY) in range(250, 500):
        objeto.move_x(0)
        objeto.move_y(delta)
        velX = 0
        velY = velocidadeObjeto
    if (int(posX) in range(60, 630)) and (int(posY) in range(415, 500)):
        objeto.move_x(delta)
        objeto.move_y(0)
        velX = velocidadeObjeto
        velY = 0
    if (int(posX) in range(630, 635)) and int(posY) in range(475, 255, -1):
        objeto.move_x(0)
        objeto.move_y(-delta)
        velX = 0
        velY = -velocidadeObjeto
    if int(posX) in range(631, 460, -1) and int(posY) in range(250, 260):
        objeto.move_x(-delta)
        objeto.move_y(0)
        velX = -velocidadeObjeto
        velY = 0
    if int(posX) in range(460, 465) and int(posY) in range(261, 90, -1):
        objeto.move_x(0)
        objeto.move_y(-delta)
        velX = 0
        velY = -velocidadeObjeto
    if int(posX) in range(460, 661) and int(posY) in range(90, 105):
        objeto.move_x(delta)
        objeto.move_y(0)
        velX = velocidadeObjeto
        velY = 0
    if int(posX) in range(661, 670) and int(posY) in range(90, 105):
        Game_Estate = 1
        janela.draw_text("Aperte Esc Pra sair, ou Enter pra Reiniciar",0,0,30,(255,255,255),"Arial",True,True)
        if teclado.key_pressed("escape"):
            janela.close()
        '''if teclado.key_pressed("enter"):
            Game_Estate = menu()'''
        print("PERDEU")
        janela.update()
    return velX, velY

def mudancaDeAnimacao(objeto, velX, velY, vetorSprites, verificadorObj):
    posX = 0
    posY = 0
    altura = objeto.height
    if verificadorObj[0] == 0:
        if velX < 0:
            posX = int(objeto.x)
            posY = int(objeto.y)
            objeto, altura = inimigo(vetorSprites[1], 9, 0, 9, 1000, posX, posY + altura)
            verificadorObj[0] = 1
    if velY != 0:
        verificadorObj[0] = 0
    if verificadorObj[1] == 0:
        if velY > 0 :
            posX = int(objeto.x)
            posY = int(objeto.y)
            objeto, altura = inimigo(vetorSprites[2], 9, 0, 9, 1000, posX, posY + altura)
            verificadorObj[1] = 1
    if velX != 0:
        verificadorObj[1] = 0
    posX = int(objeto.x)
    posY = int(objeto.y)
    if (verificadorObj[2] == 0 and posY in range(400, 500)) or (verificadorObj[2] ==0 and int(posX) in range(460, 661) and int(posY) in range(90, 101)):
        if velX > 0:
            posX = int(objeto.x)
            posY = int(objeto.y)
            objeto, altura = inimigo(vetorSprites[0], 9, 0, 9, 1000, posX, posY + altura)
            verificadorObj[2] = 1
    if velY != 0:
        verificadorObj[2] = 0
    if verificadorObj[3] == 0:
        if velY < 0 :
            posX = int(objeto.x)
            posY = int(objeto.y)
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

def torreAtira(listaTorre, bloco, listaAlvo, verificaTiro, verificaColisao):
    #Criei um quadrado com as coordenadas, que corresponde a área de ataque da torre
    #listaTorre = [sprite, alcanceX, alcanceY, taxaDeDisparo, dano]
    #listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado]
    #Alcance em X
    areaX1 = bloco[0] - listaTorre[1]
    areaX2 = bloco[0] + listaTorre[1]
    #Alcance em Y
    areaY1 = (bloco[1] - listaTorre[2])-listaAlvo[1]
    areaY2 = bloco[1] + listaTorre[2]

    #Tem que converter para int, pois se não a comparação não funciona
    if int(listaAlvo[0].x) in range(areaX1, areaX2) and int(listaAlvo[0].y) in range(areaY1, areaY2):
        if listaAlvo[2] > 0:
            print("DENTRO DA AREA DA TORRE")
            listaAlvo[2] = listaAlvo[2] - listaTorre[4]
            verificaColisao = 0
            verificaTiro = 0
    else:
        verificaColisao = 1
        verificaTiro = 1

    return verificaTiro, verificaColisao

def verificaPosMouse(xInicial, xFinal, yInicial, yFinal):
    x, y = pygame.mouse.get_pos()
    if x in range(xInicial, xFinal) and y in range(yInicial, yFinal):
        return True
    return False

def pausa():
    Game_Estate = 2
    janela.draw_text("Aperte Enter pra sair da Pausa",200,200,45,(255,255,255),"Arial",True,True)

    if teclado.key_pressed("enter"):
        Game_Estate = 1
    janela.update()
    return Game_Estate
def verificaDeltaTime():
    global janela
    return janela.delta_time()
#def dinheiro():
#    coins = 0


def menu():
    Game_Estate = 0
    background = GameImage("imagens\cenarios\cenario1.3.5.png")
    background.draw()
    janela.draw_text("Aperte Enter pra começar",200,200,45,(255,255,255),"Arial",True,True)


    if teclado.key_pressed("enter"):
        Game_Estate = 1
    janela.update()
    return Game_Estate

#def restart():

def criaFlecha(imagem, posX, posY):
    flecha = Sprite(imagem, 1)
    flecha.set_position(posX, posY)
    flecha.set_sequence(0, 1)
    flecha.set_total_duration(0)
    verifica = 0 #apenas para simplificar a primeira chamada
    return flecha, verifica

def movimentaEAtualizaProjetil(flecha, verifica, vetorProjetil, vetorInimigo, verificaTiro): #Movimenta e muda a imagem do projetil
    if (verifica == 0):# and contador in range(100, 200): #MOVIMENTO PRIMITIVO DA FLECHA
        x = (flecha.x - listaSoldado1[0].x)
        y = (flecha.y - listaSoldado1[0].y)
        proporcao = x/y
        if proporcao < 0:
            proporcao = -proporcao
        if x > 0:
            velx = -vetorProjetil[4]
        else:
            velx = vetorProjetil[4]
        if y > 0:
            vely = -vetorProjetil[4]
        else:
            vely = vetorProjetil[4]

        vely = vely/proporcao
        flechaPOS = flecha
        if velx > 0 and vely > 0: #Regula a imagem da flecha, os comentários(tentam) representam o sentido da flecha
            flecha, verifica = criaFlecha(vetorProjetil[0], flecha.x, flecha.y) # \>
        if velx < 0 and vely > 0:
            flecha, verifica = criaFlecha(vetorProjetil[1], flecha.x, flecha.y) # </
        if velx < 0 and vely < 0:
            flecha, verifica = criaFlecha(vetorProjetil[2], flecha.x, flecha.y) # <\
        if velx > 0 and vely < 0:
            flecha, verifica = criaFlecha(vetorProjetil[3], flecha.x, flecha.y) # />

        flecha.move_x(velx)
        flecha.move_y(vely)
        print("VEL:", velx)
        print("VEL/prop", vely)
        flecha.draw()
        flecha.update()
    if flecha.collided(vetorInimigo[0]):
        verifica = 1
        verificaTiro = 0
    return flecha, verifica, verificaTiro



#Principal
#Fundo


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
velocidadeSol1 = 60
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
torre2 = torre(spriteTorre1, bloco2)
torre3 = torre(spriteTorre1, bloco3)
#listaTorre = [objeto, alcanceX, alcanceY, taxaDeDisparo, dano]
listaTorre1 = [torre1, 100, 100, "??", 10] #VALORES DESTINADOS À TESTE
listaTorre2 = [torre2, 100, 100, "??", 10]
listaTorre3 = [torre3, 100, 100, "??", 10]
confirmador = 0
confirmador1 = 0
confirmador2 = 0
contador = 0
#Define Flecha
vetorFlecha1 = ["imagens\Projeteis\Flechas\Flecha1.png", "imagens\Projeteis\Flechas\Flecha2.png", "imagens\Projeteis\Flechas\Flecha3.png", "imagens\Projeteis\Flechas\Flecha4.png", 0.5]
flecha, verifica = criaFlecha(vetorFlecha1[0], 0, 0)
verificaTiro = 1
#GameLoop
while True:
    if Game_Estate == 0:
        Game_Estate = menu()
    if Game_Estate == 1:
        if teclado.key_pressed("escape"):
            Game_Estate = 2
         #Contador de frames
        contador = contador + 1

        if contador < 5: # Esta parte é necessária pois como dependemos do delta_time() para controlar a velocidade do personagem
        #nos primeiros frames este valor está bugado portanto precisa-se esperar um pouco, posteriormente, com a tela de inicialização
        #o problema deve sumir.
            velocidadeSol1 = 1
            deltaTime = verificaDeltaTime()
        else:
            velocidadeSol1 = 800

        janela.set_background_color((0, 0, 0))
        background.draw()
        #Inimigos

        #Soldado1
        if listaSoldado1[2] > 0:


            listaSoldado1[0].move_x(0)
            listaSoldado1[0].move_y(0)
            listaSoldado1[0].update()
            listaSoldado1[0].draw()
            janela.draw_text(str(listaSoldado1[2]), listaSoldado1[0].x, listaSoldado1[0].y, 12, (255, 0 , 0), "Arial", False)
                #Movimentacao do Soldado 1
            posXSol1 = listaSoldado1[0].x
            posYSol1 = listaSoldado1[0].y
            velXSol1, velYSol1 = movimentacao(posXSol1, posYSol1, listaSoldado1[0], velocidadeSol1, deltaTime)
                #Troca de animações do Soldado 1
            listaSoldado1[0] = mudancaDeAnimacao(listaSoldado1[0], velXSol1, velYSol1, vetorSoldado1, vetorVerificadoresSol1)
        #torre(posXSol1, posYSol1)
        #Torres
        ############BLOCO 1############
        if verificaPosMouse(270, 370, 150, 260) and confirmador == 0: #Precisa-se do confirmador para que só ative 1 vez a torre
            if pygame.mouse.get_pressed()[0]:
                confirmador = 1
        if confirmador == 1:
            listaTorre1[0].draw()
            if contador%100 == 0:
                verificaTiro, verifica = torreAtira(listaTorre1, bloco1, listaSoldado1, verificaTiro, verifica)
                flecha, verifica = criaFlecha(vetorFlecha1[0], bloco1[0], bloco1[1])
            #Flecha
        if verifica == 0 and verificaTiro == 0:

            flecha, verifica, verificaTiro = movimentaEAtualizaProjetil(flecha, verifica, vetorFlecha1, listaSoldado1, verificaTiro)

        ############BLOCO 2############
        if verificaPosMouse(bloco2[0]-60, bloco2[0]+60, bloco2[1]-60, bloco2[1]+60) and confirmador1 == 0: #Precisa-se do confirmador para que só ative 1 vez a torre
            if pygame.mouse.get_pressed()[0]:
                confirmador1 = 1
        if confirmador1 == 1:
            listaTorre2[0].draw()
            if contador%100 == 0:
                verificaTiro, verifica = torreAtira(listaTorre2, bloco2, listaSoldado1, verificaTiro, verifica)
                flecha, verifica = criaFlecha(vetorFlecha1[0], bloco2[0], bloco2[1])
            #Flecha
        if verifica == 0 and verificaTiro == 0:

            flecha, verifica, verificaTiro = movimentaEAtualizaProjetil(flecha, verifica, vetorFlecha1, listaSoldado1, verificaTiro)
        ############BLOCO 3############
        if verificaPosMouse(bloco3[0]-60, bloco3[0]+60, bloco3[1]-60, bloco3[1]+60) and confirmador2 == 0: #Precisa-se do confirmador para que só ative 1 vez a torre
            if pygame.mouse.get_pressed()[0]:
                confirmador2 = 1
        if confirmador2 == 1:
            listaTorre3[0].draw()
            if contador%100 == 0:
                verificaTiro, verifica = torreAtira(listaTorre3, bloco3, listaSoldado1, verificaTiro, verifica)
                flecha, verifica = criaFlecha(vetorFlecha1[0], bloco3[0], bloco3[1])
        #Flecha
        if verifica == 0 and verificaTiro == 0:

            flecha, verifica, verificaTiro = movimentaEAtualizaProjetil(flecha, verifica, vetorFlecha1, listaSoldado1, verificaTiro)

            print("EXECUTANDO")
            flecha.update()
        #Musica
        #musicaAtual.play() Temporariamente coloquei o .play() fora do loop
        #PROBLEMA!! Música sendo reproduzida mais de uma vez ao mesmo tempo
        #Mouse
            #Muda o cursor OBS: https://www.pygame.org/docs/ref/cursors.html
            #OBS: pygame.mouse.get_pressed()[0]: #se clicado o botão 0, retorna True
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)
        janela.update()
    if Game_Estate == 2:
        Game_Estate = pausa()
