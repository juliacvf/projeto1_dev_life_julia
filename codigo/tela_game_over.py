from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, AZUL_ESCURO)
    motor.desenha_string(janela, (largura-len('game over'))//2, 5, 'GAME OVER', AZUL_ESCURO, VERMELHO)
    motor.desenha_string(janela, (largura-len('game over'))//2, 6, '---------', AZUL_ESCURO, AMARELO_DOURADO)
    motor.desenha_string(janela, (largura-len('menu inicial - ↑'))//2, altura//2-1, 'MENU INICIAL - ↑', AZUL_ESCURO, BRANCO)
    motor.desenha_string(janela, (largura-len('sair do jogo - esc/q'))//2, altura//2+1, 'SAIR DO JOGO - esc/q', AZUL_ESCURO, BRANCO)
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
        estado['tela_atual'] = TELA_INICIAL

    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
