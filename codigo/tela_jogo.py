from constantes import *
import motor_grafico as motor
import random   

def desenha_tela(janela, estado, altura_tela, largura_tela):
    motor.preenche_fundo(janela, PRETO)

    if estado['tela_atual'] == TELA_JOGO:
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

        mensagem = estado['mensagem']
        motor.desenha_string(janela, 0, altura_tela - 1, mensagem, PRETO, AMARELO)

    motor.mostra_janela(janela)



def atualiza_estado(estado, tecla):
    estado['mensagem'] = ''
    mapa = estado['mapa']
    monstros = estado['monstros']
    posicao_monstros = []
    for monstro in monstros:
        posicao_monstros.append(monstro['posicao'])


    x = estado['pos_jogador'][0]
    y = estado['pos_jogador'][1]

    
    if tecla == motor.SETA_ESQUERDA:
        if [x-1, y] not in estado['paredes'] and [x-1, y] not in posicao_monstros:
            if x-1 >= 0:
                x -= 1
        elif [x-1, y] in posicao_monstros:
            estado['mensagem'] = "Você não pode se mover nessa direção"
            numero = random.random()
            if numero < 0.3:
                if estado['vidas'] > 1:
                    estado['vidas'] -= 1             
                    estado['mensagem'] = "Você perdeu uma vida"
                else:
                    estado['vidas'] -= 1
                    estado['mensagem'] = "Você perdeu todas as vidas"
                    estado['tela_atual'] = SAIR
            else:
                for monstro in monstros:
                    if monstro['posicao'] == [x-1, y]:
                        monstro['vida'] -= 1
                        estado['mensagem'] = "O monstro perdeu uma vida"
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_DIREITA:
        if [x+1, y] not in estado['paredes'] and [x+1, y] not in posicao_monstros:
            if x+1 < len(mapa[0]):
                x += 1
        elif [x+1, y] in posicao_monstros:
            estado['mensagem'] = "Você não pode se mover nessa direção"
            numero = random.random()
            if numero < 0.3:
                if estado['vidas'] > 1:
                    estado['vidas'] -= 1             
                    estado['mensagem'] = "Você perdeu uma vida"
                else:
                    estado['vidas'] -= 1
                    estado['mensagem'] = "Você perdeu todas as vidas"
                    estado['tela_atual'] = SAIR
            else:
                for monstro in monstros:
                    if monstro['posicao'] == [x+1, y]:
                        monstro['vida'] -= 1
                        estado['mensagem'] = "O monstro perdeu uma vida"
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"
                  
    elif tecla == motor.SETA_CIMA:
        if [x, y-1] not in estado['paredes'] and [x, y-1] not in posicao_monstros:
            if y-1 >= 0:
                y -= 1
        elif [x, y-1] in posicao_monstros:
            estado['mensagem'] = "Você não pode se mover nessa direção"
            numero = random.random()
            if numero < 0.3:
                if estado['vidas'] > 1:
                    estado['vidas'] -= 1             
                    estado['mensagem'] = "Você perdeu uma vida"
                else:
                    estado['vidas'] -= 1
                    estado['mensagem'] = "Você perdeu todas as vidas"
                    estado['tela_atual'] = SAIR
            else:
                for monstro in monstros:
                    if monstro['posicao'] == [x, y-1]:
                        monstro['vida'] -= 1
                        estado['mensagem'] = "O monstro perdeu uma vida"
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
        else:
            estado['mensagem'] = "Você não pode se mover nessa direção"

    elif tecla == motor.SETA_BAIXO:
        if [x, y+1] not in estado['paredes'] and [x, y+1] not in posicao_monstros:
            if y+1 < len(mapa):
                y += 1
        elif [x, y+1] in posicao_monstros:
            estado['mensagem'] = "Você não pode se mover nessa direção"
            numero = random.random()
            if numero < 0.3:
                if estado['vidas'] > 1:
                    estado['vidas'] -= 1             
                    estado['mensagem'] = "Você perdeu uma vida"
                else:
                    estado['vidas'] -= 1
                    estado['mensagem'] = "Você perdeu todas as vidas"
                    estado['tela_atual'] = SAIR
            else:
                for monstro in monstros:
                    if monstro['posicao'] == [x, y+1]:
                        monstro['vida'] -= 1
                        estado['mensagem'] = "O monstro perdeu uma vida"
                        if monstro['vida'] == 0:
                            monstros.remove(monstro)
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
                        estado['mensagem'] = "Você perdeu todas as vidas"
                        estado['tela_atual'] = SAIR

                elif objeto['tipo'] == CORACAO:
                    if estado['vidas'] == estado['max_vidas']:
                         estado['mensagem'] = "Vida cheia"
                    else:
                        estado['vidas'] += 1
                        estado['mensagem'] = "Você ganhou uma vida"

                    estado['objetos'].remove(objeto)
                

    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO

    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR

