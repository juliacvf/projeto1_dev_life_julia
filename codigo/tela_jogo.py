from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código
import motor_grafico as motor  # Utilize as funções do arquivo motor_grafico.py para desenhar na tela
                               # Por exemplo: motor.preenche_fundo(janela, [0, 0, 0]) preenche o fundo de preto


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

    x = estado['pos_jogador'][0]
    y = estado['pos_jogador'][1]

    
    if tecla == motor.SETA_ESQUERDA:
        if x-1 >= 0:
            x -= 1
    elif tecla == motor.SETA_DIREITA:
        if x+1 < len(mapa[0]):
            x += 1

    elif tecla == motor.SETA_CIMA:
       if y-1 >= 0:
            y -= 1

    elif tecla == motor.SETA_BAIXO:
        if y+1 < len(mapa):
            y += 1

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

