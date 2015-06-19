__author__ = 'João Pedro Sá Medeiros' , 'Ian Lanza'
"""Versão Atual do Jogo"""
versao = "v1.2.6.5" #Esta variável é utilizada no menu para exibir a versão
#OBS: sempre que a versão for atualizada, mudar no subprograma menu a versão exibida!
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import  randint
from PPlay.collision import *
from PPlay.animation import *
from PPlay.sound import  *
from PPlay.mouse import *
from pygame import *
while True:
    background = GameImage("imagens\cenarios\cenario1.3.5.png")
    background.set_position(0, 0)
    larguraFundo = background.width
    alturaFundo = background.height
    #Janela
    larguraJanela = 800
    alturaJanela = 600
    janela = Window(larguraFundo, alturaFundo)
    janela.set_title("Viking Attack")
    janela.set_background_color((255, 255, 255))
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
        resp = 0
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
        if int(posX) in range(635, 460, -1) and int(posY) in range(250, 260):
            objeto.move_x(-delta)
            objeto.move_y(0)
            velX = -velocidadeObjeto
            velY = 0
        if int(posX) in range(450, 465) and int(posY) in range(261, 90, -1):
            objeto.move_x(0)
            objeto.move_y(-delta)
            velX = 0
            velY = -velocidadeObjeto
        if int(posX) in range(450, 661) and int(posY) in range(80, 105):
            objeto.move_x(delta)
            objeto.move_y(0)
            velX = velocidadeObjeto
            velY = 0
        if int(posX) in range(661, 670) and int(posY) in range(90, 105):
            Game_Estate = 4
        return velX, velY, Game_Estate

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
                #listaAlvo[2] = listaAlvo[2] - listaTorre[3]
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
        background = GameImage("imagens\menus\pausa.png")
        background.draw()
        janela.draw_text(str(versao), 0, 584, 15, (255, 255, 255), "Arial", True)

        if teclado.key_pressed("enter"):
            Game_Estate = 1
        if teclado.key_pressed("space"):
            Game_Estate = 3
            musicaAtual.stop()
        janela.update()
        return Game_Estate
    def derrota():

        Game_Estate = 4
        background = GameImage("imagens\menus\perdeu.png")
        background.draw()
        janela.draw_text(str(versao), 0, 584, 15, (255, 255, 255), "Arial", True)
        if teclado.key_pressed("escape"):
            janela.close()
        if teclado.key_pressed("enter"):
            Game_Estate = 3
            musicaAtual.stop() #Sem isso a música começa a tocar novamente encima da outra
        janela.update()
        return Game_Estate
    def verificaDeltaTime():
        global janela
        return janela.delta_time()
    #def dinheiro():
    #    coins = 0

    def menu():
        Game_Estate = 0
        background = GameImage("imagens\menus\iniciar.png")
        background.draw()
        janela.draw_text(str(versao), 0, 584, 15, (255, 255, 255), "Arial", True)
        if teclado.key_pressed("enter"):
            Game_Estate = 1
        janela.update()
        return Game_Estate

    def criaFlecha(imagem, posX, posY):
        flecha = Sprite(imagem, 1)
        flecha.set_position(posX, posY)
        flecha.set_sequence(0, 1)
        flecha.set_total_duration(0)
        verifica = 0 #apenas para simplificar a primeira chamada
        return flecha, verifica

    def movimentaEAtualizaProjetil(flecha, verifica, vetorProjetil, vetorInimigo, verificaTiro, listaTorre, deltaT): #Movimenta e muda a imagem do projetil
        if (verifica == 0):# and contador in range(100, 200): #MOVIMENTO PRIMITIVO DA FLECHA
            x = (flecha.x - vetorInimigo[0].x)
            y = (flecha.y - vetorInimigo[0].y)
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
            if velx > 0 and vely > 0: #Regula a imagem da flecha, os comentários(tentam) representam o sentido da flecha
                flecha, verifica = criaFlecha(vetorProjetil[0], flecha.x, flecha.y) # \>
            if velx < 0 and vely > 0:
                flecha, verifica = criaFlecha(vetorProjetil[1], flecha.x, flecha.y) # </
            if velx < 0 and vely < 0:
                flecha, verifica = criaFlecha(vetorProjetil[2], flecha.x, flecha.y) # <\
            if velx > 0 and vely < 0:
                flecha, verifica = criaFlecha(vetorProjetil[3], flecha.x, flecha.y) # />
            velx = velx * deltaT
            vely = vely * deltaT
            flecha.move_x(velx)
            flecha.move_y(vely)
            flecha.draw()
            flecha.update()
        if flecha.collided(vetorInimigo[0]): #OBS: A vida é retirada apenas quando ocorre a colisão, portanto às vezes a colisão falha e a vida não subtraída.
            vetorInimigo[2] = vetorInimigo[2] - listaTorre[3]
            verifica = 1
            verificaTiro = 0
        return flecha, verifica, verificaTiro
    def inimigoFinal(FatorDelta, listaInimigo, vetorSpritesInimigo, vetorVerificadoresInimigo): #Representa a criação final do inimigo, a função que será chamada no game loop
        if listaInimigo[2] > 0:
            listaInimigo[0].move_x(0)
            listaInimigo[0].move_y(0)
            listaInimigo[0].update()
            listaInimigo[0].draw()
            janela.draw_text(str(listaInimigo[2]), listaInimigo[0].x, listaInimigo[0].y, 12, (255, 0 , 0), "Arial", False)
            print(listaInimigo[0].x, listaInimigo[0].y)
            #Movimentacao do Inimigo
            posXSol1 = listaInimigo[0].x
            posYSol1 = listaInimigo[0].y
            velXSol1, velYSol1, Game_Estate = movimentacao(posXSol1, posYSol1, listaInimigo[0], listaInimigo[3], FatorDelta)
            #Mudança de Animação do Inimigo
            listaInimigo[0] = mudancaDeAnimacao(listaInimigo[0], velXSol1, velYSol1, vetorSpritesInimigo, vetorVerificadoresInimigo)
        return listaInimigo

    def torreFinal(conf, ultimoTiro, listaTorre, listaAlvo, bloco, verificaDisparo, listaProjetil, projetil, verificador, timeDelta): #Representa a criação final da torre, a função que será chamada no game loop
        if verificaPosMouse(bloco[0]-60, bloco[0]+60, bloco[1]-60, bloco[1]+60) and conf== 0: #Precisa-se do confirmador para que só ative 1 vez a torre
            if pygame.mouse.get_pressed()[0]:
                conf = 1
        if conf == 1:
            listaTorre[0].draw()
            if (janela.curr_time > ultimoTiro + listaTorre[4]) and listaAlvo[2] > 0:
                ultimoTiro = janela.curr_time
                verificaDisparo, verificador = torreAtira(listaTorre, bloco, listaAlvo, verificaDisparo, verificador)
                projetil, verificador = criaFlecha(listaProjetil[0], bloco[0], bloco[1])
        if verificador == 0 and verificaDisparo == 0:
            projetil, verificador, verificaDisparo = movimentaEAtualizaProjetil(projetil, verificador, listaProjetil, listaAlvo, verificaDisparo, listaTorre, timeDelta)
        projetil.update()
        return conf, ultimoTiro, projetil, verificador, verificaDisparo

    def soldado0():
        #Utilidade: Definir previamente o soldado tipo 0
        #inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY)
        soldadoSprite0, alturaSol0 = inimigo("imagens\soldado0\soldado0lado1.png", 9, 0, 9, 1000, 0, 140)
        vidaSol0 = 100
        velocidadeSol0 = 50
        #listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado, velocidadeSoldado]
        listaSol0 = [soldadoSprite0, alturaSol0, vidaSol0, velocidadeSol0]
        vetorSol0 =["imagens\soldado0\soldado0lado1.png", "imagens\soldado0\soldado0lado2.png", "imagens\soldado0\soldado0frente.png", "imagens\soldado0\soldado0costas.png"]
        vetVerificadoresSol0 = [0, 0, 0, 0]
        return listaSol0, vetorSol0, vetVerificadoresSol0
    def soldado1():
        #Utilidade: Definir previamente o soldado tipo 1
        #inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY)
        soldadoSprite1, alturaSol1 = inimigo("imagens\soldado1\soldado1lado1.png", 9, 0, 9, 1000, 0, 140)
        vidaSol1 = 300
        velocidadeSol1 = 70
        #listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado, velocidadeSoldado]
        listaSol1 = [soldadoSprite1, alturaSol1, vidaSol1, velocidadeSol1]
        vetorSol1 =["imagens\soldado1\soldado1lado1.png", "imagens\soldado1\soldado1lado2.png", "imagens\soldado1\soldado1frente.png", "imagens\soldado1\soldado1costas.png"]
        vetVerificadoresSol1 = [0, 0, 0, 0]
        return listaSol1, vetorSol1, vetVerificadoresSol1

    def criaSoldado(soldadoX, listaTodosIni):
        #Armazenar em uma lista todos os inimigos da fase(OBS: esses inimigos serão removidos conforme forem sendo eliminados)
        listaSoldadosY, vetorSoldadoY, vetorVerificadoresSolY = soldadoX
        vetorSoldadoAtual = [listaSoldadosY, vetorSoldadoY, vetorVerificadoresSolY]
        listaTodosIni.append(vetorSoldadoAtual)
        #Como essa função é chamada apenas após os frames iniciais, pode-se utilizar o deltaTime, mas é recomendado criar uma
        #restrição para o chamador das waves para chamar apenas após o contador 5
        return listaTodosIni

    def atualizaInimigos(vetorTodosOsInimigos):
        #Atualiza todos os inimigos presentes no vetorTodosOsInimigos, que é o vetor que contém todos os inimigos da fase
        for w in range(len(vetorTodosOsInimigos)):
            listaSoldadoW = vetorTodosOsInimigos[w][0]
            vetorSoldadoW = vetorTodosOsInimigos[w][1]
            vetorVerificaSolW = vetorTodosOsInimigos[w][2]
            inimigoFinal(deltaTime, listaSoldadoW, vetorSoldadoW, vetorVerificaSolW)
        return

    def waves():
        #Utilizade: definir previamente o conteúdo de todas as waves
        #waveX = [soldado0, soldado1, ...]
        wave0 = [2, 2] #3 soldados0, 1 soldado1 ...
        wave1 = [5, 2]
        wave2 = [10, 4]
        todasWaves = [wave0, wave1, wave2]
        return todasWaves

    def chamaWave(nWave, listaTIni, verificaFim, ultimoSpawn, conta):
        #Utilidade: Chamar a função criaSoldado dependendo da Wave
        #nWave = numero da wave
        #listaTIni é uma lista em que estão armazenados todos os inimigos spawnados
        #verificaFim é um verificador que checa se o ultimo inimigo foi spawnado, 0 = não foi spawnado | 1 = foi spawnado
        wavesTodas = waves()
        waveDesejada = wavesTodas[nWave]
        soma1 = 0
        soma2 = 0
        tempoDeEspaco = randint(800, 4000)
        for i in range(len(waveDesejada)):
            soma2 = soma2 + waveDesejada[i]
            for j in range(waveDesejada[i]):
                if i == 0 and janela.curr_time > ultimoSpawn + tempoDeEspaco and conta[0] != waveDesejada[0]:
                    ultimoSpawn = janela.curr_time
                    conta[0] = conta[0] + 1
                    criaSoldado(soldado0(), listaTIni)
                if i == 1 and janela.curr_time > ultimoSpawn + tempoDeEspaco and conta[1] != waveDesejada[1]:
                    ultimoSpawn = janela.curr_time
                    conta[1] = conta[1] + 1
                    criaSoldado(soldado1(), listaTIni)
        for i2 in range(len(conta)):
            soma1 = soma1 + conta[i2]
        if soma1 == soma2:
            verificaFim = 1
        #Lógica: se a soma da quantidade de soldados que ainda faltam pra spawnar for = 0, acabou a wave
        return verificaFim, ultimoSpawn

    #Define o ícone obs:(Não funciona completamente)
    icone = pygame.image.load("imagens\icone.jpg").convert_alpha()
    pygame.display.set_icon(icone)
    #Inimigos
    listaTodosInimigos = [] #é uma lista em que estão armazenados todos os inimigos spawnados
        #Soldado1
    #inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY)
    listaSoldado0, vetorSoldado0, vetorVerificadoresSol0 = soldado0()
    listaSoldado1, vetorSoldado1, vetorVerificadoresSol1 = soldado1()
    #Musica
    musicaAtual = Sound("musicas\kingarthur.ogg")
    musicaAtual.set_volume(10)
    musicaAtual.play()
    #Waves
    #Torres
        #Centros dos Blocos de Inserção(aproximado)
    bloco1 = [322, 212]
    bloco2 = [181, 388]
    bloco3 = [444, 378]
    spriteTorre1 = "imagens\Torres\TorrePedra.png" #Tive que definir o sprite antes
    spriteTorre2 = "imagens\Torres\TorrePedra.png"
    spriteTorre3 = "imagens\Torres\TorrePedra.png"
    torre1 = torre(spriteTorre1, bloco1)
    torre2 = torre(spriteTorre2, bloco2)
    torre3 = torre(spriteTorre3, bloco3)
    #Define Flecha
    vetorFlecha = ["imagens\Projeteis\Flechas\Flecha1.png", "imagens\Projeteis\Flechas\Flecha2.png", "imagens\Projeteis\Flechas\Flecha3.png", "imagens\Projeteis\Flechas\Flecha4.png", 100]
    flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
    flechaT1, flechaT2, flechaT3 = flecha, flecha, flecha
    verificaT1, verificaT2, verificaT3 = verifica, verifica, verifica
    #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
    listaTorre1 = [torre1, 150, 150, 10, 2000] #VALORES DESTINADOS À TESTE
    listaTorre2 = [torre2, 150, 150, 10, 2000]
    listaTorre3 = [torre3, 150, 150, 10, 2000]
    confirmador = 0
    confirmador1 = 0
    confirmador2 = 0
    contador = 0
    verificaTiroT1, verificaTiroT2, verificaTiroT3 = 1, 1, 1
    ultimoTiroT1 = 0
    ultimoTiroT2 = 0
    ultimoTiroT3 = 0
    verificaFinal = 0
    ultSpawn = 0
    contaSpawn = [0, 0]
    #Mouse
        #Muda o cursor OBS: https://www.pygame.org/docs/ref/cursors.html
        #OBS: pygame.mouse.get_pressed()[0]: #se clicado o botão 0, retorna True
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    #GameLoop
    while Game_Estate != 3:
        if Game_Estate == 0:
            Game_Estate = menu()
        if Game_Estate == 1:
            if teclado.key_pressed("escape"):
                Game_Estate = 2
             #Contador de frames
            contador = contador + 1
            if contador < 5: # Esta parte é necessária pois como dependemos do delta_time() para controlar a velocidade do personagem
                #por isso ao iniciar o jogo armazenamos o valor do deltaTime da máquina em que o código está sendo executado para que
                #quando pausarmos o jogo usaremos esse valor.
                deltaTime = verificaDeltaTime()
            janela.set_background_color((0, 0, 0))
            background.draw()
            #Inimigos
            #inimigoFinal(deltaTime, listaSoldado0, vetorSoldado0, vetorVerificadoresSol0)
            if verificaFinal != 1:
                verificaFinal, ultSpawn = chamaWave(0, listaTodosInimigos, verificaFinal, ultSpawn, contaSpawn)
            atualizaInimigos(listaTodosInimigos)
            #inimigoFinal(deltaTime, listaTodosInimigos[0][0], listaTodosInimigos[0][1], listaTodosInimigos[0][2])
            #Soldado1
            #inimigoFinal(deltaTime, listaSoldado0, vetorSoldado0, vetorVerificadoresSol0)
            #Torres
                #Torre1
            confirmador, ultimoTiroT1, flechaT1, verificaT1, verificaTiroT1 = torreFinal(confirmador, ultimoTiroT1, listaTorre1, listaSoldado0, bloco1, verificaTiroT1, vetorFlecha, flechaT1, verificaT1, deltaTime)
                #Torre2
            confirmador1, ultimoTiroT2, flechaT2, verificaT2, verificaTiroT2 = torreFinal(confirmador1, ultimoTiroT2, listaTorre2, listaSoldado0, bloco2, verificaTiroT2, vetorFlecha, flechaT2, verificaT2, deltaTime)
                #Torre3
            confirmador2, ultimoTiroT3, flechaT3, verificaT3, verificaTiroT3 = torreFinal(confirmador2, ultimoTiroT3, listaTorre3, listaSoldado0, bloco3, verificaTiroT3, vetorFlecha, flechaT3, verificaT3, deltaTime)
            #Musica
            #musicaAtual.play() Temporariamente coloquei o .play() fora do loop
            #PROBLEMA!! Música sendo reproduzida mais de uma vez ao mesmo tempo
            janela.update()
        if Game_Estate == 2:
            Game_Estate = pausa()
        if Game_Estate == 4:
            Game_Estate = derrota()
