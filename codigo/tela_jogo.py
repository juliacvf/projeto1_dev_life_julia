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

    largura_visivel = largura_tela - 1
    altura_visivel = altura_tela - 1


    camera_x = estado['pos_jogador'][0] - largura_visivel//2
    camera_y = estado['pos_jogador'][1] - altura_visivel//2

    camera_x = max(0, min(camera_x, largura_mapa - largura_visivel))
    camera_y = max(0, min(camera_y, altura_mapa - altura_visivel))

    for y in range (altura_visivel): 
        for x in range(largura_visivel):
            x_mapa = (camera_x + x)
            y_mapa = (camera_y + y)
            posicao = [x_mapa, y_mapa]

            motor.desenha_string(janela, x, y, ' ', VERDE_FLORESTA, VERDE_FLORESTA)

            if posicao == estado['pos_jogador']:
                motor.desenha_string(janela, x, y, JOGADOR, VERDE_FLORESTA, AMARELO_DOURADO)

            for objeto in estado['objetos']:
                if posicao == objeto['posicao']:
                    motor.desenha_string(janela, x, y, objeto['tipo'], VERDE_FLORESTA, objeto['cor'])

            for parede in estado['paredes']:
                if posicao == parede:
                    motor.desenha_string(janela, x, y, PAREDE, MARROM_MAIS_ESCURO, MARROM_ESCURO)

            for monstro in estado['monstros']:
                if posicao == monstro['posicao']:
                    if monstro['tipo'] == MONSTRO1:
                        motor.desenha_string(janela, x, y, monstro['tipo'], VERDE_FLORESTA, COR_MONSTRO1)
                    elif monstro['tipo'] == MONSTRO2:
                        motor.desenha_string(janela, x, y, monstro['tipo'], VERDE_FLORESTA, COR_MONSTRO2)
                    elif monstro['tipo'] == MONSTRO3:
                        motor.desenha_string(janela, x, y, monstro['tipo'], VERDE_FLORESTA, COR_MONSTRO3)

            for iten in estado['itens']:
                if posicao == iten['posicao']:
                    if iten['tipo'] == POCAO:
                        motor.desenha_string(janela, x, y, iten['tipo'], VERDE_FLORESTA, iten['cor'])
                    elif iten['tipo'] == ELIXIR:
                        motor.desenha_string(janela, x, y, iten['tipo'], VERDE_FLORESTA, iten['cor'])
                    elif iten['tipo'] == ESPADA:
                        motor.desenha_string(janela, x, y, iten['tipo'], VERDE_FLORESTA, iten['cor'])
                    elif iten['tipo'] == MARTELO:
                        motor.desenha_string(janela, x, y, iten['tipo'], VERDE_FLORESTA, iten['cor'])
                    elif iten['tipo'] == CHAVE:
                        motor.desenha_string(janela, x, y, iten['tipo'], VERDE_FLORESTA, iten['cor'])

    for x in range(estado['max_vidas']):
        if x < estado['vidas']:
            cor = VERMELHO
        else:
            cor = BRANCO
        motor.desenha_string(janela, x, 0, CORACAO, VERDE_FLORESTA, cor)

    nivel = estado['nivel'] 
    experiencia = estado['experiencia']
    motor.desenha_string(janela, 0, 1, f'Nível {nivel}: {experiencia}', VERDE_FLORESTA, BRANCO)

    mensagem = estado['mensagem']
    motor.desenha_string(janela, 0, altura_tela - 1, mensagem, AZUL_ESCURO, BRANCO)

    motor.desenha_string(janela, 10, 1, str(estado['inventario']['†']), PRETO, BRANCO)

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

    altura_mapa = len(mapa)
    largura_mapa = len(mapa[0])
    
    monstros = estado['monstros']
    objetos = estado['objetos']
    itens = estado['itens']


    posicoes_ocupadas = []
    posicoes_ocupadas.append(estado['pos_jogador'])
    posicoes_ocupadas.extend(estado['paredes'])

    for objeto in objetos:
        posicoes_ocupadas.append(objeto['posicao'])

    posicao_monstros = []
    for monstro in monstros:
        posicao_monstros.append(monstro['posicao'])
        posicoes_ocupadas.append(monstro['posicao'])


    posicao_itens = []
    for iten in itens:
        posicao_itens.append(iten['posicao'])
        posicoes_ocupadas.append(iten['posicao'])
    

    x = estado['pos_jogador'][0]
    y = estado['pos_jogador'][1]
    posicao_inicial_jogador = [x, y]

    def batalha(monstro):
        numero = random.random()
        if numero < 0.30 and monstro['tipo'] == MONSTRO1:
            estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
            estado['vidas'] -= 1
            if estado['vidas'] == 0:
                estado['tela_atual'] = TELA_GAME_OVER

        elif numero < 0.45 and monstro['tipo'] == MONSTRO2:
            estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
            estado['vidas'] -= 1
            if estado['vidas'] == 0:
                estado['tela_atual'] = TELA_GAME_OVER

        elif numero < 0.70 and monstro['tipo'] == MONSTRO3:
            estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
            estado['vidas'] -= 1
            if estado['vidas'] == 0:
                estado['tela_atual'] = TELA_GAME_OVER

        else:
            monstro['vida'] -= 1
            if monstro['vida'] == 0:
                monstros.remove(monstro)
                posicao_monstros.remove(monstro['posicao'])
                posicoes_ocupadas.remove(monstro['posicao'])
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
                    for novo in novo_monstro:
                        if monstro_sorteado == MONSTRO1:
                            novo['vida'] = 5
                            novo['probabilidade de ataque'] = 0.30
                        elif monstro_sorteado == MONSTRO2:
                            novo['vida'] = 3
                            novo['probabilidade de ataque'] = 0.45
                            novo['eixo'] = None
                        elif monstro_sorteado == MONSTRO3:
                            novo['vida'] = 2
                            novo['probabilidade de ataque'] = 0.70
                            novo['situação'] = None
                        monstros.append(novo)

                objetos.extend(gera_objetos(3, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas))
                itens.extend(gera_objetos(2, POCAO, COR_POCAO, largura_mapa, altura_mapa, posicoes_ocupadas))
                itens.extend(gera_objetos(1, ELIXIR, COR_ELIXIR, largura_mapa, altura_mapa, posicoes_ocupadas))
                itens.extend(gera_objetos(1, ESPADA, COR_ESPADA, largura_mapa, altura_mapa, posicoes_ocupadas))
                itens.extend(gera_objetos(1, MARTELO, COR_ESPADA, largura_mapa, altura_mapa, posicoes_ocupadas))
                

                estado['experiencia'] -= 10

    def coleta_iten(iten):
        soma_itens = sum(estado['inventario'].values())
        if soma_itens < 6:
            tipo_iten = iten['tipo']
            if tipo_iten == CHAVE and estado['inventario'][tipo_iten] + 1 == 3:
                    estado['inventario'][tipo_iten] += 1
                    estado['mensagem'] = 'Você desbloqueou a sala secreta'
                    itens.remove(iten) 
                    posicao_itens.remove(iten['posicao'])
                    posicoes_ocupadas.remove(iten['posicao'])
    
            else:
                estado['inventario'][tipo_iten] += 1
                estado['mensagem'] = 'Iten adicionado ao inventário'
                itens.remove(iten) 
                posicao_itens.remove(iten['posicao'])
                posicoes_ocupadas.remove(iten['posicao'])

        else:
            estado['mensagem'] = 'Seu inventário está cheio'


    if tecla == motor.SETA_ESQUERDA:
        if [x-1, y] not in estado['paredes'] and [x-1, y] not in posicao_monstros and x-1 >= 0:
            x -= 1
            if [x, y] in posicao_itens:
                for iten in itens:
                    if [x, y] == iten['posicao']:
                        coleta_iten(iten)
                        break

        elif [x-1, y] in posicao_monstros:
            for monstro in monstros:
                if [x-1, y] == monstro['posicao']:
                    batalha(monstro)
                    break

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_DIREITA:
        if [x+1, y] not in estado['paredes'] and [x+1, y] not in posicao_monstros and x+1 < len(mapa[0]):
            x += 1
            if [x, y] in posicao_itens:
                for iten in itens:
                    if [x, y] == iten['posicao']:
                        coleta_iten(iten)
                        break

        elif [x+1, y] in posicao_monstros:
            for monstro in monstros:
                if [x+1, y] == monstro['posicao']:
                    batalha(monstro)
                    break

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_CIMA:
        if [x, y-1] not in estado['paredes'] and [x, y-1] not in posicao_monstros and y-1 >= 0:
            y -= 1
            if [x, y] in posicao_itens:
                for iten in itens:
                    if [x, y] == iten['posicao']:
                        coleta_iten(iten)
                        break

        elif [x, y-1] in posicao_monstros:
            for monstro in monstros:
                if [x, y-1] == monstro['posicao']:
                    batalha(monstro)
                    break

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_BAIXO:
        if [x, y+1] not in estado['paredes'] and [x, y+1] not in posicao_monstros and y+1 < len(mapa):
            y += 1
            if [x, y] in posicao_itens:
                for iten in itens:
                    if [x, y] == iten['posicao']:
                       coleta_iten(iten)
                       break

        elif [x, y+1] in posicao_monstros:
            for monstro in monstros:
                if [x, y+1] == monstro['posicao']:
                   batalha(monstro)
                   break

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

    elif tecla == 'p':
        if estado['inventario']['⚗'] >= 1:
            estado['inventario']['⚗'] -= 1
            numero = random.random()
            if numero <= 0.4:
                estado['vidas'] -= 1
                estado['max_vidas'] -= 1
            else:
                estado['max_vidas'] += 1
                estado['vidas'] += 1

        else:
            estado['mensagem'] = 'Você não tem poções'

    elif tecla == 'e':
        if estado['inventario']['✦'] >= 1:
            estado['inventario']['✦'] -= 1
            estado['experiencia'] += 2

        else:
            estado['mensagem'] = 'Você não tem elixir'

    elif tecla == 's':
        if estado['inventario']['†'] >= -1:
                estado['inventario']['†'] -= 1
                for monstro in estado['monstros']:
                    if monstro['tipo'] == MONSTRO1:
                        monstro['probabilidade de ataque'] = 0.25
                    if monstro['tipo'] == MONSTRO2:
                        monstro['probabilidade de ataque'] = 0.40
                    if monstro['tipo'] == MONSTRO3:
                        monstro['probabilidade de ataque'] = 0.55

        else:
            estado['mensagem'] = 'Você não têm espadas'


    elif tecla == 'h':
        if estado['inventario']['⚒'] >= 1:
                estado['inventario']['⚒'] -= 1
                for monstro in estado['monstros']:
                    if monstro['tipo'] == MONSTRO1:
                        monstro['vida'] = 4
                    if monstro['tipo'] == MONSTRO2:
                        monstro['vida'] = 2
                    if monstro['tipo'] == MONSTRO3:
                        monstro['vida'] = 1

        else:
            estado['mensagem'] = 'Você não têm martelos'

    elif tecla == 'k':
        if estado['inventario']['⚿'] < 3:  
            estado['mensagem'] = 'Você ainda não pode acessar a sala secreta'
        else: 
            estado['inventario']['⚿'] -= 3
            estado['tela_atual'] = SALA_SECRETA
            