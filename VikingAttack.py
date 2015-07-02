__author__ = 'João Pedro Sá Medeiros' , 'Ian Lanza'
"""Versão Atual do Jogo"""
versao = "v1.2.9.0" #Esta variável é utilizada no menu para exibir a versão
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
    #Game_State
    Game_State = 0
    #Teclado
    teclado = janela.get_keyboard()
    #Define as imagens das flechas que serão utilizadas nos subprogramas das torres
    vetorFlecha = ["imagens\Projeteis\Flechas\Flecha1.png", "imagens\Projeteis\Flechas\Flecha2.png", "imagens\Projeteis\Flechas\Flecha3.png", "imagens\Projeteis\Flechas\Flecha4.png", 200]
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
        global Game_State
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
            Game_State = 4
        return velX, velY, Game_State

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
        Game_State = 2
        background = GameImage("imagens\menus\pausa.png")
        background.draw()
        janela.draw_text(str(versao), 0, 584, 15, (255, 255, 255), "Arial", True)

        if teclado.key_pressed("enter"):
            Game_State = 1
        if teclado.key_pressed("space"):
            Game_State = 3
            musicaAtual.stop()
        if teclado.key_pressed("i"):
            Game_State = 6
        ver2 = 0
        janela.update()
        return Game_State, ver2
    def derrota():

        Game_State = 4
        background = GameImage("imagens\menus\perdeu.png")
        background.draw()
        janela.draw_text(str(versao), 0, 584, 15, (255, 255, 255), "Arial", True)
        if teclado.key_pressed("escape"):
            janela.close()
            musicaAtual.stop()
        if teclado.key_pressed("enter"):
            Game_State = 3
            musicaAtual.stop() #Sem isso a música começa a tocar novamente encima da outra
        janela.update()
        return Game_State
    def verificaDeltaTime():
        global janela
        return janela.delta_time()

    #def dinheiro():
    #    coins = 0
    def instrucoes(ver1):
        Game_State = 5
        if ver1 != 1:
            background = GameImage("imagens\menus\instrucoes.png")
        if ver1 == 1:
            background = GameImage("imagens\menus\creditos.png")
        if teclado.key_pressed("escape"):
            Game_State = 0
        if teclado.key_pressed("c"):
            ver1 = 1
        background.draw()
        janela.update()
        return Game_State, ver1
    def instrucoes2(ver2):
        Game_State = 6
        if ver2 != 1:
            background = GameImage("imagens\menus\instrucoes.png")
        if ver2 == 1:
            background = GameImage("imagens\menus\creditos.png")
        if teclado.key_pressed("escape"):
            Game_State = 2
        if teclado.key_pressed("c"):
            ver2 = 1
        background.draw()
        janela.update()
        return Game_State, ver2

    def menu(img1, img2):
        Game_State = 0
        background = GameImage("imagens\menus\iniciar.png")
        background.draw()
        img1.move_x(2)
        #image.SetAlpha(0)
        img1.draw()
        img1.update()
        img2.move_x(2)
        #image.SetAlpha(0)
        img2.draw()
        img2.update()
        if int(img2.x) == 1000: #Sem o int não funciona pois o valor em ponto flutuante não é um valor exato
            #img1.set_position(-1000, 0)
            img2.set_position(-1000, 0)
        if int(img1.x) == 1000: #Sem o int não funciona pois o valor em ponto flutuante não é um valor exato
            img1.set_position(-1000, 0)
        janela.draw_text(str(versao), 0, 584, 15, (255, 255, 255), "Arial", True)
        if teclado.key_pressed("enter"):
            Game_State = 1
        if teclado.key_pressed("i"):
            Game_State = 5
        ver1 = 0
        janela.update()
        return Game_State, img1, img2, ver1

    def vitoria():
        Game_State = 10
        background = GameImage("imagens\menus\Venceu.png")
        background.draw()
        if teclado.key_pressed("enter"):
            Game_State = 3
            musicaAtual.stop()
        if teclado.key_pressed("escape"):
            janela.close()
            musicaAtual.stop()
        janela.update()
        return Game_State

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
            if vetorInimigo[2] > 0 and vetorInimigo[3] != 0: #Proteção, verifica se a vida é maior do que 0 e se não é
                #o soldado fake!
                flecha.draw()
                flecha.update()
        if flecha.collided(vetorInimigo[0]):# or vetorInimigo[2] < 1: #OBS: A vida é retirada apenas quando ocorre a colisão, portanto às vezes a colisão falha e a vida não subtraída.
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
            #Movimentacao do Inimigo
            posXSol1 = listaInimigo[0].x
            posYSol1 = listaInimigo[0].y
            velXSol1, velYSol1, Game_State = movimentacao(posXSol1, posYSol1, listaInimigo[0], listaInimigo[3], FatorDelta)
            #Mudança de Animação do Inimigo
            listaInimigo[0] = mudancaDeAnimacao(listaInimigo[0], velXSol1, velYSol1, vetorSpritesInimigo, vetorVerificadoresInimigo)
        return listaInimigo

    def torreFinal(conf, ultimoTiro, listaTorre, listaAlvo, bloco, verificaDisparo, listaProjetil, projetil, verificador, timeDelta): #Representa a criação final da torre, a função que será chamada no game loop
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
        valorEmMoedas = 25
        #listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado, velocidadeSoldado]
        listaSol0 = [soldadoSprite0, alturaSol0, vidaSol0, velocidadeSol0, valorEmMoedas]
        vetorSol0 =["imagens\soldado0\soldado0lado1.png", "imagens\soldado0\soldado0lado2.png", "imagens\soldado0\soldado0frente.png", "imagens\soldado0\soldado0costas.png"]
        vetVerificadoresSol0 = [0, 0, 0, 0]
        return listaSol0, vetorSol0, vetVerificadoresSol0
    def soldado1():
        #Utilidade: Definir previamente o soldado tipo 1
        #inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY)
        soldadoSprite1, alturaSol1 = inimigo("imagens\soldado1\soldado1lado1.png", 9, 0, 9, 1000, 0, 140)
        vidaSol1 = 100
        velocidadeSol1 = 70
        valorEmMoedas = 100
        #listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado, velocidadeSoldado]
        listaSol1 = [soldadoSprite1, alturaSol1, vidaSol1, velocidadeSol1, valorEmMoedas]
        vetorSol1 =["imagens\soldado1\soldado1lado1.png", "imagens\soldado1\soldado1lado2.png", "imagens\soldado1\soldado1frente.png", "imagens\soldado1\soldado1costas.png"]
        vetVerificadoresSol1 = [0, 0, 0, 0]
        return listaSol1, vetorSol1, vetVerificadoresSol1

    def soldadoFake():
        #Utilidade: Definir um soldado que está fora da área de alcance de qualquer torre, para que seja apenas um valor temporário para o alvo da torre
        #inimigo(endereco, animacao, animacaoInicial, animacaoFinal, duracao, posX, posY)
        soldadoSpriteFake, alturaSolFake = inimigo("imagens\soldado1\soldado1lado1.png", 9, 0, 9, 1000, 0, -140)
        vidaSolFake = 3000
        velocidadeSolFake = 0
        valorEmMoedas = 0
        #listaSoldado = [soldado(sprite), alturaSoldado, vidaSoldado, velocidadeSoldado]
        listaSolFake = [soldadoSpriteFake, alturaSolFake, vidaSolFake, velocidadeSolFake, valorEmMoedas]
        vetorSolFake =["imagens\soldado1\soldado1lado1.png", "imagens\soldado1\soldado1lado2.png", "imagens\soldado1\soldado1frente.png", "imagens\soldado1\soldado1costas.png"]
        vetVerificadoresSolFake = [0, 0, 0, 0]
        return listaSolFake

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
        #wave0 = [5, 0] #3 soldados0, 1 soldado1 ...
        #wave1 = [3, 1]
        #wave2 = [5, 2]
        wave0 = [1, 0] #3 soldados0, 1 soldado1 ...
        wave1 = [0, 1]
        wave2 = [1, 0]
        todasWaves = [wave0, wave1, wave2]
        return todasWaves

    def chamaWave(listaTIni, verificaFim, ultimoSpawn, conta, contWave, ultimaWave):
        #Utilidade: Chamar a função criaSoldado dependendo da Wave
        #nWave = numero da wave Atual
        #listaTIni é uma lista em que estão armazenados todos os inimigos spawnados
        #verificaFim é um verificador que checa se o ultimo inimigo foi spawnado, 0 = não foi spawnado | 1 = foi spawnado
        wavesTodas = waves()
        soma1 = 0
        soma2 = 0
        tempoDeEspaco = randint(1000, 4000)
        espacoEntreWaves = 1000
        waveDesejada = wavesTodas[contWave]
        if janela.curr_time > ultimaWave + espacoEntreWaves:
            for i in range(len(waveDesejada)):
                soma2 = soma2 + waveDesejada[i] #Pega o numero de soldados que devem ser spawnados
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
            soma1 = soma1 + conta[i2] #Pega o numero de soldados que foram spawnados até agora
        if soma1 == soma2  and janela.curr_time > ultimaWave + espacoEntreWaves:
            if contWave < len(wavesTodas):
                contWave = contWave +1
                ultimaWave = janela.curr_time
                conta = [0]*len(conta)
                ultimoSpawn = 0
        if contWave == len(wavesTodas):
            verificaFim = 1
        #Lógica: se a soma da quantidade de soldados que ainda faltam pra spawnar for = 0, acabou a wave
        return verificaFim, ultimoSpawn, contWave, conta, ultimaWave

    def selecionaAlvo(lisTodosInimigos, bloco, listaTorre):
        areaX1 = bloco[0] - listaTorre[1]
        areaX2 = bloco[0] + listaTorre[1]
        areaY2 = bloco[1] + listaTorre[2]
        listaAlvos = []
        for soldado in range(len(lisTodosInimigos)):
            areaY1 = (bloco[1] - listaTorre[2])-lisTodosInimigos[soldado][0][0].height
            if int(lisTodosInimigos[soldado][0][0].x) in range(areaX1, areaX2) and int(lisTodosInimigos[soldado][0][0].y) in range(areaY1, areaY2):
                listaAlvos.append(lisTodosInimigos[soldado][0])
                break
        if listaAlvos == []:
            listaSoldadoFake = soldadoFake()
            return listaSoldadoFake
        else:
            return listaAlvos[0]

    def destroiInimigos(lsTodosIni, quantidadeMoedas):
        for inimigo in range(len(lsTodosIni)):
            if lsTodosIni[inimigo][0][2] < 1:
                quantidadeMoedas = quantidadeMoedas +  lsTodosIni[inimigo][0][4] #Soma a quantidade de moedas que é o valor do inimigo
                lsTodosIni.remove(lsTodosIni[inimigo]) #Remove o inimigo morto da lista de inimigos
                break
        return lsTodosIni, quantidadeMoedas

    def telaDeUpgrade(Game_State, qtdMoedasAtual, Tower_StateAtual):
        #Utilidade: Esta tela irá pausar o jogo e irá disponibilizar as opções de torres para fazer upgrade dependendo do
        #Tower_State, que Tower_State = 0(significa que o bloco de inserção está vazio), Tower_State = 1(significa que o bloco
        #está com a torre tipo 1 em sua posição... Durante esta tela o usuário decide o que fazer, sua decisão deve ser passada
        #retornando o dinheiro atual, visto que o usuário pode ter consumido parte do dinheiro anterior e também o Tower_State
        #para que seja sabido qual torre que deve aparecer.
        #DICA: os números 0, 1, 2... do Tower_State podem também ser utilizados para referenciar diferentes torres dentro de um
        #vetor ainda não criado de torres
        #Quando uma torre está disponível para venda ela deve-se dar o draw da imagem dela na telaDeUpgrade, se ela não está
        #disponível deve-se dar o draw da imagem em preto e branco dela, para sinalizar que aquela torre não está disponível.
        #Tower_State = 0 Significa que está vazio --> "imagens\menus\Cadeados\Cadeados0.png"
        #Tower_State = 1 Significa que está com a Torre 1 --> "imagens\menus\Cadeados\Cadeados1.png"
        #assim por diante
        background = GameImage("imagens\menus\Torres.png")
        background.draw()
        moeda.draw()
        janela.draw_text("Moedas: "+str(qtdMoedas), 100, 0, 15, (255, 255, 255), "Arial", True)
        if Tower_StateAtual == 0:
            if qtdMoedasAtual < 100: #Neste caso não tem dinheiro para comprar nenhuma torre e não tem nenhuma torre
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados0.png")
                cadeados.draw()
            else: #Neste caso tem-se dinheiro suficiente para comprar a próxima torre
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados1.png")
                cadeados.draw()
                if teclado.key_pressed("1"):
                    Tower_StateAtual = 1
                    qtdMoedasAtual = qtdMoedasAtual - 100
                #Fazer a torre spawnar e descontar o dinheiro se a torre for comprada
        elif Tower_StateAtual == 1:
            if qtdMoedasAtual < 150:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados1.png")
                cadeados.draw()
            else:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados2.png")
                cadeados.draw()
                if teclado.key_pressed("2"):
                    Tower_StateAtual = 2
                    qtdMoedasAtual = qtdMoedasAtual - 150
                #Fazer a torre spawnar e descontar o dinheiro se a torre for comprada

        elif Tower_StateAtual == 2:
            if qtdMoedasAtual < 250:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados2.png")
                cadeados.draw()
            else:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados3.png")
                cadeados.draw()
                if teclado.key_pressed("3"):
                    Tower_StateAtual = 3
                    qtdMoedasAtual = qtdMoedasAtual - 250
                #Fazer a torre spawnar e descontar o dinheiro se a torre for comprada
        elif Tower_StateAtual == 3:
            if qtdMoedasAtual < 300:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados3.png")
                cadeados.draw()
            else:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados4.png")
                cadeados.draw()
                if teclado.key_pressed("4"):
                    Tower_StateAtual = 4
                    qtdMoedasAtual = qtdMoedasAtual - 300
                #Fazer a torre spawnar e descontar o dinheiro se a torre for comprada
        elif Tower_StateAtual == 4:
            if qtdMoedasAtual < 350:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados4.png")
                cadeados.draw()
            else:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados5.png")
                cadeados.draw()
                if teclado.key_pressed("5"):
                    Tower_StateAtual = 5
                    qtdMoedasAtual = qtdMoedasAtual - 350
                #Fazer a torre spawnar e descontar o dinheiro se a torre for comprada
        elif Tower_StateAtual == 5:
            if qtdMoedasAtual < 400:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados5.png")
                cadeados.draw()
            elif qtdMoedasAtual >= 400 and qtdMoedasAtual < 500:
                cadeados = GameImage("imagens\menus\Cadeados\Cadeados6.png")
                cadeados.draw()
                if teclado.key_pressed("6"):
                    Tower_StateAtual = 6
                    qtdMoedasAtual = qtdMoedasAtual - 400
                #Fazer a torre spawnar e descontar o dinheiro se a torre for comprada
            elif qtdMoedasAtual > 500:
                if teclado.key_pressed("6"):
                    Tower_StateAtual = 6
                    qtdMoedasAtual = qtdMoedasAtual - 400
                if teclado.key_pressed("7"):
                    Tower_StateAtual = 7
                    qtdMoedasAtual = qtdMoedasAtual - 500
                #Fazer a torre spawnar e descontar o dinheiro se a torre for comprada
                #Tem todos os pre requizitos para a ultima torre.
                #Não precisa desenhar cadeado nenhum, apenas verificar se vai comprar ou não
        if teclado.key_pressed("space"): #Volta para o jogo
            Game_State = 1

        janela.update()
        return Game_State, qtdMoedasAtual, Tower_StateAtual

    #Os valores das Torres são destinados a teste!
    def Torre1(bloco):
        torreAtual = torre("imagens\Torres\TorreMadeira.png", bloco)
        #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
        listaTorre = [torreAtual, 100, 100, 10, 3000]
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        return listaTorre, flecha, verifica
    def Torre2(bloco):
        torreAtual = torre("imagens\Torres\TorreAntiga.png", bloco)
        #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
        listaTorre = [torreAtual, 150, 150, 15, 2500]
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        return listaTorre, flecha, verifica
    def Torre3(bloco):
        torreAtual = torre("imagens\Torres\TorrePedra.png", bloco)
        #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
        listaTorre = [torreAtual, 150, 150, 25, 2500]
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        return listaTorre, flecha, verifica
    def Torre4(bloco):
        torreAtual = torre("imagens\Torres\TorrePedra2.png", bloco)
        #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
        listaTorre = [torreAtual, 200, 200, 35, 2000]
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        return listaTorre, flecha, verifica
    def Torre5(bloco):
        torreAtual = torre("imagens\Torres\TorrePedra3.png", bloco)
        #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
        listaTorre = [torreAtual, 200, 200, 50, 2500]
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        return listaTorre, flecha, verifica
    def Torre6(bloco):
        torreAtual = torre("imagens\Torres\CampoDeArqueiros.png", bloco)
        #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
        listaTorre = [torreAtual, 300, 300, 70, 1500]
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        return listaTorre, flecha, verifica
    def Torre7(bloco):
        torreAtual = torre("imagens\Torres\TorreFinal.png", bloco)
        #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
        listaTorre = [torreAtual, 200, 200, 200, 4500]
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        return listaTorre, flecha, verifica

    def selecionaTipoDeTorre(Tower_StateAt, bloco):
        listaTorre = []
        flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
        if Tower_StateAt == 1:
            listaTorre, flecha, verifica = Torre1(bloco)
        if Tower_StateAt == 2:
            listaTorre, flecha, verifica = Torre2(bloco)
        if Tower_StateAt == 3:
            listaTorre, flecha, verifica = Torre3(bloco)
        if Tower_StateAt == 4:
            listaTorre, flecha, verifica = Torre4(bloco)
        if Tower_StateAt == 5:
            listaTorre, flecha, verifica = Torre5(bloco)
        if Tower_StateAt == 6:
            listaTorre, flecha, verifica = Torre6(bloco)
        if Tower_StateAt == 7:
            listaTorre, flecha, verifica = Torre7(bloco)
        return listaTorre, flecha, verifica

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
    #spriteTorre1 = "imagens\Torres\TorrePedra.png" #Tive que definir o sprite antes
    #spriteTorre2 = "imagens\Torres\TorrePedra.png"
    #spriteTorre3 = "imagens\Torres\TorrePedra.png"
    #torre1 = torre(spriteTorre1, bloco1)
    #torre2 = torre(spriteTorre2, bloco2)
    #torre3 = torre(spriteTorre3, bloco3)
    #Define Flecha

    flecha, verifica = criaFlecha(vetorFlecha[0], 0, 0)
    flechaT1, flechaT2, flechaT3 = flecha, flecha, flecha
    verificaT1, verificaT2, verificaT3 = verifica, verifica, verifica
    #listaTorre = [objeto, alcanceX, alcanceY, dano, taxaDeDisparo]
    #listaTorre1 = [torre1, 150, 150, 10, 2000] #VALORES DESTINADOS À TESTE
    #listaTorre2 = [torre2, 150, 150, 10, 2000]
    #listaTorre3 = [torre3, 150, 150, 10, 2000]
    listaTorre1 = []
    listaTorre2 = []
    listaTorre3 = []
    confirmador = 0
    confirmador1 = 0
    confirmador2 = 0
    contador = 0
    verificaTiroT1, verificaTiroT2, verificaTiroT3 = 1, 1, 1
    ultimoTiroT1 = 0
    ultimoTiroT2 = 0
    ultimoTiroT3 = 0
    contaWave = 0
    verificaFinal = 0
    waveAtual = 1
    ultSpawn = 0
    ultWave = 0
    contaSpawn = [0, 0]
    tempoJanelaAtual = 0
    moeda = GameImage("imagens\moeda.png")
    moeda.set_position(75, 0)
    Tower_StateT1 = 0
    Tower_StateT2 = 0
    Tower_StateT3 = 0
    qtdMoedas = 2000
    ver1 = 0
    ver2 = 0
    #Nuvem
    nuvem1 = Sprite("imagens\cloud.png", 1)
    nuvem1.set_position(-1000, 0)
    nuvem1.set_sequence(0, 1)
    nuvem1.set_total_duration(0)
    nuvem2 = Sprite("imagens\cloud.png", 1)
    nuvem2.set_position(0, 0)
    nuvem2.set_sequence(0, 1)
    nuvem2.set_total_duration(0)
    #Mouse
        #Muda o cursor OBS: https://www.pygame.org/docs/ref/cursors.html
        #OBS: pygame.mouse.get_pressed()[0]: #se clicado o botão 0, retorna True
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    clock = pygame.time.Clock()
    #GameLoop
    while Game_State != 3:
        if Game_State == 0:
            Game_State, nuvem1, nuvem2, ver1 = menu(nuvem1, nuvem2)
        if Game_State == 1:
            #Chama a pausa
            if teclado.key_pressed("escape"):
                Game_State = 2
            #Verifica se o mouse foi clicado e se o mouse está sobre algum dos blocos de inserção, então chama a tela de Upgrade
            #de Torres
            if pygame.mouse.get_pressed()[0]:
                if verificaPosMouse(bloco1[0]-60, bloco1[0]+60, bloco1[1]-60, bloco1[1]+60):
                    Game_State = 7
                if verificaPosMouse(bloco2[0]-60, bloco2[0]+60, bloco2[1]-60, bloco2[1]+60):
                    Game_State = 8
                if verificaPosMouse(bloco3[0]-60, bloco3[0]+60, bloco3[1]-60, bloco3[1]+60):
                    Game_State = 9

            if waveAtual == len(waves()) and listaTodosInimigos == []:
                Game_State = 10
             #Contador de frames
            contador = contador + 1
            """
            if contador < 5:
                deltaTime = verificaDeltaTime()
                # Esta parte é necessária pois como dependemos do delta_time() para controlar a velocidade do personagem
                #por isso ao iniciar o jogo armazenamos o valor do deltaTime da máquina em que o código está sendo executado para que
                #quando pausarmos o jogo usaremos esse valor.
            """
            deltaTime = verificaDeltaTime()
            janela.set_background_color((0, 0, 0))
            background.draw()
            #Inimigos
            #inimigoFinal(deltaTime, listaSoldado0, vetorSoldado0, vetorVerificadoresSol0)
            if verificaFinal != 1:
                verificaFinal, ultSpawn, contaWave, contaSpawn, ultWave= chamaWave(listaTodosInimigos, verificaFinal, ultSpawn, contaSpawn, contaWave, ultWave)
            atualizaInimigos(listaTodosInimigos)
            waveAtual = contaWave +1
            if contaWave+1 > len(waves()):
                waveAtual = contaWave

            janela.draw_text("Waves: "+str(waveAtual)+"/"+str(len(waves())), 0, 0, 15, (255, 255, 255), "Arial", True)
            moeda.draw()
            janela.draw_text("Moedas: "+str(qtdMoedas), 100, 0, 15, (255, 255, 255), "Arial", True)
            clock.tick()
            janela.draw_text("FPS: " +str(int(clock.get_fps())), 700, 0, 15, (255, 255, 255), "Arial", True)
            #inimigoFinal(deltaTime, listaTodosInimigos[0][0], listaTodosInimigos[0][1], listaTodosInimigos[0][2])
            #Soldado1
            #inimigoFinal(deltaTime, listaSoldado0, vetorSoldado0, vetorVerificadoresSol0)
            #Torres
                #Torre1
            if listaTorre1 != []:
                AlvoT1 = selecionaAlvo(listaTodosInimigos, bloco1, listaTorre1)
                confirmador, ultimoTiroT1, flechaT1, verificaT1, verificaTiroT1 = torreFinal(confirmador, ultimoTiroT1, listaTorre1, AlvoT1, bloco1, verificaTiroT1, vetorFlecha, flechaT1, verificaT1, deltaTime)
                #Torre2
            if listaTorre2 != []:
                AlvoT2 = selecionaAlvo(listaTodosInimigos, bloco2, listaTorre2)
                confirmador1, ultimoTiroT2, flechaT2, verificaT2, verificaTiroT2 = torreFinal(confirmador1, ultimoTiroT2, listaTorre2, AlvoT2, bloco2, verificaTiroT2, vetorFlecha, flechaT2, verificaT2, deltaTime)
                #Torre3
            if listaTorre3 != []:
                AlvoT3 = selecionaAlvo(listaTodosInimigos, bloco3, listaTorre3)
                confirmador2, ultimoTiroT3, flechaT3, verificaT3, verificaTiroT3 = torreFinal(confirmador2, ultimoTiroT3, listaTorre3, AlvoT3, bloco3, verificaTiroT3, vetorFlecha, flechaT3, verificaT3, deltaTime)

            listaTodosInimigos, qtdMoedas = destroiInimigos(listaTodosInimigos, qtdMoedas) #Esta função retira os inimigos da lista que contém todos eles

            #Musica
            #musicaAtual.play() Temporariamente coloquei o .play() fora do loop
            #PROBLEMA!! Música sendo reproduzida mais de uma vez ao mesmo tempo

            janela.update()
        if Game_State == 2:
            Game_State, ver2 = pausa()
        if Game_State == 4:
            Game_State = derrota()
        if Game_State == 5:
            Game_State, ver1 = instrucoes(ver1)
        if Game_State == 6:
            Game_State, ver2 = instrucoes2(ver2)
        if Game_State == 7:
            Game_State, qtdMoedas, Tower_StateT1 = telaDeUpgrade(Game_State, qtdMoedas, Tower_StateT1)
            listaTorre1, flechaT1, verificaT1 = selecionaTipoDeTorre(Tower_StateT1, bloco1)
        if Game_State == 8:
            Game_State, qtdMoedas, Tower_StateT2 = telaDeUpgrade(Game_State, qtdMoedas, Tower_StateT2)
            listaTorre2, flechaT2, verificaT2 = selecionaTipoDeTorre(Tower_StateT2, bloco2)
        if Game_State == 9:
            Game_State, qtdMoedas, Tower_StateT3 = telaDeUpgrade(Game_State, qtdMoedas, Tower_StateT3)
            listaTorre3, flechaT3, verificaT3 = selecionaTipoDeTorre(Tower_StateT3, bloco3)
        if Game_State == 10:
            Game_State = vitoria()