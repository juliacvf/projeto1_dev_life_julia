from constantes import *
import motor_grafico as motor
import random 


def desenha_tela(janela, estado, altura, largura):
    itens = estado['itens']

    motor.preenche_fundo(janela, MARROM_ESCURO)
    motor.desenha_string(janela, (largura-(len('inventario')))//2, 5, 'INVENTÁRIO', MARROM_ESCURO, AMARELO_DOURADO)
    motor.desenha_string(janela, (largura-(len('----------')))//2, 6, '----------', MARROM_ESCURO, AMARELO_DOURADO)

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
    itens = estado['itens']
    inventário = estado['inventario']

    if tecla == 'i':
        estado['tela_atual'] = TELA_JOGO
    elif tecla in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR

    elif tecla == 'p':
        if estado['inventario']['⚗'] >= 1:
            estado['inventario']['⚗'] -= 1
            numero = random.random()
            if numero <= 0.4:
                estado['max_vidas'] -= 1
            else:
                estado['max_vidas'] += 1
                estado['vidas'] += 1

        else:
            estado['mensagem'] = 'Você não tem poções'

    elif tecla == 'e':
        if estado['inventario']['✦'] >= 1:
            estado['inventario']['✦'] -= 1
            estado['experiencia'] += 2

        else:
            estado['mensagem'] = 'Você não tem elixir'

    elif tecla == 's':
        if estado['inventario']['†'] >= 1:
            estado['inventario']['†'] -= 1
            for monstro in estado['monstros']:
                if monstro['tipo'] == MONSTRO1:
                    monstro['probabilidade de ataque'] == 0.25
                if monstro['tipo'] == MONSTRO1:
                    monstro['probabilidade de ataque'] == 0.40
                if monstro['tipo'] == MONSTRO1:
                    monstro['probabilidade de ataque'] == 0.55

        else:
            estado['mensagem'] = 'Você não têm espadas'

    elif tecla == 'h':
        if estado['inventario']['⚒'] >= 1:
            estado['inventario']['⚒'] -= 1
            for monstro in estado['monstros']:

                if monstro['tipo'] == MONSTRO1:
                    monstro['vida'] == 4
                if monstro['tipo'] == MONSTRO1:
                    monstro['vida'] == 2
                if monstro['tipo'] == MONSTRO1:
                    monstro['vida'] == 1
        else:
            estado['mensagem'] = 'Você não têm martelos'

    elif tecla == 'k':
        if estado['inventario']['⚿'] < 3:  
            estado['mensagem'] = 'Você ainda não pode acessar a sala secreta'
        else: 
            estado['inventario']['⚿'] -= 3
            estado['tela'] = SALA_SECRETA


    
        
        