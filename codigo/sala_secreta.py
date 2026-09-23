from constantes import *
import motor_grafico as motor
import random 


def desenha_tela(janela, estado, altura, largura):
     motor.preenche_fundo(janela, AZUL_ESCURO)
     
    


def atualiza_estado(estado, tecla):
    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    elif tecla in (motor.ESCAPE, 'q'):
        estado['tela_atual'] = SAIR
    elif tecla == motor.ESCAPE:
        estado['tela_atual'] = TELA_JOGO

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
        if estado['inventario']['†'] >= -1:
                estado['inventario']['†'] -= 1
                for monstro in estado['monstros']:
                    if monstro['tipo'] == MONSTRO1:
                        monstro['probabilidade de ataque'] = 0.25
                    if monstro['tipo'] == MONSTRO2:
                        monstro['probabilidade de ataque'] = 0.40
                    if monstro['tipo'] == MONSTRO3:
                        monstro['probabilidade de ataque'] = 0.55

        else:
            estado['mensagem'] = 'Você não têm espadas'


    elif tecla == 'h':
        if estado['inventario']['⚒'] >= 1:
                estado['inventario']['⚒'] -= 1
                for monstro in estado['monstros']:
                    if monstro['tipo'] == MONSTRO1:
                        monstro['vida'] = 4
                    if monstro['tipo'] == MONSTRO2:
                        monstro['vida'] = 2
                    if monstro['tipo'] == MONSTRO3:
                        monstro['vida'] = 1

        else:
            estado['mensagem'] = 'Você não têm martelos'
    
