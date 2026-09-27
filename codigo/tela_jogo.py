from constantes import *
import motor_grafico as motor
from funcoes_auxiliares import movimento_dos_monstros
from funcoes_auxiliares import atualizacao_inventario
from funcoes_auxiliares import batalha
from funcoes_auxiliares import coleta_iten_mapa
from funcoes_auxiliares import passa_por_objetos
from funcoes_auxiliares import niveis 


def desenha_tela(janela, estado, altura_tela, largura_tela):
    motor.preenche_fundo(janela, PRETO)
    mapa = estado['mapa']
    altura_mapa = len(mapa)
    largura_mapa = len(mapa[0])

    # delimitação de limites p/ evitar problemas de "out of range"
    largura_visivel = largura_tela - 1
    altura_visivel = altura_tela - 1

    # definição das variáveis "camera" que permitem a centralização da posição do jogador no mapa de acordo com o pedaço do mapa que se encontra dentro da janela do jogo
    camera_x = estado['pos_jogador'][0] - largura_visivel//2
    camera_y = estado['pos_jogador'][1] - altura_visivel//2

    camera_x = max(0, min(camera_x, largura_mapa - largura_visivel)) # delimitação dos mínimos e máximos p/ que a camera não continue seu movimento quando o fim do mapa estiver visivel em qualquer das direções
    camera_y = max(0, min(camera_y, altura_mapa - altura_visivel))


    # delimitação dos limites de desenho p/ elementos dentro da janela visivel do mapa
    for y in range (altura_visivel): 
        for x in range(largura_visivel):
            x_mapa = (camera_x + x)
            y_mapa = (camera_y + y)
            posicao = [x_mapa, y_mapa]

            # desenho do jogador, objetos, itens e mosntros que compoem o jogo a cada atualização de estado do mapa
            motor.desenha_string(janela, x, y, ' ', VERDE_FLORESTA, VERDE_FLORESTA)

            if posicao == estado['pos_jogador']:
                motor.desenha_string(janela, x, y, JOGADOR, VERDE_FLORESTA, ROXO)

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

    # desenho do contador de vidas
    for x in range(estado['max_vidas']):
        if x < estado['vidas']:
            cor = VERMELHO
        else:
            cor = BRANCO
        motor.desenha_string(janela, x, 0, CORACAO, VERDE_FLORESTA, cor)

    # desenho do contador de níveis 
    nivel = estado['nivel'] 
    experiencia = estado['experiencia']
    motor.desenha_string(janela, 0, 1, f'Nível {nivel}: {experiencia}', VERDE_FLORESTA, BRANCO)

    # desenho das mensagens
    mensagem = estado['mensagem']
    motor.desenha_string(janela, 0, altura_tela - 1, mensagem, AZUL_ESCURO, BRANCO)


    motor.mostra_janela(janela)

def atualiza_estado(estado, tecla):
    estado['mensagem'] = ''

    mapa = estado['mapa']
    
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
    posicao_inicial_jogador = [x, y] # posicao inicial do jogador é guardada a cada passagem da função estado antes da tentativa de movimento de modo a permitir a verificação das posições de todos os monstros antes de seus movimentos

    if tecla == motor.SETA_ESQUERDA: # em todas as direções, o movimento é estruturado da mesma maneira, mudando apenas as coordenadas verificadas
        if [x-1, y] not in estado['paredes'] and [x-1, y] not in posicao_monstros and x-1 >= 0: # p/ movimentos permitidos dentro das especificações impostas
            x -= 1
            if [x, y] in posicao_itens: # coleta de itens
                for iten in itens:
                    if [x, y] == iten['posicao']:
                        coleta_iten_mapa(estado, iten, posicao_itens, posicoes_ocupadas, itens)
                        break

        elif [x-1, y] in posicao_monstros: # se o movimento atinge uma posição de monstro - batalha
            for monstro in monstros:
                if [x-1, y] == monstro['posicao']:
                    batalha(estado, monstro, posicao_monstros, posicoes_ocupadas, monstros)
                    break

        else: # p/ movimentos impedido por fatores que não monstros
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_DIREITA:
        if [x+1, y] not in estado['paredes'] and [x+1, y] not in posicao_monstros and x+1 < len(mapa[0]):
            x += 1
            if [x, y] in posicao_itens:
                for iten in itens:
                    if [x, y] == iten['posicao']:
                        coleta_iten_mapa(estado, iten, posicao_itens, posicoes_ocupadas, itens)
                        break

        elif [x+1, y] in posicao_monstros:
            for monstro in monstros:
                if [x+1, y] == monstro['posicao']:
                    batalha(estado, monstro, posicao_monstros, posicoes_ocupadas, monstros)
                    break

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_CIMA:
        if [x, y-1] not in estado['paredes'] and [x, y-1] not in posicao_monstros and y-1 >= 0:
            y -= 1
            if [x, y] in posicao_itens:
                for iten in itens:
                    if [x, y] == iten['posicao']:
                        coleta_iten_mapa(estado, iten, posicao_itens, posicoes_ocupadas, itens)
                        break

        elif [x, y-1] in posicao_monstros:
            for monstro in monstros:
                if [x, y-1] == monstro['posicao']:
                    batalha(estado, monstro, posicao_monstros, posicoes_ocupadas, monstros)
                    break

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_BAIXO:
        if [x, y+1] not in estado['paredes'] and [x, y+1] not in posicao_monstros and y+1 < len(mapa):
            y += 1
            if [x, y] in posicao_itens:
                for iten in itens:
                    if [x, y] == iten['posicao']:
                       coleta_iten_mapa(estado, iten, posicao_itens, posicoes_ocupadas, itens)
                       break

        elif [x, y+1] in posicao_monstros:
            for monstro in monstros:
                if [x, y+1] == monstro['posicao']:
                    batalha(estado, monstro, posicao_monstros, posicoes_ocupadas, monstros)
                    break

        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"


    if [x, y] != estado['pos_jogador']:
        estado['pos_jogador'] = [x, y] # atualização da posição do jogador na função de estado
        passa_por_objetos(estado)

    movimento_dos_monstros(estado, tecla, posicao_inicial_jogador) # verificação das possibilidades de movimento dos mosntros de acordo com coordenadas do jogador pré-atualização, permitindo o correto funcionamento das batalhas

    # definição de retorno à tela do jogo ou saída do jogo
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO

    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR

    # definição do estado do inventário
    atualizacao_inventario(estado, tecla) # verificação do inventario a depender da coleta e uso de itens

    niveis(estado) # verificação do nivel do jogador apos batalhas ou uso de elixires para aumento de experiencia 