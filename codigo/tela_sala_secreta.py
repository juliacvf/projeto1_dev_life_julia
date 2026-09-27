from constantes import *
import motor_grafico as motor
from funcoes_auxiliares import coleta_iten_sala_secreta
from funcoes_auxiliares import coleta_objeto_sala_secreta


def desenha_tela(janela, estado, altura, largura):
    # pega constantes do inicializa estado p/ desenhar a sala secreta qnd o comando de abrir for dado, atualizando os valores p/ valores coerentes
    estado['largura_sala'] = largura
    estado['altura_sala'] = altura
    estado['paredes_sala'] = []

    motor.preenche_fundo(janela, AZUL_ESCURO)

    # desenho de paredes contornando as laterais da sala 
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


    # desenho de estrelinhas na sala (puramente decorativo)
    for x in range(6, largura - 5, 3):
        motor.desenha_string(janela, x, 3, '*', AZUL_ESCURO, AMARELO_TOCHA)
        motor.desenha_string(janela, x, altura - 5, '*', AZUL_ESCURO, AMARELO_TOCHA)

    for y in range(5, altura - 4, 2):
        motor.desenha_string(janela, 4, y, '*', AZUL_ESCURO, AMARELO_TOCHA)
        motor.desenha_string(janela, largura - 6, y, '*', AZUL_ESCURO, AMARELO_TOCHA)

    # desnho dos objetos, itens e do jogador nas posições ja pré-definidas na função de inicialização de estado
    for objeto in estado['objetos_sala']:
        motor.desenha_string(janela, objeto['posicao'][0], objeto['posicao'][1], objeto['tipo'], AZUL_ESCURO, objeto['cor'])

    motor.desenha_string(janela, estado['pos_jogador_sala'][0], estado['pos_jogador_sala'][1], JOGADOR, AZUL_ESCURO, AMARELO_DOURADO)

    for iten in estado['itens_sala']:
        motor.desenha_string(janela, iten['posicao'][0], iten['posicao'][1], iten['tipo'], AZUL_ESCURO, iten['cor'])

    mensagem = estado['mensagem']
    motor.desenha_string(janela, 0, altura - 1, mensagem, AZUL_ESCURO, BRANCO)

    for x in range(estado['max_vidas']):
        if x < estado['vidas']:
            cor = VERMELHO
        else:
            cor = BRANCO
        motor.desenha_string(janela, x, 0, CORACAO, AZUL_ESCURO, cor)


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

    # possui função de atualização de estado referente ao movimento do jogador no mapa, mas ainda mais simplificado uma vez que despreza a necessidade de variaveis para controlar porção do mapa dentro da janela
    if tecla == motor.SETA_ESQUERDA:
        nova_posicao = [x - 1, y]
        if nova_posicao not in paredes and x - 1 >= 0: # a ausencia de monstros e objetos que impedem movimentação permite apenas a verificação das paredes nas possibilidades de movimento do jogador
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
                coleta_iten_sala_secreta(estado, iten, itens, posicao_itens)
                break

    if posicao_jogador in posicao_objetos:
        for objeto in objetos:
            if objeto['posicao'] == posicao_jogador:
                coleta_objeto_sala_secreta(estado, objeto, objetos, posicao_objetos)
                break

    # definição de retorno à tela do jogo ou saída do jogo
    if tecla == motor.ESPACO:
        estado['tela_atual'] = TELA_JOGO

    elif tecla == motor.ESCAPE or tecla == 'q':
        estado['tela_atual'] = SAIR

    
    # não é possível o acesso ao inventário nem uso de itens do inventário dentro da sala secreta. o jogador deve sair dela para poder utulizá-los e verificar o que está carregando