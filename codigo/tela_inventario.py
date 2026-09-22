from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, MARROM_ESCURO)
    motor.desenha_string(janela, (largura-(len('inventario')))//2, 5, 'INVENTÁRIO', MARROM_ESCURO, AMARELO_DOURADO)
    motor.desenha_string(janela, (largura-(len('----------')))//2, 6, '----------', MARROM_ESCURO, AMARELO_DOURADO)
    for y in range(2, altura - 2):
        motor.desenha_string(janela, 1, y, '|', MARROM_ESCURO, MARROM_MAIS_ESCURO)
        motor.desenha_string(janela, largura - 2, y, '|', MARROM_ESCURO, MARROM_MAIS_ESCURO)

    for x in range(2, largura - 2):
        motor.desenha_string(janela, x, 1, '-', MARROM_ESCURO, MARROM_MAIS_ESCURO)
        motor.desenha_string(janela, x, altura - 2, '-', MARROM_ESCURO, MARROM_MAIS_ESCURO)


    motor.desenha_string(janela, 1, 1, '+', MARROM_ESCURO, MARROM_MAIS_ESCURO)
    motor.desenha_string(janela, largura - 2, 1, '+', MARROM_ESCURO, MARROM_MAIS_ESCURO)
    motor.desenha_string(janela, 1, altura - 2, '+', MARROM_ESCURO, MARROM_MAIS_ESCURO)
    motor.desenha_string(janela, largura - 2, altura - 2, '+', MARROM_ESCURO, MARROM_MAIS_ESCURO)
    
    motor.mostra_janela(janela)


def atualiza_estado(estado, tecla):
    if tecla == 'i':
        estado['tela_atual'] = TELA_JOGO
    elif tecla in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR