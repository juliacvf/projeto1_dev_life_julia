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
                estado['vidas'] -= 1
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
        if estado['equipamento'] is None:
            if estado['inventario']['†'] >= 1:
                estado['inventario']['†'] -= 1
                estado['equipamento'] = 'espada'
                estado['mensagem'] = 'Espada equipada'
                for monstro in estado['monstros']:
                    if monstro['tipo'] == MONSTRO1:
                        monstro['probabilidade de ataque'] = 0.25

                    elif monstro['tipo'] == MONSTRO2:
                        monstro['probabilidade de ataque'] = 0.40

                    elif monstro['tipo'] == MONSTRO3:
                        monstro['probabilidade de ataque'] = 0.55

            else:
                estado['mensagem'] = 'Você não tem espada para equipar'

        elif estado['equipamento'] == 'espada':
            estado['equipamento'] = None
            estado['mensagem'] = 'Espada desequipada'

            for monstro in estado['monstros']:
                if monstro['tipo'] == MONSTRO1:
                    monstro['probabilidade de ataque'] = 0.30

                elif monstro['tipo'] == MONSTRO2:
                    monstro['probabilidade de ataque'] = 0.45

                elif monstro['tipo'] == MONSTRO3:
                    monstro['probabilidade de ataque'] = 0.70

        else:
            estado['mensagem'] = 'Você já possui outro item equipado'

    elif tecla == 'h':
        if estado['equipamento'] is None:

            if estado['inventario']['⚒'] >= 1:
                estado['inventario']['⚒'] -= 1
                estado['equipamento'] = 'martelo'
                estado['mensagem'] = 'Martelo equipado'

                for monstro in estado['monstros']:
                    if monstro['tipo'] == MONSTRO1:
                        monstro['max_vidas'] = 4

                    elif monstro['tipo'] == MONSTRO2:
                        monstro['max_vidas'] = 2

                    elif monstro['tipo'] == MONSTRO3:
                        monstro['max_vidas'] = 1

                    if monstro['vida'] > monstro['max_vidas']:
                        monstro['vida'] = monstro['max_vidas']

            else:
                estado['mensagem'] = 'Você não tem martelo para equipar'

        elif estado['equipamento'] == 'martelo':
            estado['equipamento'] = None
            estado['mensagem'] = 'Martelo desequipado'

            for monstro in estado['monstros']:
                if monstro['tipo'] == MONSTRO1:
                    monstro['max_vidas'] = 5

                elif monstro['tipo'] == MONSTRO2:
                    monstro['max_vidas'] = 3

                elif monstro['tipo'] == MONSTRO3:
                    monstro['max_vidas'] = 2


        else:
            estado['mensagem'] = 'Você já possui outro item equipado'
        

    elif tecla == 'k':
        if estado['inventario']['⚿'] < 3:  
            estado['mensagem'] = 'Você ainda não pode acessar a sala secreta'
        else: 
            estado['inventario']['⚿'] -= 3
            estado['tela_atual'] = SALA_SECRETA