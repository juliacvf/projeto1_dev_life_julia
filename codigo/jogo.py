import motor_grafico
import tela_inventario
import tela_jogo
import tela_inicial
import tela_instrucoes
import tela_game_over
import tela_sala_secreta
from constantes import SAIR, TELA_INVENTARIO, TELA_JOGO, TELA_INICIAL, TELA_INSTRUCOES, TELA_GAME_OVER, TELA_SALA_SECRETA
from inicializacao import inicializa_estado


def jogo(janela, altura_tela, largura_tela):
    estado = inicializa_estado()

    print(altura_tela)

    while estado['tela_atual'] != SAIR:
        
        if estado['tela_atual'] == TELA_INICIAL:
            tela_inicial.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla = motor_grafico.pega_tecla_apertada(janela)
            tela_inicial.atualiza_estado(estado, tecla)

        elif estado['tela_atual'] == TELA_JOGO:
            tela_jogo.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla = motor_grafico.pega_tecla_apertada(janela)
            tela_jogo.atualiza_estado(estado, tecla)

        elif estado['tela_atual'] == TELA_INVENTARIO:
            tela_inventario.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla = motor_grafico.pega_tecla_apertada(janela)
            tela_inventario.atualiza_estado(estado, tecla)

        elif estado['tela_atual'] == TELA_INSTRUCOES:
            tela_instrucoes.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla = motor_grafico.pega_tecla_apertada(janela)
            tela_instrucoes.atualiza_estado(estado, tecla)

        elif estado['tela_atual'] == TELA_GAME_OVER:
            tela_game_over.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla = motor_grafico.pega_tecla_apertada(janela)
            tela_game_over.atualiza_estado(estado, tecla)

        elif estado['tela_atual'] == TELA_SALA_SECRETA:
            tela_sala_secreta.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla = motor_grafico.pega_tecla_apertada(janela)
            tela_sala_secreta.atualiza_estado(estado, tecla)



# Não se preocupe, você não precisa entender o que está acontecendo aqui.
# É apenas uma forma de chamar a função jogo() usando a biblioteca curses.
motor_grafico.chama_funcao_jogo(jogo)