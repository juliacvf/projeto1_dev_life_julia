from constantes import *
import motor_grafico as motor
from funcoes_auxiliares import atualizacao_inventario


def desenha_tela(janela, estado, altura, largura):
    # posicionamento das partes escritas na tela
    motor.preenche_fundo(janela, MARROM_ESCURO)
    motor.desenha_string(janela, (largura-(len('inventario')))//2, 3, 'INVENTÁRIO', MARROM_ESCURO, AMARELO_DOURADO)
    motor.desenha_string(janela, (largura-(len('----------')))//2, 4, '----------', MARROM_ESCURO, AMARELO_DOURADO)


    # conexão com função de estado p/ atualização da tela do inventário a cada coleta ou uso de itens de acordo com o estado do inventário
    itens = estado['itens']
    for iten in itens:
        if iten['tipo'] == POCAO:
            motor.desenha_string(janela, (largura-len('poção ⚗ : 0x'))//2, 8, f"POÇÃO ⚗ : {estado['inventario']['⚗']}", MARROM_ESCURO, BRANCO)
        elif iten['tipo'] == ELIXIR:
            motor.desenha_string(janela, (largura-len('elixir ⚗ : 0x'))//2, 12, f"ELIXIR ✦ : {estado['inventario']['✦']}", MARROM_ESCURO, BRANCO)
        elif iten['tipo'] == ESPADA:
            motor.desenha_string(janela, (largura-len('espada ⚗ : 0x'))//2, 16, f"ESPADA † : {estado['inventario']['†']}", MARROM_ESCURO, BRANCO)
        elif iten['tipo'] == MARTELO:
            motor.desenha_string(janela, (largura-len('martelo ⚗ : 0x'))//2, 20, f"MARTELO ⚒ : {estado['inventario']['⚒']}", MARROM_ESCURO, BRANCO)
        elif iten['tipo'] == CHAVE:
            motor.desenha_string(janela, (largura-len('chave ⚗ : 0x'))//2, 24, f"CHAVE ⚿ : {estado['inventario']['⚿']}", MARROM_ESCURO, BRANCO)
        mensagem = estado['mensagem']
        motor.desenha_string(janela, 0, altura - 1, mensagem, AZUL_ESCURO, BRANCO)

    # desenho dos detalhes das bordas
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
    # definição de retorno à tela do jogo ou saída do jogo
    if tecla == 'i':
        estado['tela_atual'] = TELA_JOGO
    elif tecla in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR
    
    # definição do estado do inventário
    atualizacao_inventario(estado, tecla)
