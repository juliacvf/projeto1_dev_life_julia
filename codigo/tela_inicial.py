from constantes import *
import motor_grafico as motor
from inicializacao import inicializa_estado


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, AZUL_ESCURO)
    motor.desenha_string(janela, (largura-len('◆ entre monstros e muros ◆'))//2, 5, '◆ ENTRE MONSTROS E MUROS ◆', AZUL_ESCURO, AMARELO_DOURADO)
    motor.desenha_string(janela, (largura-len('jogar - ↑'))//2, (altura//2)-1, 'JOGAR - ↑', AZUL_ESCURO, BRANCO)
    motor.desenha_string(janela, (largura-len('instrucoes - ↓'))//2, (altura//2)+1, 'INSTRUÇÕES - ↓', AZUL_ESCURO, BRANCO)

   
    for y in range(2, altura - 2):
        motor.desenha_string(janela, 1, y, '|', AZUL_ESCURO, MARROM)
        motor.desenha_string(janela, largura - 2, y, '|', AZUL_ESCURO, MARROM)

    for x in range(2, largura - 2):
        motor.desenha_string(janela, x, 1, '-', AZUL_ESCURO, MARROM)
        motor.desenha_string(janela, x, altura - 2, '-', AZUL_ESCURO, MARROM)

    
    motor.desenha_string(janela, 1, 1, '+', AZUL_ESCURO, MARROM)
    motor.desenha_string(janela, largura - 2, 1, '+', AZUL_ESCURO, MARROM)
    motor.desenha_string(janela, 1, altura - 2, '+', AZUL_ESCURO, MARROM)
    motor.desenha_string(janela, largura - 2, altura - 2, '+', AZUL_ESCURO, MARROM)

    motor.mostra_janela(janela)

def atualiza_estado(estado, tecla):
    if tecla == motor.SETA_CIMA:
        novo_estado = inicializa_estado()
        estado.clear()
        estado.update(novo_estado)
        estado['tela_atual'] = TELA_JOGO
    elif tecla == motor.SETA_BAIXO:
        estado['tela_atual'] = TELA_INSTRUCOES
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
