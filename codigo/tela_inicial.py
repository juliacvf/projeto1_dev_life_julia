from constantes import *
import motor_grafico as motor
from inicializacao import inicializa_estado


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, BRANCO)
    motor.desenha_string(janela, largura//2, 1, 'NOME DO JOGO', BRANCO, PRETO)
    motor.desenha_string(janela, largura//2, (altura//2)-2, 'JOGAR', BRANCO, PRETO)
    motor.desenha_string(janela, largura//2, (altura//2)-1, '(Press ESPACO)', BRANCO, PRETO)
    motor.desenha_string(janela, largura//2, (altura//2)+1, 'INSTRUÇÕES', BRANCO, PRETO)
    motor.desenha_string(janela, largura//2, (altura//2)+2, '(Press ENTER)', BRANCO, PRETO)
    motor.mostra_janela(janela)

def atualiza_estado(estado, tecla):
    if tecla == motor.ESPACO:
        novo_estado = inicializa_estado()
        estado.clear()
        estado.update(novo_estado)
        estado['tela_atual'] = TELA_JOGO
    elif tecla == motor.SETA_BAIXO:
        estado['tela_atual'] = TELA_INSTRUCOES
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
