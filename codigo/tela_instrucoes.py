from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, BRANCO)
    motor.desenha_string(janela, largura//2, 1, 'INSTRUÇÕES', BRANCO, PRETO)
    
    motor.mostra_janela(janela)

def atualiza_estado(estado, tecla):
    if tecla == motor.SETA_BAIXO:
        estado['tela_atual'] = TELA_INICIAL
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
