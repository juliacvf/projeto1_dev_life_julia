from constantes import *
import motor_grafico as motor
import random 


def desenha_tela(janela, estado, altura, largura):
    estado['largura_sala'] = largura
    estado['altura_sala'] = altura
    estado['paredes_sala'] = []

    motor.preenche_fundo(janela, AZUL_ESCURO)

    for y in range(altura-1):
        estado['paredes_sala'].append([0, y])
        estado['paredes_sala'].append([1, y])
        estado['paredes_sala'].append([largura - 3, y])
        estado['paredes_sala'].append([largura - 2, y])

        motor.desenha_string(janela, 0, y, '▣', CINZA_PEDRA, CINZA)
        motor.desenha_string(janela, 1, y, '▣', CINZA_PEDRA, CINZA)
        motor.desenha_string(janela, largura - 3, y, '▣', CINZA_PEDRA, CINZA)
        motor.desenha_string(janela, largura - 2, y, '▣', CINZA_PEDRA, CINZA)

    for x in range(largura-1):
        estado['paredes_sala'].append([x, 0])
        estado['paredes_sala'].append([x, altura - 2])
        
        motor.desenha_string(janela, x, 0, '▣', CINZA_PEDRA, CINZA)
        motor.desenha_string(janela, x, altura - 2, '▣', CINZA_PEDRA, CINZA)

    for x in range(6, largura - 5, 3):
        motor.desenha_string(janela, x, 3, '*', AZUL_ESCURO, AMARELO_TOCHA)
        motor.desenha_string(janela, x, altura - 5, '*', AZUL_ESCURO, AMARELO_TOCHA)

    for y in range(5, altura - 4, 2):
        motor.desenha_string(janela, 4, y, '*', AZUL_ESCURO, AMARELO_TOCHA)
        motor.desenha_string(janela, largura - 6, y, '*', AZUL_ESCURO, AMARELO_TOCHA)

    for objeto in estado['objetos_sala']:
        motor.desenha_string(janela, objeto['posicao'][0], objeto['posicao'][1], objeto['tipo'], AZUL_ESCURO, objeto['cor'])

    motor.desenha_string(janela, estado['pos_jogador_sala'][0], estado['pos_jogador_sala'][1], JOGADOR, AZUL_ESCURO, AMARELO_DOURADO)

    for iten in estado['itens_sala']:
        motor.desenha_string(janela, iten['posicao'][0], iten['posicao'][1], iten['tipo'], AZUL_ESCURO, iten['cor'])

    mensagem = estado['mensagem']
    motor.desenha_string(janela, 0, altura - 1, mensagem, AZUL_ESCURO, BRANCO)

    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla):
    estado['mensagem'] = ''

    x = estado['pos_jogador_sala'][0]
    y = estado['pos_jogador_sala'][1]

    itens = estado['itens_sala']
    objetos = estado['objetos_sala']
    paredes = estado['paredes_sala']

    largura = estado['largura_sala']
    altura = estado['altura_sala']

    posicao_itens = []
    for iten in itens:
        posicao_itens.append(iten['posicao'])

    posicao_objetos = []
    for objeto in objetos:
        posicao_objetos.append(objeto['posicao'])

    def coleta_iten(iten):
        soma_itens = sum(estado['inventario'].values())

        if soma_itens < 8:
            tipo_iten = iten['tipo']

            estado['inventario'][tipo_iten] += 1
            estado['mensagem'] = 'Item adicionado ao inventário'

            posicao_itens.remove(iten['posicao'])
            itens.remove(iten)
        else:
            estado['mensagem'] = 'Seu inventário está cheio'

    def coleta_objeto(objeto):
        if objeto['tipo'] == CORACAO:
            if estado['max_vidas'] < 8:
                estado['max_vidas'] += 1
                estado['vidas'] += 1

                posicao_objetos.remove(objeto['posicao'])
                objetos.remove(objeto)

                estado['mensagem'] = 'Quantidade de vidas aumentada'
            else:
                estado['mensagem'] = 'Você já possui o máximo de 8 vidas'

    if tecla == motor.SETA_ESQUERDA:
        nova_posicao = [x - 1, y]

        if nova_posicao not in paredes and x - 1 >= 0:
            x -= 1
        else:
            estado['mensagem'] = 'Você não pode se mover nessa direção'

    elif tecla == motor.SETA_DIREITA:
        nova_posicao = [x + 1, y]

        if nova_posicao not in paredes and x + 1 < largura - 1:
            x += 1
        else:
            estado['mensagem'] = 'Você não pode se mover nessa direção'
            

    elif tecla == motor.SETA_CIMA:
        nova_posicao = [x, y - 1]

        if nova_posicao not in paredes and y - 1 >= 0:
            y -= 1
        else:
            estado['mensagem'] = 'Você não pode se mover nessa direção'
            

    elif tecla == motor.SETA_BAIXO:
        nova_posicao = [x, y + 1]

        if nova_posicao not in paredes and y + 1 < altura - 1:
            y += 1
        else:
            estado['mensagem'] = 'Você não pode se mover nessa direção'
        

    estado['pos_jogador_sala'] = [x, y]
    posicao_jogador = [x, y]

    if posicao_jogador in posicao_itens:
        for iten in itens:
            if iten['posicao'] == posicao_jogador:
                coleta_iten(iten)
                break

    if posicao_jogador in posicao_objetos:
        for objeto in objetos:
            if objeto['posicao'] == posicao_jogador:
                coleta_objeto(objeto)
                break

    if tecla == motor.ESPACO:
        estado['tela_atual'] = TELA_JOGO

    elif tecla == motor.ESCAPE or tecla == 'q':
        estado['tela_atual'] = SAIR