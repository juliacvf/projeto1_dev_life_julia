from constantes import *
import motor_grafico as motor
import random
from inicializacao import gera_objetos
from inicializacao import gera_posicao_desocupada

def desenha_tela(janela, estado, altura_tela, largura_tela):
    motor.preenche_fundo(janela, PRETO)
    mapa = estado['mapa']
    altura_mapa = len(mapa)
    largura_mapa = len(mapa[0])
    inicio_x = (largura_tela - largura_mapa) // 2
    inicio_y = (altura_tela - altura_mapa) // 2


    for y in range(altura_mapa):
        for x in range(largura_mapa):
            motor.desenha_string(janela, inicio_x + x, inicio_y + y, ' ', VERDE_ESCURO, VERDE_ESCURO)

    for y in range(altura_mapa):
        for x in range(largura_mapa):
            posicao = [x, y]

            if posicao == estado['pos_jogador']:
                motor.desenha_string(janela, inicio_x + x, inicio_y + y, JOGADOR, VERDE_ESCURO, AZUL)

            for objeto in estado['objetos']:
                if posicao == objeto['posicao']:
                    motor.desenha_string(janela, inicio_x + x, inicio_y + y, objeto['tipo'], VERDE_ESCURO, objeto['cor'])

            for parede in estado['paredes']:
                if posicao == parede:
                    motor.desenha_string(janela, inicio_x + x, inicio_y + y, PAREDE, MARROM_MAIS_ESCURO, MARROM_ESCURO)

            for monstro in estado['monstros']:
                if posicao == monstro['posicao']:
                    motor.desenha_string(janela, inicio_x + x, inicio_y + y, monstro['tipo'], VERDE_ESCURO, monstro['cor'])

    for x in range(estado['max_vidas']):
        if x < estado['vidas']:
            cor = VERMELHO
        else:
            cor = BRANCO
        motor.desenha_string(janela, x, 0, CORACAO, PRETO, cor)

    nivel = estado['nivel'] 
    experiencia = estado['experiencia']
    motor.desenha_string(janela, 0, 1, f'Nível {nivel}: {experiencia}', PRETO, AMARELO)

    mensagem = estado['mensagem']
    motor.desenha_string(janela, 0, altura_tela - 1, mensagem, PRETO, AMARELO)

    motor.mostra_janela(janela)



def movimento_dos_monstros(estado, tecla, posicao_inicial_jogador):
    movimentos = [motor.SETA_ESQUERDA, motor.SETA_DIREITA, motor.SETA_CIMA, motor.SETA_BAIXO]
    mapa = estado['mapa']
    monstros = estado['monstros']
    posicao_monstros = []
    for monstro in monstros:
        posicao_monstros.append(monstro['posicao'])

    posicao_objetos = []
    for objeto in estado['objetos']:
        posicao_objetos.append(objeto['posicao'])

    x = posicao_inicial_jogador[0]
    y = posicao_inicial_jogador[1]

    for monstro in monstros:
        xm = monstro['posicao'][0]
        ym = monstro['posicao'][1]

        if (tecla == motor.SETA_ESQUERDA and [x-1, y] != [xm, ym]) or (tecla == motor.SETA_DIREITA and [x+1, y] != [xm, ym]) or (tecla == motor.SETA_CIMA and [x, y-1] != [xm, ym]) or (tecla == motor.SETA_BAIXO and [x, y+1] != [xm, ym]):

            if monstro['tipo'] == MONSTRO1:
                movimento = random.choice(movimentos)

                if movimento == motor.SETA_ESQUERDA and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and xm-1 >= 0:
                    xm -= 1
                elif movimento == motor.SETA_DIREITA and [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and xm+1 < len(mapa[0]):
                    xm += 1
                elif movimento == motor.SETA_CIMA and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and ym-1 >= 0:
                    ym -= 1
                elif movimento == motor.SETA_BAIXO and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and ym+1 < len(mapa):
                    ym += 1


            elif monstro['tipo'] == MONSTRO2:
                distancia_horizontal = abs(xm - estado['pos_jogador'][0])
                distancia_vertical = abs(ym - estado['pos_jogador'][1])

                if monstro['eixo'] == None:
                    if distancia_horizontal > distancia_vertical:
                        if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and xm-1 >= 0:
                            xm -= 1
                            monstro['eixo'] = 'vertical'
                        elif estado['pos_jogador'][0] - xm > 0 and  [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and xm+1 < len(mapa[0]):
                            xm += 1
                            monstro['eixo'] = 'vertical'
                        else:
                            monstro['eixo'] = 'vertical'

                    else:
                        if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and ym-1 >= 0:
                            ym -= 1
                            monstro['eixo'] = 'horizontal'
                        elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and ym+1 < len(mapa):
                            ym += 1
                            monstro['eixo'] = 'horizontal'
                        else:
                            monstro['eixo'] = 'horizontal'

                elif monstro['eixo'] == 'vertical':
                    if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and ym-1 >= 0:
                        ym -= 1
                        monstro['eixo'] = 'horizontal'
                    elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and ym+1 < len(mapa):
                        ym += 1
                        monstro['eixo'] = 'horizontal'
                    else:
                        monstro['eixo'] = 'horizontal'

                elif monstro['eixo'] == 'horizontal':
                    if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and xm-1 >= 0:
                        xm -= 1
                        monstro['eixo'] = 'vertical'
                    elif estado['pos_jogador'][0] - xm > 0 and  [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and xm+1 < len(mapa[0]):
                        xm += 1
                        monstro['eixo'] = 'vertical'
                    else:
                        monstro['eixo'] = 'vertical'
                    

            elif monstro['tipo'] == MONSTRO3:
                distancia_horizontal = abs(xm - estado['pos_jogador'][0])
                distancia_vertical = abs(ym - estado['pos_jogador'][1])
                distancias = ['horizontal', 'vertical']
                situacao = ['esperar', 'avançar']

                if monstro['situação'] == None:
                    situação = random.choice(situacao)
                    monstro['situação'] = situação

                if monstro['situação'] == 'avançar':
                    if distancia_horizontal > distancia_vertical:
                        if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and [xm-2, ym] not in estado['paredes'] and [xm-2, ym] not in posicao_monstros and [xm-2, ym] not in posicao_objetos and [xm-2, ym] != estado['pos_jogador'] and xm-2 >= 0:
                            xm -= 2
                        elif estado['pos_jogador'][0] - xm > 0 and [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and [xm+2, ym] not in estado['paredes'] and [xm+2, ym] not in posicao_monstros and [xm+2, ym] not in posicao_objetos and [xm+2, ym] != estado['pos_jogador'] and xm+2 < len(mapa[0]):
                            xm += 2
                    elif distancia_vertical > distancia_horizontal:
                        if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and [xm, ym-2] not in estado['paredes'] and [xm, ym-2] not in posicao_monstros and [xm, ym-2] not in posicao_objetos and [xm, ym-2] != estado['pos_jogador'] and ym-2 >= 0:
                            ym -= 2
                        elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and [xm, ym+2] not in estado['paredes'] and [xm, ym+2] not in posicao_monstros and [xm, ym+2] not in posicao_objetos and [xm, ym+2] != estado['pos_jogador'] and ym+2 < len(mapa):
                            ym += 2
                    else:
                        distancia = random.choice(distancias)
                        if distancia == 'horizontal':
                            if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and [xm-2, ym] not in estado['paredes'] and [xm-2, ym] not in posicao_monstros and [xm-2, ym] not in posicao_objetos and [xm-2, ym] != estado['pos_jogador'] and xm-2 >= 0:
                                xm -= 2
                            elif estado['pos_jogador'][0] - xm > 0 and [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and [xm+2, ym] not in estado['paredes'] and [xm+2, ym] not in posicao_monstros and [xm+2, ym] not in posicao_objetos and [xm+2, ym] != estado['pos_jogador'] and xm+2 < len(mapa[0]):
                                xm += 2
                        else:
                            if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and [xm, ym-2] not in estado['paredes'] and [xm, ym-2] not in posicao_monstros and [xm, ym-2] not in posicao_objetos and [xm, ym-2] != estado['pos_jogador'] and ym-2 >= 0:
                                ym -= 2
                            elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and [xm, ym+2] not in estado['paredes'] and [xm, ym+2] not in posicao_monstros and [xm, ym+2] not in posicao_objetos and [xm, ym+2] != estado['pos_jogador'] and ym+2 < len(mapa):
                                ym += 2
                    monstro['situação'] = 'esperar'

                elif monstro['situação'] == 'esperar':
                    monstro['situação'] = 'avançar'


        if [xm, ym] != monstro['posicao']:
            posicao_monstros.remove(monstro['posicao'])
            monstro['posicao'] = [xm, ym]
            posicao_monstros.append(monstro['posicao'])



def atualiza_estado(estado, tecla):
    estado['mensagem'] = ''
    movimentos = [motor.SETA_ESQUERDA, motor.SETA_DIREITA, motor.SETA_CIMA, motor.SETA_BAIXO]
    lista_monstros = [MONSTRO1, MONSTRO2, MONSTRO3]
    mapa = estado['mapa']
    monstros = estado['monstros']
    altura_mapa = len(mapa)
    largura_mapa = len(mapa[0])
    objetos = estado['objetos']

    posicoes_ocupadas = []
    posicoes_ocupadas.append(estado['pos_jogador'])
    posicoes_ocupadas.append(estado['paredes'])
    for objeto in objetos:
        posicoes_ocupadas.append(objeto['posicao'])

    posicao_monstros = []
    for monstro in monstros:
        posicao_monstros.append(monstro['posicao'])
        posicoes_ocupadas.append(monstro['posicao'])

    x = estado['pos_jogador'][0]
    y = estado['pos_jogador'][1]
    posicao_inicial_jogador = [x, y]

    if tecla == motor.SETA_ESQUERDA:
        if [x-1, y] not in estado['paredes'] and [x-1, y] not in posicao_monstros and x-1 >= 0:
            x -= 1

        elif [x-1, y] in posicao_monstros:
            for monstro in monstros:
                if [x-1, y] == monstro['posicao']:
                    numero = random.random()
                    if numero < 0.2 and monstro['tipo'] == MONSTRO1:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.4 and monstro['tipo'] == MONSTRO2:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.6 and monstro['tipo'] == MONSTRO3:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    else:
                        monstro['vida'] -= 1
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
                            estado['mensagem'] = "Você matou o monstro"

                            if monstro['tipo'] == MONSTRO1:
                                estado['experiencia'] += 2
                            elif monstro['tipo'] == MONSTRO2:
                                estado['experiencia'] += 3
                            elif monstro['tipo'] == MONSTRO3:
                                estado['experiencia'] += 5

                        else:
                            estado['mensagem'] = f"Você atacou o monstro e agora ele tem {monstro['vida']} vidas"

                        if estado['experiencia'] >= 10:
                            estado['nivel'] += 1

                            for i in range(4):
                                monstro_sorteado = random.choice(lista_monstros)
                                novo_monstro = []
                                novo_monstro += gera_objetos(1, monstro_sorteado, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
                                for monstro in novo_monstro:
                                    if monstro_sorteado == MONSTRO1:
                                        monstro['vida'] = 5
                                        monstro['probabilidade de ataque'] = 0.2
                                    if monstro_sorteado == MONSTRO2:
                                        monstro['vida'] = 3
                                        monstro['probabilidade de ataque'] = 0.4
                                        monstro['eixo'] = None
                                    elif monstro_sorteado == MONSTRO3:
                                        monstro['vida'] = 2
                                        monstro['probabilidade de ataque'] = 0.6
                                        monstro['situação'] = None
                                    monstros.append(monstro)

                            objetos += gera_objetos(3, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)

                            estado['experiencia'] -= 10

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_DIREITA:
        if [x+1, y] not in estado['paredes'] and [x+1, y] not in posicao_monstros and x+1 < len(mapa[0]):
                x += 1

        elif [x+1, y] in posicao_monstros:
            for monstro in monstros:
                if [x+1, y] == monstro['posicao']:
                    numero = random.random()
                    if numero < 0.2 and monstro['tipo'] == MONSTRO1:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.4 and monstro['tipo'] == MONSTRO2:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.6 and monstro['tipo'] == MONSTRO3:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    else:
                        monstro['vida'] -= 1
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
                            estado['mensagem'] = "Você matou o monstro"

                            if monstro['tipo'] == MONSTRO1:
                                estado['experiencia'] += 2
                            elif monstro['tipo'] == MONSTRO2:
                                estado['experiencia'] += 3
                            elif monstro['tipo'] == MONSTRO3:
                                estado['experiencia'] += 5

                        else:
                            estado['mensagem'] = f"Você atacou o monstro e agora ele tem {monstro['vida']} vidas"

                        if estado['experiencia'] >= 10:
                            estado['nivel'] += 1

                            for i in range(4):
                                monstro_sorteado = random.choice(lista_monstros)
                                novo_monstro = []
                                novo_monstro += gera_objetos(1, monstro_sorteado, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
                                for monstro in novo_monstro:
                                    if monstro_sorteado == MONSTRO1:
                                        monstro['vida'] = 5
                                        monstro['probabilidade de ataque'] = 0.2
                                    if monstro_sorteado == MONSTRO2:
                                        monstro['vida'] = 3
                                        monstro['probabilidade de ataque'] = 0.4
                                        monstro['eixo'] = None
                                    elif monstro_sorteado == MONSTRO3:
                                        monstro['vida'] = 2
                                        monstro['probabilidade de ataque'] = 0.6
                                        monstro['situação'] = None
                                    monstros.append(monstro)

                            objetos += gera_objetos(3, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)

                            estado['experiencia'] -= 10

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_CIMA:
        if [x, y-1] not in estado['paredes'] and [x, y-1] not in posicao_monstros and y-1 >= 0:
                y -= 1
        elif [x, y-1] in posicao_monstros:
            for monstro in monstros:
                if [x, y-1] == monstro['posicao']:
                    numero = random.random()
                    if numero < 0.2 and monstro['tipo'] == MONSTRO1:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.4 and monstro['tipo'] == MONSTRO2:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.6 and monstro['tipo'] == MONSTRO3:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    else:
                        monstro['vida'] -= 1
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
                            estado['mensagem'] = "Você matou o monstro"

                            if monstro['tipo'] == MONSTRO1:
                                estado['experiencia'] += 2
                            elif monstro['tipo'] == MONSTRO2:
                                estado['experiencia'] += 3
                            elif monstro['tipo'] == MONSTRO3:
                                estado['experiencia'] += 5

                        else:
                            estado['mensagem'] = f"Você atacou o monstro e agora ele tem {monstro['vida']} vidas"

                        if estado['experiencia'] >= 10:
                            estado['nivel'] += 1

                            for i in range(4):
                                monstro_sorteado = random.choice(lista_monstros)
                                novo_monstro = []
                                novo_monstro += gera_objetos(1, monstro_sorteado, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
                                for monstro in novo_monstro:
                                    if monstro_sorteado == MONSTRO1:
                                        monstro['vida'] = 5
                                        monstro['probabilidade de ataque'] = 0.2
                                    if monstro_sorteado == MONSTRO2:
                                        monstro['vida'] = 3
                                        monstro['probabilidade de ataque'] = 0.4
                                        monstro['eixo'] = None
                                    elif monstro_sorteado == MONSTRO3:
                                        monstro['vida'] = 2
                                        monstro['probabilidade de ataque'] = 0.6
                                        monstro['situação'] = None
                                    monstros.append(monstro)

                            objetos += gera_objetos(3, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)

                            estado['experiencia'] -= 10

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_BAIXO:
        if [x, y+1] not in estado['paredes'] and [x, y+1] not in posicao_monstros and y+1 < len(mapa):
                y += 1
        elif [x, y+1] in posicao_monstros:
            for monstro in monstros:
                if [x, y+1] == monstro['posicao']:
                    numero = random.random()
                    if numero < 0.2 and monstro['tipo'] == MONSTRO1:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.4 and monstro['tipo'] == MONSTRO2:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    elif numero < 0.6 and monstro['tipo'] == MONSTRO3:
                        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
                        estado['vidas'] -= 1
                        if estado['vidas'] == 0:
                            estado['tela_atual'] = TELA_GAME_OVER

                    else:
                        monstro['vida'] -= 1
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
                            estado['mensagem'] = "Você matou o monstro"

                            if monstro['tipo'] == MONSTRO1:
                                estado['experiencia'] += 2
                            elif monstro['tipo'] == MONSTRO2:
                                estado['experiencia'] += 3
                            elif monstro['tipo'] == MONSTRO3:
                                estado['experiencia'] += 5

                        else:
                            estado['mensagem'] = f"Você atacou o monstro e agora ele tem {monstro['vida']} vidas"

                        if estado['experiencia'] >= 10:
                            estado['nivel'] += 1

                            for i in range(4):
                                monstro_sorteado = random.choice(lista_monstros)
                                novo_monstro = []
                                novo_monstro += gera_objetos(1, monstro_sorteado, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
                                for monstro in novo_monstro:
                                    if monstro_sorteado == MONSTRO1:
                                        monstro['vida'] = 5
                                        monstro['probabilidade de ataque'] = 0.2
                                    if monstro_sorteado == MONSTRO2:
                                        monstro['vida'] = 3
                                        monstro['probabilidade de ataque'] = 0.4
                                        monstro['eixo'] = None
                                    elif monstro_sorteado == MONSTRO3:
                                        monstro['vida'] = 2
                                        monstro['probabilidade de ataque'] = 0.6
                                        monstro['situação'] = None
                                    monstros.append(monstro)

                            objetos += gera_objetos(3, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)

                            estado['experiencia'] -= 10


        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"


    if [x, y] != estado['pos_jogador']:
        estado['pos_jogador'] = [x, y]
        posicao = [x, y]

        for objeto in estado['objetos']:
            if posicao == objeto['posicao']:
                if objeto['tipo'] == ESPINHO:
                    if estado['vidas'] > 1:
                        estado['vidas'] -= 1             
                        estado['mensagem'] = "Você perdeu uma vida"
                    else:
                        estado['vidas'] -= 1
                        estado['tela_atual'] = TELA_GAME_OVER

                elif objeto['tipo'] == CORACAO:
                    if estado['vidas'] == estado['max_vidas']:
                         estado['mensagem'] = "Vida cheia"
                    else:
                        estado['vidas'] += 1
                        estado['mensagem'] = "Você ganhou uma vida"

                    estado['objetos'].remove(objeto) 

    movimento_dos_monstros(estado, tecla, posicao_inicial_jogador)
                
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO

    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR

