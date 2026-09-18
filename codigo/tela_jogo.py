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

                if estado['max_vidas'] - estado['vidas'] == 0:
                    if y == 0 and x in range(5):
                        motor.desenha_string(janela, x, y, CORACAO, PRETO, VERMELHO)

                if estado['max_vidas'] - estado['vidas'] != 0:
                    if y == 0 and x in range(estado['vidas']):
                        motor.desenha_string(janela, x, y, CORACAO, PRETO, VERMELHO)

                    if y == 0 and x in range(estado['vidas']+1, estado['max_vidas']):
                        motor.desenha_string(janela, x, y, CORACAO, PRETO, BRANCO)

                    if y == len(mapa)-1 and x in range(6):
                        mensagem = estado['mensagem']
                        motor.desenha_string(janela, x, y, mensagem, PRETO, AMARELO)

                for objeto in estado['objetos']:
                    if posicao == objeto['posicao']:
                        motor.desenha_string(janela, inicio_x + x, inicio_y + y, objeto['tipo'], VERDE_ESCURO, objeto['cor'])

    motor.mostra_janela(janela)



def atualiza_estado(estado, tecla):
    # O seu código deve atualizar o dicionário "estado" com base na tecla apertada pelo jogador
    # Por exemplo, se o jogador apertar a seta para a esquerda (o valor da variável será "ESQUERDA"), 
    # o seu código deve atualizar o dicionário estado['pos_jogador'][0] -= 1

    # Mude o valor da chave 'tela_atual' para mudar de tela
    
    # Começamos apagando a mensagem anterior, pois ela já foi mostrada no frame anterior
    estado['mensagem'] = ''

    # Escreva seu código para atualizar o dicionário "estado" com base na tecla apertada pelo jogador aqui
    # APAGUE ESTA LINHA E ESCREVA SEU CÓDIGO AQUI

    # Ao apertar a tecla 'i', o jogador deve ver o inventário
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR